<script>
  import { createEventDispatcher } from 'svelte';
  import MovieCard from './MovieCard.svelte';
  export let title = "Categoría";
  /** @type {Array<{id: number, title: string, image: string}>} */
  export let movies = [];
  export let favoritosIds = [];

  const dispatch = createEventDispatcher();

  let sliderRef;
  let showLeftArrow = false;
  let showRightArrow = true;

  function scrollLeft() {
    if (!sliderRef) return;
    sliderRef.scrollBy({ left: -(sliderRef.clientWidth * 0.75), behavior: 'smooth' });
  }

  function scrollRight() {
    if (!sliderRef) return;
    sliderRef.scrollBy({ left: sliderRef.clientWidth * 0.75, behavior: 'smooth' });
  }

  function handleScroll() {
    if (!sliderRef) return;
    showLeftArrow = sliderRef.scrollLeft > 20;
    showRightArrow = sliderRef.scrollLeft < sliderRef.scrollWidth - sliderRef.clientWidth - 20;
  }
</script>

<div class="row-container">
  <h2 class="row-title">{title}</h2>
  
  <div class="slider-wrapper">
    <!-- Flecha izquierda -->
    {#if showLeftArrow}
      <!-- svelte-ignore a11y-click-events-have-key-events a11y-no-static-element-interactions -->
      <div class="slider-arrow left" on:click={scrollLeft}>
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/></svg>
      </div>
    {/if}

    <!-- Flecha derecha -->
    {#if showRightArrow}
      <!-- svelte-ignore a11y-click-events-have-key-events a11y-no-static-element-interactions -->
      <div class="slider-arrow right" on:click={scrollRight}>
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
      </div>
    {/if}

    <div class="row-posters" bind:this={sliderRef} on:scroll={handleScroll}>
      {#each movies as movie (movie.id)}
        <MovieCard {movie} isFavorite={favoritosIds.includes(movie.id)} on:click={() => dispatch('selectMovie', movie)} on:favToggled />
      {/each}
    </div>
  </div>
</div>

<style>
  .row-container {
    margin-top: 10px;
    margin-bottom: 40px;
    color: white;
    padding-left: 4%;
  }

  .row-title {
    font-size: 1.4vw;
    font-weight: bold;
    margin-bottom: 0.8rem;
    color: #e5e5e5;
    text-transform: capitalize;
  }

  .slider-wrapper {
    position: relative;
  }

  /* ── Flechas de navegación ── */
  .slider-arrow {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 55px;
    z-index: 20;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    opacity: 0;
    transition: opacity 0.3s ease, background 0.3s ease;
  }

  .slider-wrapper:hover .slider-arrow {
    opacity: 1;
  }

  .slider-arrow.left {
    left: 0;
    background: linear-gradient(to right, rgba(20,20,20,0.85), transparent);
    border-radius: 0 4px 4px 0;
  }

  .slider-arrow.right {
    right: 0;
    background: linear-gradient(to left, rgba(20,20,20,0.85), transparent);
    border-radius: 4px 0 0 4px;
  }

  .slider-arrow svg {
    width: 40px;
    height: 40px;
    color: white;
    filter: drop-shadow(0 0 2px rgba(0,0,0,0.5));
    transition: transform 0.2s;
  }

  .slider-arrow:hover svg {
    transform: scale(1.25);
  }

  /* ── Contenedor de tarjetas ── */
  .row-posters {
    display: flex;
    overflow-y: hidden;
    overflow-x: auto;
    gap: 6px;
    padding: 20px 0;
    padding-right: 4%;
    scroll-behavior: smooth;

    /* Ocultar barra scroll */
    -ms-overflow-style: none;
    scrollbar-width: none;
  }

  .row-posters::-webkit-scrollbar {
    display: none;
  }

  @media (max-width: 800px) {
    .row-title {
      font-size: 1.2rem;
    }
    .slider-arrow {
      width: 35px;
    }
    .slider-arrow svg {
      width: 28px;
      height: 28px;
    }
  }
</style>
