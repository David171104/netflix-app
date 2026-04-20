<script>
  import { createEventDispatcher } from 'svelte';
  import { agregarFavorito } from '$lib/api.js';
  import Swal from 'sweetalert2';

  export let movie;
  export let isFavorite = false;
  let imageError = false;
  let imageLoaded = false;
  
  const dispatch = createEventDispatcher();

  function handleError() {
    imageError = true;
  }

  function handleLoad() {
    imageLoaded = true;
  }

  async function toggleFavorite(e) {
    const userStr = localStorage.getItem('usuario');
    if (!userStr) {
      Swal.fire({
        title: 'Acceso Denegado',
        text: 'Inicia sesión para poder añadir películas a tu lista de favoritos.',
        icon: 'warning',
        confirmButtonColor: '#e50914',
        background: '#141414',
        color: '#fff'
      });
      return;
    }
    const user = JSON.parse(userStr);
    
    try {
      const res = await agregarFavorito({ usuario_id: user.id, pelicula_id: movie.id });
      isFavorite = (res.estado === "agregado");
      dispatch('favToggled', { movieId: movie.id, isFavorite });
    } catch (err) {
      console.error(err);
    }
  }
</script>

<!-- svelte-ignore a11y-click-events-have-key-events a11y-no-static-element-interactions -->
<div class="movie-card" on:click>
  {#if !imageError && movie.image}
    <div class="img-wrapper" class:loaded={imageLoaded}>
      <img 
        src={movie.image} 
        alt={movie.title} 
        loading="lazy"
        on:error={handleError}
        on:load={handleLoad}
      />
    </div>
  {/if}

  {#if imageError || !movie.image}
    <div class="fallback-placeholder">
      <span class="fallback-title-text">{movie.title}</span>
    </div>
  {/if}

  <!-- Overlay de información al hacer hover -->
  <div class="hover-info">
    <span class="hover-title">{movie.title}</span>
    <div class="hover-meta">
      <span class="match">98% para ti</span>
      <span class="badge">HD</span>
    </div>
    <div class="hover-actions">
      <button class="fav-btn" class:active={isFavorite} on:click|stopPropagation={toggleFavorite} aria-label="Favorito">
        <svg viewBox="0 0 24 24" fill={isFavorite ? "currentColor" : "none"} stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
        </svg>
      </button>
    </div>
  </div>
</div>

<style>
  .movie-card {
    position: relative;
    flex: 0 0 200px;
    height: 300px;
    border-radius: 6px;
    overflow: hidden;
    cursor: pointer;
    background-color: #1a1a1a;
    transition: transform 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94),
                box-shadow 0.35s ease;
  }

  .movie-card:hover {
    transform: scale(1.08) translateY(-8px);
    z-index: 10;
    box-shadow: 0 8px 25px rgba(0,0,0,0.7), 0 0 0 1px rgba(255,255,255,0.1);
  }

  /* ── Imagen ── */
  .img-wrapper {
    width: 100%;
    height: 100%;
    opacity: 0;
    transition: opacity 0.4s ease;
  }

  .img-wrapper.loaded {
    opacity: 1;
  }

  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }

  /* ── Fallback ── */
  .fallback-placeholder {
    width: 100%;
    height: 100%;
    background: linear-gradient(145deg, #2a2a2a 0%, #1a1a1a 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 16px;
    box-sizing: border-box;
  }

  .fallback-title-text {
    color: #aaa;
    font-size: 0.85rem;
    font-weight: 600;
    line-height: 1.3;
  }

  /* ── Hover Info Overlay ── */
  .hover-info {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 16px 12px 12px;
    background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.6) 60%, transparent 100%);
    opacity: 0;
    transform: translateY(8px);
    transition: opacity 0.3s ease, transform 0.3s ease;
    pointer-events: none;
  }

  .movie-card:hover .hover-info {
    opacity: 1;
    transform: translateY(0);
    pointer-events: auto;
  }

  .hover-title {
    display: block;
    font-size: 0.85rem;
    font-weight: 700;
    color: #fff;
    margin-bottom: 6px;
    text-shadow: 0 1px 3px rgba(0,0,0,0.5);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .hover-meta {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .match {
    color: #46d369;
    font-size: 0.72rem;
    font-weight: 700;
  }

  .badge {
    border: 1px solid rgba(255,255,255,0.4);
    padding: 1px 5px;
    font-size: 0.6rem;
    color: rgba(255,255,255,0.7);
    border-radius: 3px;
    font-weight: 600;
  }

  .hover-actions {
    margin-top: 8px;
    display: flex;
    justify-content: flex-end;
  }

  .fav-btn {
    background: transparent;
    border: none;
    color: white;
    cursor: pointer;
    padding: 0;
    width: 24px;
    height: 24px;
    transition: color 0.2s, transform 0.2s;
  }
  
  .fav-btn:hover {
    transform: scale(1.15);
  }
  
  .fav-btn.active {
    color: #e50914;
    stroke: #e50914;
  }

  /* ── Responsive ── */
  @media (max-width: 1200px) {
    .movie-card { flex: 0 0 170px; height: 255px; }
  }

  @media (max-width: 800px) {
    .movie-card { flex: 0 0 140px; height: 210px; }
  }

  @media (max-width: 500px) {
    .movie-card { flex: 0 0 120px; height: 180px; }
  }
</style>
