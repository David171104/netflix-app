<script>
  // Pósters locales (servidos desde /static/assets/movies/)
  const trendingMovies = [
    { id: 1,  titulo: "Stranger Things", img: "/assets/movies/49WJfeN0moxb9IPfGn8AIqMGskD.jpg" },
    { id: 2,  titulo: "The Witcher",     img: "/assets/movies/7vjaCdMw15FEbXyLQTVa04URsPm.jpg" },
    { id: 3,  titulo: "Wednesday",       img: "/assets/movies/9PFonBhy4cQy7Jz20NpMygczOkv.jpg" },
    { id: 4,  titulo: "Squid Game",      img: "/assets/movies/dDlEmu3EZ0Pgg93K2SVNLCjCSvE.jpg" },
    { id: 5,  titulo: "Ozark",           img: "/assets/movies/ozark.svg" },
    { id: 6,  titulo: "Dark",            img: "/assets/movies/apbrbWs8M9lyOpJYU5WXrpFbk1Z.jpg" },
    { id: 7,  titulo: "Money Heist",     img: "/assets/movies/reEMJA1uzscCbkpeRJeTT2bjqUp.jpg" },
    { id: 8,  titulo: "Narcos",          img: "/assets/movies/rTmal9fDbwh5F0waol2hq35U4ah.jpg" },
    { id: 9,  titulo: "Black Mirror",    img: "/assets/movies/7PRddO7z7mcPi21nZTCMGShAyy1.jpg" },
    { id: 10, titulo: "Bridgerton",      img: "/assets/movies/luoKpgVwi1E5nQsi7W0UuKHu2Rq.jpg" },
  ];

  /** @type {HTMLElement|null} */
  let carouselEl = null;
  let showLeft  = false;
  let showRight = true;

  function scrollLeft() {
    carouselEl?.scrollBy({ left: -(carouselEl.clientWidth * 0.7), behavior: 'smooth' });
  }
  function scrollRight() {
    carouselEl?.scrollBy({ left: carouselEl.clientWidth * 0.7, behavior: 'smooth' });
  }
  function onScroll() {
    if (!carouselEl) return;
    showLeft  = carouselEl.scrollLeft > 20;
    showRight = carouselEl.scrollLeft < carouselEl.scrollWidth - carouselEl.clientWidth - 20;
  }

  /** @type {Record<number,boolean>} */
  let loaded = {};
  /** @type {Record<number,boolean>} */
  let errored = {};

  /** @param {number} id */
  function markLoaded(id)  { loaded  = { ...loaded,  [id]: true }; }
  /** @param {number} id */
  function markError(id)   { errored = { ...errored, [id]: true }; }
</script>

<section class="trending-section">
  <h2 class="title">Tendencias</h2>

  <div class="slider-wrapper">
    <!-- Flecha izquierda -->
    {#if showLeft}
      <!-- svelte-ignore a11y-click-events-have-key-events a11y-no-static-element-interactions -->
      <div class="arrow arrow-left" on:click={scrollLeft}>
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/></svg>
      </div>
    {/if}

    <!-- Flecha derecha -->
    {#if showRight}
      <!-- svelte-ignore a11y-click-events-have-key-events a11y-no-static-element-interactions -->
      <div class="arrow arrow-right" on:click={scrollRight}>
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
      </div>
    {/if}

    <div class="carousel" bind:this={carouselEl} on:scroll={onScroll}>
      {#each trendingMovies as movie, i (movie.id)}
        <div class="ranking-card">
          <!-- Número de ranking -->
          <div class="rank-number">{i + 1}</div>

          <!-- Póster -->
          <div class="poster-wrap" class:is-loaded={loaded[movie.id]} class:is-error={errored[movie.id]}>
            {#if !errored[movie.id]}
              <img
                class="poster"
                src={movie.img}
                alt={movie.titulo}
                loading="lazy"
                on:load={() => markLoaded(movie.id)}
                on:error={() => markError(movie.id)}
              />
            {:else}
              <div class="fallback">
                <span>{movie.titulo}</span>
              </div>
            {/if}

            <!-- Badge "N" de Netflix -->
            <img class="n-badge" src="/n-logo.svg" alt="N" />

            <!-- Overlay con título en hover -->
            <div class="hover-overlay">
              <span class="hover-title">{movie.titulo}</span>
            </div>
          </div>
        </div>
      {/each}
    </div>
  </div>
</section>

<style>
  /* ── Sección ── */
  .trending-section {
    padding: 60px 0 40px;
    background: #000;
  }

  .title {
    font-size: 1.5rem;
    font-weight: 700;
    margin: 0 0 20px 4%;
    color: #e5e5e5;
    letter-spacing: 0.5px;
  }

  /* ── Slider wrapper (posición para las flechas) ── */
  .slider-wrapper {
    position: relative;
  }

  /* ── Flechas ── */
  .arrow {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 60px;
    z-index: 20;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    opacity: 0;
    transition: opacity 0.3s ease;
  }

  .slider-wrapper:hover .arrow {
    opacity: 1;
  }

  .arrow-left {
    left: 0;
    background: linear-gradient(to right, rgba(0,0,0,0.9) 0%, transparent 100%);
  }

  .arrow-right {
    right: 0;
    background: linear-gradient(to left, rgba(0,0,0,0.9) 0%, transparent 100%);
  }

  .arrow svg {
    width: 44px;
    height: 44px;
    color: #fff;
    filter: drop-shadow(0 0 4px rgba(0,0,0,0.6));
    transition: transform 0.2s ease;
  }

  .arrow:hover svg {
    transform: scale(1.25);
  }

  /* ── Carrusel ── */
  .carousel {
    display: flex;
    overflow-x: auto;
    overflow-y: hidden;
    gap: 0;
    padding: 20px 4% 20px 60px;
    scrollbar-width: none;
    scroll-behavior: smooth;
  }

  .carousel::-webkit-scrollbar { display: none; }

  /* ── Tarjeta con número ── */
  .ranking-card {
    position: relative;
    flex: 0 0 auto;
    display: flex;
    align-items: flex-end;
    /* El número se superpone con la tarjeta siguiente — margen negativo intencional */
    margin-right: -8px;
    cursor: pointer;
  }

  /* ── Número gigante ── */
  .rank-number {
    position: relative;
    font-size: 170px;
    font-weight: 900;
    line-height: 1;
    color: #000;
    -webkit-text-stroke: 3px #555;
    letter-spacing: -8px;
    user-select: none;
    transition: -webkit-text-stroke 0.3s ease;
    z-index: 1;
    padding-right: 4px;
    /* Alineado al fondo del póster */
    align-self: flex-end;
    margin-bottom: -10px;
  }

  .ranking-card:hover .rank-number {
    -webkit-text-stroke: 3px #fff;
  }

  /* ── Poster wrap ── */
  .poster-wrap {
    position: relative;
    width: 160px;
    height: 240px;
    border-radius: 6px;
    overflow: hidden;
    background: #1a1a1a;
    flex-shrink: 0;
    z-index: 2;
    box-shadow: 4px 0 16px rgba(0,0,0,0.6);
    /* Imagen empieza invisible y aparece al cargar */
    transition: transform 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94),
                box-shadow 0.35s ease;
  }

  .ranking-card:hover .poster-wrap {
    transform: scale(1.07) translateY(-6px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.8), 0 0 0 1px rgba(255,255,255,0.08);
  }

  .poster {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    opacity: 0;
    transition: opacity 0.4s ease;
  }

  .poster-wrap.is-loaded .poster {
    opacity: 1;
  }

  /* ── Fallback si imagen falla ── */
  .fallback {
    width: 100%;
    height: 100%;
    background: linear-gradient(145deg, #2a2a2a 0%, #111 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 12px;
    text-align: center;
  }

  .fallback span {
    color: #888;
    font-size: 0.8rem;
    font-weight: 600;
    line-height: 1.3;
  }

  /* ── Badge "N" ── */
  .n-badge {
    position: absolute;
    top: 7px;
    left: 9px;
    width: 18px;
    height: auto;
    z-index: 10;
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.9));
  }

  /* ── Hover overlay ── */
  .hover-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 30px 10px 10px;
    background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, transparent 100%);
    opacity: 0;
    transform: translateY(6px);
    transition: opacity 0.3s ease, transform 0.3s ease;
    pointer-events: none;
  }

  .ranking-card:hover .hover-overlay {
    opacity: 1;
    transform: translateY(0);
  }

  .hover-title {
    display: block;
    color: #fff;
    font-size: 0.8rem;
    font-weight: 700;
    text-shadow: 0 1px 3px rgba(0,0,0,0.7);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  /* ── Responsive ── */
  @media (min-width: 768px) {
    .poster-wrap {
      width: 190px;
      height: 285px;
    }
    .rank-number {
      font-size: 210px;
      letter-spacing: -10px;
    }
    .carousel {
      padding-left: 70px;
    }
  }

  @media (max-width: 500px) {
    .poster-wrap {
      width: 130px;
      height: 195px;
    }
    .rank-number {
      font-size: 130px;
      letter-spacing: -6px;
    }
    .carousel {
      padding-left: 45px;
    }
  }
</style>
