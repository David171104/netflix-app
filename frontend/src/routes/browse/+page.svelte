<script>
  import Navbar from '$lib/components/Navbar.svelte';
  import HeroBanner from '$lib/components/HeroBanner.svelte';
  import Row from '$lib/components/Row.svelte';
  import MovieModal from '$lib/components/MovieModal.svelte';

  import { onMount } from 'svelte';
  import { getPeliculas } from '$lib/api.js';

  // Reactividad: Las filas inician vacías y se llenan en caliente
  /** @type {Array<{id: number, title: string, image: string, description?: string, cast?: string}>} */
  let peliculasList = [];
  let selectedMovie = null;

  function openModal(movie) {
    selectedMovie = movie;
  }

  function closeModal() {
    selectedMovie = null;
  }

  onMount(async () => {
    try {
      const data = await getPeliculas();
      // Mapear claves del Backend (MySQL) -> hacia el Frontend (Componente Row)
      peliculasList = (data.peliculas || []).map(
        /** @param {{id: number, titulo: string, imagen: string, descripcion: string, reparto: string}} p */
        (p) => ({
          id: p.id,
          title: p.titulo,
          image: p.imagen,
          description: p.descripcion,
          cast: p.reparto
        })
      );
    } catch (e) {
      console.error("Error al obtener películas:", e);
    }
  });

  // Datos para el Hero destacado
  const heroData = {
    title: "Oppenheimer",
    description: "La historia del brillante físico J. Robert Oppenheimer y su papel en el desarrollo de la bomba atómica durante la Segunda Guerra Mundial, enfrentando dilemas morales sobre el impacto de su descubrimiento en el futuro de la humanidad.",
    backgroundUrl: "https://image.tmdb.org/t/p/original/rktDFPbfHfUbArZ6OOOKsXcv0Bm.jpg"
  };
</script>

<svelte:head>
  <title>NetflixApp - Inicio</title>
</svelte:head>

<main class="browse-layout">
  <Navbar />
  
  <HeroBanner 
    title={heroData.title} 
    description={heroData.description} 
    backgroundUrl={heroData.backgroundUrl} 
  />

  <div class="rows-section">
    <Row title="Tendencias de hoy" movies={peliculasList} on:selectMovie={(e) => openModal(e.detail)} />
    <Row title="Series Top Mundiales" movies={[...peliculasList].reverse()} on:selectMovie={(e) => openModal(e.detail)} />
    <Row title="Películas Aclamadas" movies={peliculasList} on:selectMovie={(e) => openModal(e.detail)} />
    <Row title="Sci-Fi para el Fin de Semana" movies={[...peliculasList].reverse()} on:selectMovie={(e) => openModal(e.detail)} />
  </div>

  {#if selectedMovie}
    <MovieModal movie={selectedMovie} on:close={closeModal} />
  {/if}
</main>

<style>
  :global(body) {
    margin: 0;
    padding: 0;
    background-color: #141414; /* Fondo oficial de Netflix */
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    color: white;
    /* Ocultar desbordamiento horizontal extra por el scale del Hover */
    overflow-x: hidden; 
  }

  .browse-layout {
    min-height: 100vh;
  }

  .rows-section {
    /* Mueve la primera fila un poco hacia arriba encima del fade del Hero */
    margin-top: -5rem; 
    position: relative;
    z-index: 10;
    padding-bottom: 2rem;
  }
</style>
