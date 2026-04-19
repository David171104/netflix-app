// src/lib/api.js
// Todas las llamadas al backend FastAPI van aquí.
// El BASE_URL usa /api porque nginx redirige /api/ → FastAPI.

const BASE_URL = '/api';

// ── Utilidad interna ───────────────────────────────────────────────
async function request(endpoint, options = {}) {
  const url = `${BASE_URL}${endpoint}`;

  const res = await fetch(url, {
    headers: { 'Content-Type': 'application/json', ...options.headers },
    ...options,
  });

  const data = await res.json().catch(() => null);

  if (!res.ok) {
    const mensaje = data?.detail || `Error ${res.status}`;
    throw new Error(mensaje);
  }

  return data;
}

// ── Usuarios ───────────────────────────────────────────────────────

/**
 * Registra un nuevo usuario.
 * @param {{ nombre: string, apellido: string, contrasena: string }} usuario
 */
export async function registrarUsuario(usuario) {
  return request('/usuarios/registro', {
    method: 'POST',
    body: JSON.stringify(usuario),
  });
}

/**
 * Obtiene la lista de todos los usuarios (solo admin).
 */
export async function getUsuarios() {
  return request('/usuarios');
}

// ── Películas ──────────────────────────────────────────────────────

/**
 * Obtiene todas las películas.
 */
export async function getPeliculas() {
  return request('/peliculas');
}

/**
 * Obtiene una película por ID.
 * @param {number} id
 */
export async function getPelicula(id) {
  return request(`/peliculas/${id}`);
}

/**
 * Crea una nueva película.
 * @param {{ titulo: string, descripcion: string, reparto: string, imagen: string }} pelicula
 */
export async function crearPelicula(pelicula) {
  return request('/peliculas', {
    method: 'POST',
    body: JSON.stringify(pelicula),
  });
}

/**
 * Elimina una película por ID.
 * @param {number} id
 */
export async function eliminarPelicula(id) {
  return request(`/peliculas/${id}`, { method: 'DELETE' });
}

// ── Favoritos ──────────────────────────────────────────────────────

/**
 * Obtiene las películas favoritas de un usuario.
 * @param {number} usuarioId
 */
export async function getFavoritos(usuarioId) {
  return request(`/favoritos/${usuarioId}`);
}

/**
 * Agrega una película a favoritos.
 * @param {{ usuario_id: number, pelicula_id: number }} favorito
 */
export async function agregarFavorito(favorito) {
  return request('/favoritos', {
    method: 'POST',
    body: JSON.stringify(favorito),
  });
}

/**
 * Elimina una película de favoritos.
 * @param {number} usuarioId
 * @param {number} peliculaId
 */
export async function eliminarFavorito(usuarioId, peliculaId) {
  return request(`/favoritos/${usuarioId}/${peliculaId}`, { method: 'DELETE' });
}

// ── Health ─────────────────────────────────────────────────────────

/**
 * Verifica el estado de la API y la base de datos.
 */
export async function checkHealth() {
  return request('/health');
}