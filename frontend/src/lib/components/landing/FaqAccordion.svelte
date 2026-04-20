<script>
  const faqs = [
    { q: "¿Qué es Netflix?", a: "Netflix es un servicio de streaming que ofrece una gran variedad de películas, series y documentales premiados en casi cualquier pantalla conectada a internet.\\n\\nTodo lo que quieras ver, sin límites ni comerciales, a un costo muy accesible. Siempre hay algo nuevo por descubrir, ¡y todas las semanas se agregan más películas y series!" },
    { q: "¿Cuánto cuesta Netflix?", a: "Disfruta Netflix en tu smartphone, tablet, smart TV, laptop o dispositivo de streaming, todo por una tarifa plana mensual. Planes desde $ 18.900 hasta $ 38.900 al mes. Sin costos adicionales ni contratos." },
    { q: "¿Dónde puedo ver Netflix?", a: "Disfruta donde quieras, cuando quieras. Inicia sesión en tu cuenta de Netflix para ver contenido al instante a través de netflix.com desde tu computadora personal o en cualquier dispositivo con conexión a internet que cuente con la app de Netflix, como smart TV, smartphones, tablets, reproductores multimedia y consolas de juegos." },
    { q: "¿Cómo cancelo?", a: "Netflix es flexible. Sin contratos molestos ni compromisos. Cancela la membresía online con solo dos clics. No hay cargos por cancelación. Empieza y termina cuando quieras." },
    { q: "¿Qué puedo ver en Netflix?", a: "Netflix tiene un amplio catálogo de películas, documentales, series, anime, originales de Netflix premiados y mucho más. Todo lo que quieras ver, cuando quieras." }
  ];

  let openIndex = null;

  function toggle(index) {
    if (openIndex === index) {
      openIndex = null;
    } else {
      openIndex = index;
    }
  }
</script>

<div class="faq-section">
  <h2 class="title">Preguntas frecuentes</h2>
  <div class="accordion">
    {#each faqs as faq, i}
      <div class="accordion-item">
        <button class="accordion-button" on:click={() => toggle(i)}>
          <span>{faq.q}</span>
          <span class="icon">{openIndex === i ? '✕' : '+'}</span>
        </button>
        {#if openIndex === i}
          <div class="accordion-content">
            <p>{faq.a}</p>
          </div>
        {/if}
      </div>
    {/each}
  </div>
</div>

<style>
  .faq-section {
    padding: 60px 4%;
  }

  .title {
    font-size: 24px;
    font-weight: 500;
    margin-bottom: 24px;
    text-align: left;
    color: white;
  }

  .accordion {
    display: flex;
    flex-direction: column;
    gap: 8px;
    max-width: 100%;
  }

  .accordion-item {
    background-color: #2d2d2d;
    transition: background-color 0.2s;
  }
  
  .accordion-item:hover {
    background-color: #414141;
  }

  .accordion-button {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 24px;
    background: transparent;
    border: none;
    color: white;
    font-size: 24px;
    font-weight: 400;
    cursor: pointer;
    text-align: left;
  }

  .icon {
    font-size: 36px;
    font-weight: 300;
    line-height: 1;
  }

  .accordion-content {
    padding: 24px;
    border-top: 1px solid black;
    font-size: 24px;
    line-height: 1.5;
    background-color: #2d2d2d;
    white-space: pre-wrap; /* Para respetar los saltos de linea definidos con \n */
  }

  @media (max-width: 600px) {
    .accordion-button { font-size: 18px; padding: 16px; }
    .accordion-content { font-size: 18px; padding: 16px; }
    .icon { font-size: 24px; }
  }
</style>
