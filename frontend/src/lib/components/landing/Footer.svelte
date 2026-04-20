<script>
  import EmailInput from './EmailInput.svelte';
</script>

<div class="footer-section">
  <div class="footer-resubscribe">
    <EmailInput />
  </div>

  <footer class="footer-links-container">
    <p class="questions">¿Preguntas? Llama al <a href="#tel">01 800 519 1570</a></p>
    
    <ul class="links-grid">
      <li><a href="#faq">Preguntas frecuentes</a></li>
      <li><a href="#help">Centro de ayuda</a></li>
      <li><a href="#account">Cuenta</a></li>
      <li><a href="#media">Prensa</a></li>
      <li><a href="#investors">Relaciones con inversionistas</a></li>
      <li><a href="#jobs">Empleo</a></li>
      <li><a href="#gift">Canjear tarjetas de regalo</a></li>
      <li><a href="#buygift">Comprar tarjetas de regalo</a></li>
      <li><a href="#ways">Formas de ver</a></li>
      <li><a href="#terms">Términos de uso</a></li>
      <li><a href="#privacy">Privacidad</a></li>
      <li><a href="#cookies">Preferencias de cookies</a></li>
      <li><a href="#corp">Información corporativa</a></li>
      <li><a href="#contact">Contáctanos</a></li>
      <li><a href="#speed">Prueba de velocidad</a></li>
      <li><a href="#legal">Avisos legales</a></li>
      <li><a href="#originals">Solo en Netflix</a></li>
    </ul>
    
    <div class="lang-selector">
      <span>🌐</span>
      <select>
        <option>Español</option>
        <option>English</option>
      </select>
    </div>

    <p class="netflix-location">Netflix Colombia</p>
  </footer>
</div>

<style>
  .footer-section {
    padding: 20px 4% 60px;
  }

  .footer-resubscribe {
    margin-bottom: 60px;
  }

  .footer-links-container {
    max-width: 1000px;
    margin: 0 auto;
    color: #b3b3b3;
    font-size: 14px;
  }

  .questions {
    margin-bottom: 30px;
  }

  .questions a {
    color: #b3b3b3;
  }

  .links-grid {
    display: grid;
    grid-template-columns: repeat(1, 1fr);
    gap: 16px;
    list-style: none;
    padding: 0;
    margin: 0 0 30px;
  }

  .links-grid a {
    color: #b3b3b3;
    text-decoration: underline;
  }

  .lang-selector {
    display: inline-flex;
    align-items: center;
    border: 1px solid rgba(255, 255, 255, 0.4);
    background: rgba(0,0,0,0.6);
    border-radius: 4px;
    padding: 0 10px;
    color: white;
    margin-bottom: 24px;
  }

  .lang-selector select {
    background: transparent;
    color: white;
    border: none;
    outline: none;
    padding: 8px;
    font-size: 14px;
  }

  .lang-selector select option {
    background: #333;
  }

  .netflix-location {
    font-size: 14px;
    margin: 0;
  }

  @media (min-width: 600px) {
    .links-grid { grid-template-columns: repeat(2, 1fr); }
  }

  @media (min-width: 900px) {
    .links-grid { grid-template-columns: repeat(4, 1fr); }
  }
</style>
