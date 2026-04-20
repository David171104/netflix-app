<script>
  // Pósters reales de películas populares vía TMDB (URLs públicas y estables)
  const trendingMovies = [
    { id: 1, titulo: "Stranger Things", img: "https://image.tmdb.org/t/p/w500/49WJfeN0moxb9IPfGn8AIqMGskD.jpg" },
    { id: 2, titulo: "The Witcher",     img: "https://image.tmdb.org/t/p/w500/7vjaCdMw15FEbXyLQTVa04URsPm.jpg" },
    { id: 3, titulo: "Wednesday",       img: "https://image.tmdb.org/t/p/w500/9PFonBhy4cQy7Jz20NpMygczOkv.jpg" },
    { id: 4, titulo: "Squid Game",      img: "https://image.tmdb.org/t/p/w500/dDlEmu3EZ0Pgg93K2SVNLCjCSvE.jpg" },
    { id: 5, titulo: "Ozark",           img: "https://image.tmdb.org/t/p/w500/m73bD8hkQdFVTFb8WkBk9MyBniX.jpg" },
    { id: 6, titulo: "Dark",            img: "https://image.tmdb.org/t/p/w500/apbrbWs8M9lyOpJYU5WXrpFbk1Z.jpg" },
    { id: 7, titulo: "Money Heist",     img: "https://image.tmdb.org/t/p/w500/reEMJA1uzscCbkpeRJeTT2bjqUp.jpg" },
    { id: 8, titulo: "Narcos",          img: "https://image.tmdb.org/t/p/w500/rTmal9fDbwh5F0waol2hq35U4ah.jpg" },
    { id: 9, titulo: "Black Mirror",    img: "https://image.tmdb.org/t/p/w500/7PRddO7z7mcPi21nZTCMGShAyy1.jpg" },
    { id: 10, titulo: "Bridgerton",     img: "https://image.tmdb.org/t/p/w500/luoKpgVwi1E5nQsi7W0UuKHu2Rq.jpg" }
  ];
</script>

<div class="trending-section">
  <h2 class="title">Tendencias</h2>
  <div class="carousel-container">
    <div class="carousel">
      {#each trendingMovies as movie, i}
        <div class="ranking-card">
          <!-- El número gigante en stroke -->
          <div class="rank-number">{i + 1}</div>
          <img class="poster" src={movie.img} alt={`Tendencia ${i + 1}`} loading="lazy" />
          <img class="original-n" src="/n-logo.svg" alt="N" />
        </div>
      {/each}
    </div>
  </div>
</div>

<style>
  .trending-section {
    padding: 60px 4% 30px;
  }

  .title {
    font-size: 24px;
    font-weight: 500;
    margin-bottom: 20px;
    color: white;
  }

  .carousel-container {
    position: relative;
    width: 100%;
  }

  .carousel {
    display: flex;
    overflow-x: auto;
    overflow-y: hidden;
    gap: 40px; /* Espacio para que el número sobresalga */
    padding: 20px 0 20px 40px; /* Padding izquierdo para que el #1 no se corte */
    scrollbar-width: none; /* Firefox */
  }

  .carousel::-webkit-scrollbar {
    display: none; /* Chrome/Safari */
  }

  .ranking-card {
    position: relative;
    flex: 0 0 160px; /* Tamaño del póster */
    height: 225px;
    border-radius: 4px;
    transition: transform 0.3s;
    cursor: pointer;
  }

  .ranking-card:hover {
    transform: scale(1.05); /* Escala original como el requerimiento de landing */
    z-index: 2;
  }

  .poster {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 6px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.6);
  }

  .original-n {
    position: absolute;
    top: 6px;
    left: 8px;
    width: 18px;
    height: auto;
    z-index: 10;
    filter: drop-shadow(0px 2px 3px rgba(0,0,0,0.8));
  }

  .rank-number {
    position: absolute;
    left: -40px;
    bottom: -22px; /* Tocando la base de la tarjeta */
    font-size: 160px;
    font-weight: 900;
    line-height: 1;
    color: #000; /* Interior negro como en la vida real */
    -webkit-text-stroke: 4px #595959; /* Contorno difuso inicialmente */
    letter-spacing: -6px;
    transition: -webkit-text-stroke 0.3s;
    z-index: -1;
  }

  .ranking-card:hover .rank-number {
    -webkit-text-stroke: 4px #ffffff; /* Borde ultra nítido blanco en el hover */
  }

  @media (min-width: 768px) {
    .ranking-card {
      flex: 0 0 190px;
      height: 280px;
    }
    .rank-number {
      font-size: 210px;
      left: -55px;
      bottom: -32px;
      -webkit-text-stroke: 4px #595959;
    }
    .carousel {
      gap: 60px;
      padding-left: 60px;
    }
  }
</style>
