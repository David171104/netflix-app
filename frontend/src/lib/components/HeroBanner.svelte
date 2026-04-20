<script>
  export let title = "Título de la Película";
  export let description = "Descripción breve sobre la trama de la serie o película destacada. Esto ocupará unas líneas y estará bajo el título.";
  export let backgroundUrl = "https://image.tmdb.org/t/p/original/9gk7adZA2sUH1XfOEdpIeIe4z7c.jpg";
</script>

<header 
  class="hero-banner" 
  style="background-image: url('{backgroundUrl}');"
>
  <div class="hero-content">
    <h1 class="hero-title">{title}</h1>
    <p class="hero-description">{description}</p>
    
    <div class="hero-buttons">
      <button class="btn play-btn">
        <svg viewBox="0 0 24 24" fill="currentColor" class="btn-icon"><path d="M5 3v18l15-9L5 3z"/></svg>
        Reproducir
      </button>
      <button class="btn info-btn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="btn-icon"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
        Más información
      </button>
    </div>
  </div>
  
  <div class="hero-fade-bottom"></div>
</header>

<style>
  .hero-banner {
    position: relative;
    height: 80vh;
    background-size: cover;
    background-position: center top;
    color: white;
    object-fit: contain;
  }

  .hero-content {
    position: absolute;
    top: 35%;
    left: 4%;
    width: 90%;
    max-width: 600px;
    z-index: 2;
  }

  .hero-title {
    font-size: 3.5rem;
    font-weight: 800;
    margin-bottom: 0.5rem;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.45);
    line-height: 1.1;
  }

  .hero-description {
    font-size: 1.2rem;
    font-weight: 400;
    line-height: 1.4;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.45);
    margin-bottom: 1.5rem;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .hero-buttons {
    display: flex;
    gap: 1rem;
  }

  .btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    border: none;
    border-radius: 4px;
    padding: 0.5rem 1.5rem;
    font-size: 1.2rem;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.2s;
  }

  .btn-icon {
    width: 24px;
    height: 24px;
  }

  .play-btn {
    background-color: white;
    color: black;
  }

  .play-btn:hover {
    background-color: rgba(255, 255, 255, 0.75);
  }

  .info-btn {
    background-color: rgba(109, 109, 110, 0.7);
    color: white;
  }

  .info-btn:hover {
    background-color: rgba(109, 109, 110, 0.4);
  }

  .hero-fade-bottom {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 7.4rem;
    background-image: linear-gradient(
      180deg,
      transparent,
      rgba(37, 37, 37, 0.61),
      #141414
    );
    z-index: 1;
  }

  @media (max-width: 800px) {
    .hero-title {
      font-size: 2.5rem;
    }
    .hero-description {
      font-size: 1rem;
    }
  }
</style>
