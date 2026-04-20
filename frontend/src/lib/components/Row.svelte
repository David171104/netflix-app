<script>
  import { createEventDispatcher } from 'svelte';
  import MovieCard from './MovieCard.svelte';
  export let title = "Categoría";
  /** @type {Array<{id: number, title: string, image: string}>} */
  export let movies = [];

  const dispatch = createEventDispatcher();
</script>

<div class="row-container">
  <h2 class="row-title">{title}</h2>
  
  <div class="row-posters">
    {#each movies as movie (movie.id)}
      <MovieCard {movie} on:click={() => dispatch('selectMovie', movie)} />
    {/each}
  </div>
</div>

<style>
  .row-container {
    margin-top: 10px;
    margin-bottom: 30px;
    color: white;
    padding-left: 4%;
  }

  .row-title {
    font-size: 1.4vw;
    font-weight: bold;
    margin-bottom: 0.5rem;
    color: #e5e5e5;
    text-transform: capitalize;
  }

  .row-posters {
    display: flex;
    overflow-y: hidden;
    overflow-x: scroll;
    gap: 8px;
    padding: 10px 0; /* Padding vertical para no cortar el hover scale(1.35) */
    
    /* Ocultar barra scroll */
    -ms-overflow-style: none;  /* IE and Edge */
    scrollbar-width: none;  /* Firefox */
  }

  .row-posters::-webkit-scrollbar {
    display: none;
  }

  @media (max-width: 800px) {
    .row-title {
      font-size: 1.2rem;
    }
  }
</style>
