from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import mysql.connector
from mysql.connector import Error
from decouple import config
import os
from werkzeug.security import generate_password_hash

# ─── App ──────────────────────────────────────────────────────────────────────
app = FastAPI(
    title="Netflix App API",
    description="Backend para la aplicación de streaming",
    version="1.0.0",
)

# ─── CORS ─────────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:80", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Hash de contraseñas ───────────────────────────────────────────────────────


# ─── Conexión a MySQL ──────────────────────────────────────────────────────────


def get_db():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST", "db"),
            port=int(os.getenv("MYSQL_PORT", 3306)),
            user=os.getenv("MYSQL_USER", "user"),
            password=os.getenv("MYSQL_PASSWORD", "password"),
            database=os.getenv("MYSQL_DATABASE", "bd_netflix"),
        )
        return conn
    except Error as e:
        raise HTTPException(status_code=503, detail=f"Error de conexión a la BD: {e}")

# ─── Modelos ───────────────────────────────────────────────────────────────────

class UsuarioRegistro(BaseModel):
    nombre: str
    apellido: str
    contrasena: str

class PeliculaCreate(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    reparto: Optional[str] = None
    imagen: Optional[str] = None

class FavoritoCreate(BaseModel):
    usuario_id: int
    pelicula_id: int

# ─── Health ────────────────────────────────────────────────────────────────────

@app.get("/api/")
def root():
    return {"message": "Netflix App API 🎬", "status": "ok"}

@app.get("/api/health")
def health_check():
    db_status = "ok"
    try:
        conn = get_db()
        conn.close()
    except Exception as e:
        db_status = f"error: {e}"
    return {
        "api": "ok",
        "database": db_status,
        "env": config("APP_ENV", default="local"),
    }

# ─── Usuarios ──────────────────────────────────────────────────────────────────

@app.post("/api/usuarios/registro", status_code=201)
def registrar_usuario(usuario: UsuarioRegistro):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    try:
        # 🔍 Validar longitud básica (opcional pero recomendable)
        if len(usuario.contrasena) < 6:
            raise HTTPException(
                status_code=400,
                detail="La contraseña debe tener al menos 6 caracteres."
            )

        # 🔍 Verificar si ya existe
        cursor.execute(
            "SELECT id FROM usuarios WHERE nombre = %s AND apellido = %s",
            (usuario.nombre, usuario.apellido)
        )
        if cursor.fetchone():
            raise HTTPException(
                status_code=400,
                detail="El usuario ya está registrado."
            )

        # 🔐 Hash con scrypt (sin límite de bcrypt)
        hash_pw = generate_password_hash(
            usuario.contrasena,
            method='scrypt'
        )

        # 💾 Insertar usuario
        cursor.execute(
            "INSERT INTO usuarios (nombre, apellido, contrasena, rol) VALUES (%s, %s, %s, 'user')",
            (usuario.nombre, usuario.apellido, hash_pw)
        )
        conn.commit()

        return {
            "id": cursor.lastrowid,
            "nombre": usuario.nombre,
            "apellido": usuario.apellido,
            "rol": "user",
            "mensaje": "Usuario registrado correctamente."
        }

    except HTTPException:
        raise
    except Error as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"DB Error: {str(e)}")
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Server Error: {str(e)}")

    finally:
        cursor.close()
        conn.close()

@app.get("/api/usuarios")
def get_usuarios():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT id, nombre, apellido, rol, creado_en FROM usuarios")
        return {"usuarios": cursor.fetchall()}
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# ─── Películas ─────────────────────────────────────────────────────────────────

@app.get("/api/peliculas")
def get_peliculas():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM peliculas")
        return {"peliculas": cursor.fetchall()}
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@app.get("/api/peliculas/{pelicula_id}")
def get_pelicula(pelicula_id: int):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM peliculas WHERE id = %s", (pelicula_id,))
        pelicula = cursor.fetchone()
        if not pelicula:
            raise HTTPException(status_code=404, detail="Película no encontrada.")
        return pelicula
    except HTTPException:
        raise
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@app.post("/api/peliculas", status_code=201)
def crear_pelicula(pelicula: PeliculaCreate):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO peliculas (titulo, descripcion, reparto, imagen) VALUES (%s, %s, %s, %s)",
            (pelicula.titulo, pelicula.descripcion, pelicula.reparto, pelicula.imagen)
        )
        conn.commit()
        return {"id": cursor.lastrowid, **pelicula.model_dump()}
    except Error as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@app.delete("/api/peliculas/{pelicula_id}")
def eliminar_pelicula(pelicula_id: int):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM peliculas WHERE id = %s", (pelicula_id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Película no encontrada.")
        return {"mensaje": f"Película {pelicula_id} eliminada."}
    except HTTPException:
        raise
    except Error as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# ─── Favoritos ─────────────────────────────────────────────────────────────────

@app.get("/api/favoritos/{usuario_id}")
def get_favoritos(usuario_id: int):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT p.id, p.titulo, p.descripcion, p.reparto, p.imagen, f.agregado_en
            FROM favoritos f
            JOIN peliculas p ON f.pelicula_id = p.id
            WHERE f.usuario_id = %s
        """, (usuario_id,))
        return {"favoritos": cursor.fetchall()}
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@app.post("/api/favoritos", status_code=201)
def agregar_favorito(favorito: FavoritoCreate):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO favoritos (usuario_id, pelicula_id) VALUES (%s, %s)",
            (favorito.usuario_id, favorito.pelicula_id)
        )
        conn.commit()
        return {"mensaje": "Película agregada a favoritos."}
    except Error as e:
        if e.errno == 1062:
            raise HTTPException(status_code=400, detail="Ya está en favoritos.")
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@app.delete("/api/favoritos/{usuario_id}/{pelicula_id}")
def eliminar_favorito(usuario_id: int, pelicula_id: int):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "DELETE FROM favoritos WHERE usuario_id = %s AND pelicula_id = %s",
            (usuario_id, pelicula_id)
        )
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Favorito no encontrado.")
        return {"mensaje": "Película eliminada de favoritos."}
    except HTTPException:
        raise
    except Error as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()