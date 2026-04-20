<script>
  export let movie;
</script>

<!-- svelte-ignore a11y-click-events-have-key-events a11y-no-static-element-interactions -->
<div class="movie-card" on:click>
  <img 
    src={movie.image} 
    alt={movie.title} 
    loading="lazy"
  />
  <!-- Información extra visible solo en hover podría ir aquí -->
  <div class="fallback-title">{movie.title}</div>
</div>

<style>
  .movie-card {
    position: relative;
    flex: 0 0 calc(100% / 6 - 8px); /* Mostrar 6 tarjetas por fila */
    border-radius: 4px;
    overflow: hidden;
    cursor: pointer;
    transition: transform 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94),
                z-index 0s, margin 0.3s;
    background-color: #222; /* Fallback de color */
  }

  /* Animación Hover tipo Netflix */
  .movie-card:hover {
    transform: scale(1.35) translateY(-5%);
    z-index: 10;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.8);
    position: relative;
  }

  /* Excepción: si es el primer elemento de la fila, que crezca hacia la derecha */
  .movie-card:first-child:hover {
    transform: scale(1.35) translate(15%, -5%);
  }

  /* Excepción: si es el ultimo, hacia la izquierda */
  .movie-card:last-child:hover {
    transform: scale(1.35) translate(-15%, -5%);
  }

  img {
    width: 100%;
    height: 100%;
    aspect-ratio: 16 / 9; /* Formato apaisado para pósters en fila */
    object-fit: cover;
    display: block;
    border-radius: 4px;
  }

  .fallback-title {
    position: absolute;
    bottom: 8px;
    left: 8px;
    color: white;
    font-size: 0.8rem;
    font-weight: bold;
    text-shadow: 1px 1px 3px black;
    opacity: 0;
    transition: opacity 0.2s;
  }

  /* Si la imagen falla o no tiene, mostramos título */
  img:not([src]), img[src=""] ~ .fallback-title {
    opacity: 1;
  }

  @media (max-width: 1024px) {
    .movie-card { flex: 0 0 calc(100% / 4 - 8px); }
  }

  @media (max-width: 600px) {
    .movie-card { flex: 0 0 calc(100% / 2 - 8px); }
  }
</style>
