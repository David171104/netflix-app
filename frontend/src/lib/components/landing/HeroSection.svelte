<script>
  import EmailInput from './EmailInput.svelte';
</script>

<div class="hero-container">
  <!-- Fondo y Overlay (radial gradient) -->
  <div class="bg-image"></div>
  <div class="bg-gradient"></div>

  <!-- Header Transparente -->
  <header class="header">
    <img src="/logo.png" alt="Netflix Logo" class="logo" />
    <div class="nav-right">
      <div class="lang-selector">
        <span>🌐</span>
        <select>
          <option>Español</option>
          <option>English</option>
        </select>
      </div>
      <a href="/login" class="btn-login">Iniciar sesión</a>
    </div>
  </header>

  <!-- Contenido Central -->
  <div class="hero-content">
    <h1>Películas y series ilimitadas y mucho más</h1>
    <h2>A partir de $ 18.900. Cancela cuando quieras.</h2>
    <div class="email-form-wrapper">
      <EmailInput />
    </div>
    <p class="alt-register">
      ¿Prefieres ir directo?
      <a href="/signup" class="link-registro">Crea tu cuenta ahora</a>
    </p>
  </div>
</div>

<style>
  .hero-container {
    position: relative;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    border-bottom: 8px solid #232323;
  }

  .bg-image {
    position: absolute;
    inset: 0;
    /* Placeholder background parecido al de Netflix */
    background-image: url('/landing-bg.png');
    background-size: cover;
    background-position: center;
    opacity: 0.85; /* Ajuste suave para fusionar con el gradiente de texto */
    z-index: 1;
  }

  .bg-gradient {
    position: absolute;
    inset: 0;
    /* Gradiente hiper-realista para la entrada */
    background: radial-gradient(ellipse at center, rgba(0,0,0,0.4) 0%, rgba(0,0,0,0.85) 60%, rgba(0,0,0,1) 100%);
    box-shadow: inset 0px -150px 150px -50px #000;
    z-index: 2;
  }

  .header {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    padding: 24px 5%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 10;
  }

  .logo {
    width: 150px;
    height: auto;
  }

  .nav-right {
    display: flex;
    gap: 24px;
    align-items: center;
  }

  .lang-selector {
    border: 1px solid rgba(255, 255, 255, 0.4);
    background: rgba(0,0,0,0.6);
    border-radius: 4px;
    display: flex;
    align-items: center;
    padding: 0 10px;
    color: white;
  }

  .lang-selector select {
    background: transparent;
    color: white;
    border: none;
    outline: none;
    padding: 8px;
    font-size: 16px;
    font-weight: 500;
  }

  .lang-selector select option {
    background: #333;
  }

  .btn-login {
    background-color: #E50914;
    color: white;
    text-decoration: none;
    font-weight: 500;
    font-size: 14px;
    padding: 8px 16px;
    border-radius: 4px;
    transition: background-color 0.2s;
  }

  .btn-login:hover {
    background-color: #C11119;
  }

  .hero-content {
    position: relative;
    z-index: 10;
    text-align: center;
    padding: 0 5%;
    max-width: 1200px;
    margin: auto;
  }

  h1 {
    font-size: 3rem;
    font-weight: 900;
    margin-bottom: 16px;
  }

  h2 {
    font-size: 1.5rem;
    font-weight: 400;
    margin-bottom: 30px;
  }

  .email-form-wrapper {
    margin-top: 30px;
  }

  .alt-register {
    margin-top: 18px;
    font-size: 15px;
    color: rgba(255,255,255,0.65);
    text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
  }
  .link-registro {
    color: #fff;
    font-weight: 700;
    text-decoration: underline;
    text-underline-offset: 3px;
    transition: color .2s;
  }
  .link-registro:hover { color: #E50914; }

  @media (max-width: 960px) {
    h1 { font-size: 3rem; }
    h2 { font-size: 1.25rem; }
  }

  @media (max-width: 600px) {
    .logo { width: 89px; height: 24px; }
    h1 { font-size: 2rem; }
  }
</style>
