<script>
  const features = [
    {
      title: "Disfruta en tu TV",
      desc: "Ve en smart TV, PlayStation, Xbox, Chromecast, Apple TV, reproductores de Blu-ray y más.",
      icon: "📺"
    },
    {
      title: "Descarga tus series para verlas offline",
      desc: "Guarda tu contenido favorito y siempre tendrás algo para ver.",
      icon: "💾"
    },
    {
      title: "Disfruta donde quieras",
      desc: "Películas y series ilimitadas en tu teléfono, tablet, laptop y TV.",
      icon: "🔭"
    },
    {
      title: "Crea perfiles para niños",
      desc: "Los niños vivirán aventuras con sus personajes favoritos en un espacio diseñado exclusivamente para ellos, gratis con tu membresía.",
      icon: "🧒"
    }
  ];
</script>

<div class="features-section">
  <h2 class="title">Más motivos para unirte</h2>
  
  <div class="features-grid">
    {#each features as feature}
      <div class="feature-card">
        <h3>{feature.title}</h3>
        <p>{feature.desc}</p>
        <div class="card-icon">{feature.icon}</div>
      </div>
    {/each}
  </div>
</div>

<style>
  .features-section {
    padding: 60px 4%;
  }

  .title {
    font-size: 24px;
    font-weight: 500;
    margin-bottom: 24px;
    color: white;
  }

  .features-grid {
    display: grid;
    grid-template-columns: repeat(1, 1fr);
    gap: 16px;
  }

  .feature-card {
    position: relative;
    background: linear-gradient(135deg, #192247 0%, #210e17 100%);
    border-radius: 16px;
    padding: 24px;
    min-height: 260px;
    display: flex;
    flex-direction: column;
  }

  .feature-card h3 {
    font-size: 24px;
    font-weight: 500;
    margin: 0 0 16px;
    color: white;
  }

  .feature-card p {
    font-size: 16px;
    color: #rgba(255, 255, 255, 0.7);
    line-height: 1.5;
    margin: 0;
  }

  .card-icon {
    position: absolute;
    bottom: 24px;
    right: 24px;
    font-size: 40px;
  }

  @media (min-width: 600px) {
    .features-grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }

  @media (min-width: 1024px) {
    .features-grid {
      grid-template-columns: repeat(4, 1fr);
    }
  }
</style>
