<script>
  import Navbar from '$lib/components/Navbar.svelte';
  import HeroBanner from '$lib/components/HeroBanner.svelte';
  import Row from '$lib/components/Row.svelte';
  import MovieModal from '$lib/components/MovieModal.svelte';

  import { onMount } from 'svelte';
  import { getPeliculas, getFavoritos } from '$lib/api.js';

  // Reactividad: Las filas inician vacías y se llenan en caliente
  /** @type {Array<{id: number, title: string, image: string, description?: string, cast?: string}>} */
  let peliculasList = [];
  let miLista = [];
  let favoritosIds = [];
  let selectedMovie = null;

  function openModal(movie) {
    selectedMovie = movie;
  }

  function closeModal() {
    selectedMovie = null;
  }

  async function loadFavorites(userId) {
    const favData = await getFavoritos(userId);
    if (favData && favData.favoritos) {
      favoritosIds = favData.favoritos.map(f => f.id);
      miLista = favData.favoritos.map(p => ({
        id: p.id,
        title: p.titulo,
        image: p.imagen,
        description: p.descripcion,
        cast: p.reparto
      }));
    }
  }

  async function handleFavToggle(e) {
    // Cuando cambia un favorito, recargamos la lista desde el backend para estar sincronizados
    const userStr = localStorage.getItem('usuario');
    if (userStr) {
      const user = JSON.parse(userStr);
      await loadFavorites(user.id);
    }
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
      
      const userStr = localStorage.getItem('usuario');
      if (userStr) {
        const user = JSON.parse(userStr);
        await loadFavorites(user.id);
      }
    } catch (e) {
      console.error("Error al obtener datos:", e);
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
    <div id="milista" style="scroll-margin-top: 80px;"></div>
    {#if miLista.length > 0}
      <Row title="Mi Lista" movies={miLista} {favoritosIds} on:selectMovie={(e) => openModal(e.detail)} on:favToggled={handleFavToggle} />
    {/if}
    <Row title="Tendencias de hoy" movies={peliculasList} {favoritosIds} on:selectMovie={(e) => openModal(e.detail)} on:favToggled={handleFavToggle} />
    <Row title="Series Top Mundiales" movies={[...peliculasList].reverse()} {favoritosIds} on:selectMovie={(e) => openModal(e.detail)} on:favToggled={handleFavToggle} />
    <Row title="Películas Aclamadas" movies={peliculasList} {favoritosIds} on:selectMovie={(e) => openModal(e.detail)} on:favToggled={handleFavToggle} />
    <Row title="Sci-Fi para el Fin de Semana" movies={[...peliculasList].reverse()} {favoritosIds} on:selectMovie={(e) => openModal(e.detail)} on:favToggled={handleFavToggle} />
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

  html {
    scroll-behavior: smooth;
  }
</style>
