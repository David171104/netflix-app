# 🚀 FastAPI + Svelte + MySQL — Proyecto Dockerizado

Stack completo dockerizado con FastAPI, Svelte, MySQL, phpMyAdmin y Nginx.

## 📦 Servicios

| Servicio     | Tecnología              | Puerto local |
|--------------|-------------------------|--------------|
| `nginx`      | Nginx (reverse proxy)   | `80`         |
| `backend`    | FastAPI + Uvicorn       | `8000`       |
| `frontend`   | Svelte (build estático) | interno      |
| `db`         | MySQL 8                 | `3306`       |
| `phpmyadmin` | phpMyAdmin              | `8080`       |

## ⚙️ Requisitos

- [Docker](https://www.docker.com/) >= 24
- [Docker Compose](https://docs.docker.com/compose/) >= 2.x

## 🛠️ Configuración

1. Copia el archivo de entorno y ajusta los valores:
```bash
cp .env .env.local  # opcional, .env ya está listo para desarrollo
```

2. Variables importantes en `.env`:

```env
MYSQL_ROOT_PASSWORD=root_secret
MYSQL_USER=app_user
MYSQL_PASSWORD=app_password
DATABASE_URL=mysql+mysqlconnector://app_user:app_password@db:3306/mydb
SECRET_KEY=cambia_esto_en_produccion
```

## 🚀 Levantar el proyecto

```bash
# Construir y levantar todos los servicios
docker compose up --build

# En segundo plano
docker compose up --build -d

# Ver logs en tiempo real
docker compose logs -f

# Ver logs de un servicio específico
docker compose logs -f backend
```

## 🔗 URLs de acceso

| Servicio     | URL                                  |
|--------------|--------------------------------------|
| App (nginx)  | http://localhost                     |
| API directa  | http://localhost:8000/api/           |
| Docs API     | http://localhost:8000/docs           |
| phpMyAdmin   | http://localhost:8080                |

## 🗂️ Estructura del proyecto

```
project/
├── backend/
│   ├── app/
│   │   └── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   └── Dockerfile
├── nginx/
│   └── default.conf
├── .env
├── docker-compose.yml
└── README.md
```

## 🧹 Comandos útiles

```bash
# Detener todos los servicios
docker compose down

# Detener y eliminar volúmenes (borra la DB)
docker compose down -v

# Reconstruir solo un servicio
docker compose up --build backend

# Ejecutar comandos dentro de un contenedor
docker compose exec backend bash
docker compose exec db mysql -u root -p

# Ver estado de los contenedores
docker compose ps
```

## 📝 Notas de desarrollo

- El backend usa **hot-reload** vía volumen montado (`./backend:/app`), los cambios se reflejan sin reconstruir.
- El frontend se **compila en el build** (`npm run build`). Para desarrollo activo de Svelte, se recomienda correr `npm run dev` localmente y usar el proxy de Vite.
- La DB tiene un **healthcheck** configurado; el backend y phpMyAdmin esperan a que MySQL esté listo antes de iniciar.