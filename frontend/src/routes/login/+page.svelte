<script>
  import { goto } from '$app/navigation';
  import { loginUsuario } from '$lib/api';
  import Swal from 'sweetalert2';

  let email = '';
  let password = '';
  let cargando = false;
  let error = null;
  let showPassword = false;

  async function handleLogin() {
    error = null;

    if (!email || !password) {
      error = 'Por favor ingresa tu correo y contraseña.';
      return;
    }

    cargando = true;
    
    try {
      const res = await loginUsuario({ email, contrasena: password });
      localStorage.setItem('usuario', JSON.stringify(res.usuario));
      
      await Swal.fire({
        icon: 'success',
        title: '¡Bienvenido!',
        text: 'Has iniciado sesión correctamente.',
        background: '#333',
        color: '#fff',
        confirmButtonColor: '#e50914',
        timer: 2000,
        showConfirmButton: false
      });
      goto('/browse');
    } catch (err) {
      error = err instanceof Error ? err.message : 'Error al iniciar sesión';
      Swal.fire({
        icon: 'error',
        title: 'Error de inicio de sesión',
        text: error,
        background: '#333',
        color: '#fff',
        confirmButtonColor: '#e50914'
      });
    } finally {
      cargando = false;
    }
  }
</script>

<svelte:head>
  <title>Netflix - Iniciar sesión</title>
</svelte:head>

<div class="login-page">
  <!-- ═══ Background con pósters ═══ -->
  <div class="bg-image" aria-hidden="true"></div>
  <div class="bg-overlay" aria-hidden="true"></div>

  <!-- ═══ Header con Logo SVG ═══ -->
  <header class="top-header">
    <a href="/" class="logo-link" aria-label="Netflix">
      <img src="/logo.png" alt="Netflix Logo" class="netflix-logo" />
    </a>
  </header>

  <!-- ═══ Formulario de Login ═══ -->
  <main class="login-wrapper">
    <div class="login-card">
      <h1>Iniciar sesión</h1>

      {#if error}
        <div class="error-banner" role="alert">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="error-icon">
            <path d="M8 1C4.13 1 1 4.13 1 8s3.13 7 7 7 7-3.13 7-7-3.13-7-7-7zm-.5 3h1v5h-1V4zm.5 8a.75.75 0 110-1.5.75.75 0 010 1.5z" fill="currentColor"/>
          </svg>
          <span>{error}</span>
        </div>
      {/if}

      <form on:submit|preventDefault={handleLogin}>
        <!-- Input Email -->
        <div class="form-input-wrapper" class:has-value={email !== ''}>
          <input 
            type="email" 
            id="loginEmail" 
            bind:value={email} 
            required 
            placeholder=" "
            autocomplete="email"
          />
          <label for="loginEmail">Email o número de teléfono</label>
        </div>

        <!-- Input Password -->
        <div class="form-input-wrapper" class:has-value={password !== ''}>
          <input 
            type={showPassword ? 'text' : 'password'}
            id="loginPassword" 
            bind:value={password} 
            required 
            placeholder=" "
            autocomplete="current-password"
          />
          <label for="loginPassword">Contraseña</label>
          {#if password.length > 0}
            <button 
              type="button" 
              class="toggle-password" 
              on:click={() => showPassword = !showPassword}
            >
              {showPassword ? 'OCULTAR' : 'MOSTRAR'}
            </button>
          {/if}
        </div>

        <!-- Botón Submit -->
        <button type="submit" class="login-btn" disabled={cargando}>
          {#if cargando}
            <span class="spinner"></span>
          {:else}
            Iniciar sesión
          {/if}
        </button>

        <!-- Acciones secundarias -->
        <div class="login-form-other">
          <div class="remember-me">
            <input type="checkbox" id="rememberMe" checked />
            <label for="rememberMe" class="checkbox-label">Recuérdame</label>
          </div>
          <div style="display: flex; flex-direction: column; align-items: flex-end; gap: 8px;">
            <a href="/signup" class="help-link">¿Olvidaste tu contraseña? Regístrate</a>
            <a href="#help" class="help-link">¿Necesitas ayuda?</a>
          </div>
        </div>
      </form>

      <!-- Pie de la tarjeta -->
      <div class="login-signup-now">
        <span>¿Primera vez en Netflix?</span>
        <a href="/signup">Suscríbete ahora.</a>
      </div>

      <div class="login-disclaimer">
        <p>
          Esta página está protegida por Google reCAPTCHA para asegurarnos de que no eres un robot. 
          <a href="#learn-more">Más info.</a>
        </p>
      </div>
    </div>
  </main>

  <!-- ═══ Footer  ═══ -->
  <footer class="login-footer">
    <div class="footer-content">
      <p class="footer-top-msg">¿Preguntas? Llama al 01-800-123-4567</p>
      <ul class="footer-links">
        <li><a href="#faq">Preguntas frecuentes</a></li>
        <li><a href="#help">Centro de ayuda</a></li>
        <li><a href="#terms">Términos de uso</a></li>
        <li><a href="#privacy">Privacidad</a></li>
        <li><a href="#cookies">Preferencias de cookies</a></li>
        <li><a href="#corporate">Información corporativa</a></li>
      </ul>
      <div class="footer-lang">
        <select aria-label="Seleccionar idioma">
          <option value="es">Español</option>
          <option value="en">English</option>
        </select>
      </div>
    </div>
  </footer>
</div>

<style>
  /* ═══════════════════════════════════════════════════════════════════
     RESET Y GLOBALES
     ═══════════════════════════════════════════════════════════════════ */
  :global(*, *::before, *::after) { box-sizing: border-box; }

  :global(body) {
    margin: 0;
    padding: 0;
    background-color: #000;
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    color: #fff;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  /* ═══════════════════════════════════════════════════════════════════
     LAYOUT DE PÁGINA
     ═══════════════════════════════════════════════════════════════════ */
  .login-page {
    position: relative;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }

  /* ═══════════════════════════════════════════════════════════════════
     BACKGROUND + OVERLAY
     ═══════════════════════════════════════════════════════════════════ */
  .bg-image {
    position: fixed;
    inset: 0;
    background-image: url('https://assets.nflxext.com/ffe/siteui/vlv3/a73c4363-1dcd-4e2a-b4f1-a2654d40a7b4/3de2e84c-dd20-4221-aab0-b74c3e80df05/CO-es-20231016-popsignuptwoweeks-perspective_alpha_website_large.jpg');
    background-size: cover;
    background-position: center;
    z-index: 0;
  }

  .bg-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.45);
    background-image: linear-gradient(
      to top,
      rgba(0, 0, 0, 0.85) 0%,
      rgba(0, 0, 0, 0) 50%,
      rgba(0, 0, 0, 0.85) 100%
    );
    z-index: 1;
  }

  /* ═══════════════════════════════════════════════════════════════════
     HEADER + LOGO SVG
     ═══════════════════════════════════════════════════════════════════ */
  .top-header {
    position: relative;
    z-index: 3;
    padding: 20px 3%;
    flex-shrink: 0;
  }

  .logo-link {
    display: inline-block;
  }

  .netflix-logo {
    width: 150px;
    height: auto;
  }

  /* ═══════════════════════════════════════════════════════════════════
     WRAPPER + TARJETA DE LOGIN  
     ═══════════════════════════════════════════════════════════════════ */
  .login-wrapper {
    position: relative;
    z-index: 2;
    flex: 1;
    display: flex;
    justify-content: center;
    padding: 0 5%;
  }

  .login-card {
    background-color: rgba(0, 0, 0, 0.75);
    border-radius: 4px;
    width: 100%;
    max-width: 450px;
    padding: 60px 68px 40px;
    margin-bottom: 90px;
  }

  h1 {
    font-size: 32px;
    font-weight: 700;
    margin: 0 0 28px;
    color: #fff;
  }

  /* ═══════════════════════════════════════════════════════════════════
     ERROR BANNER (Naranja Netflix)
     ═══════════════════════════════════════════════════════════════════ */
  .error-banner {
    background-color: #e87c03;
    border-radius: 4px;
    padding: 10px 20px;
    margin-bottom: 16px;
    font-size: 14px;
    color: #fff;
    display: flex;
    align-items: center;
    gap: 8px;
    line-height: 1.4;
  }

  .error-icon {
    flex-shrink: 0;
  }

  /* ═══════════════════════════════════════════════════════════════════
     FORM
     ═══════════════════════════════════════════════════════════════════ */
  form {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  /* ═══════════════════════════════════════════════════════════════════
     FLOATING LABEL INPUTS
     ═══════════════════════════════════════════════════════════════════ */
  .form-input-wrapper {
    position: relative;
  }

  .form-input-wrapper input[type="email"],
  .form-input-wrapper input[type="password"],
  .form-input-wrapper input[type="text"] {
    width: 100%;
    height: 50px;
    background: #333;
    border: none;
    border-bottom: 2px solid transparent;
    border-radius: 4px;
    color: #fff;
    font-size: 16px;
    font-family: inherit;
    padding: 16px 20px 0;
    outline: none;
    transition: background 0.2s ease, border-color 0.2s ease;
    box-sizing: border-box;
  }

  .form-input-wrapper input:focus {
    background: #454545;
    border-bottom-color: #e87c03;
  }

  /* Label flotante */
  .form-input-wrapper label {
    position: absolute;
    left: 20px;
    top: 50%;
    transform: translateY(-50%);
    color: #8c8c8c;
    font-size: 16px;
    font-weight: 400;
    pointer-events: none;
    transition: top 0.15s ease, font-size 0.15s ease, transform 0.15s ease;
  }

  /* Cuando input tiene focus O tiene texto escrito */
  .form-input-wrapper input:focus + label,
  .form-input-wrapper input:not(:placeholder-shown) + label {
    top: 7px;
    transform: translateY(0);
    font-size: 11px;
    font-weight: 700;
    color: #8c8c8c;
  }

  /* ═══════════════════════════════════════════════════════════════════
     BOTÓN MOSTRAR/OCULTAR PASSWORD
     ═══════════════════════════════════════════════════════════════════ */
  .toggle-password {
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    background: transparent;
    border: none;
    color: #8c8c8c;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.8px;
    cursor: pointer;
    padding: 4px 8px;
    font-family: inherit;
  }

  .toggle-password:hover {
    color: #e5e5e5;
  }

  /* ═══════════════════════════════════════════════════════════════════
     BOTÓN PRINCIPAL LOGIN
     ═══════════════════════════════════════════════════════════════════ */
  .login-btn {
    width: 100%;
    min-height: 48px;
    background-color: #E50914;
    color: #fff;
    font-size: 16px;
    font-weight: 700;
    font-family: inherit;
    border: none;
    border-radius: 4px;
    padding: 16px;
    margin-top: 24px;
    cursor: pointer;
    transition: background-color 0.2s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    letter-spacing: 0.2px;
  }

  .login-btn:hover:not(:disabled) {
    background-color: #f40612;
  }

  .login-btn:active:not(:disabled) {
    background-color: #bf0411;
  }

  .login-btn:disabled {
    background-color: #e5091488;
    cursor: not-allowed;
  }

  .spinner {
    width: 24px;
    height: 24px;
    border: 3px solid rgba(255,255,255,0.3);
    border-top-color: #fff;
    border-radius: 50%;
    animation: spin 0.6s linear infinite;
    display: inline-block;
  }

  @keyframes spin {
    to { transform: rotate(360deg); }
  }

  /* ═══════════════════════════════════════════════════════════════════
     ACCIONES SECUNDARIAS (Recuérdame / Ayuda)
     ═══════════════════════════════════════════════════════════════════ */
  .login-form-other {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 2px;
  }

  .remember-me {
    display: flex;
    align-items: center;
    gap: 4px;
  }

  .remember-me input[type="checkbox"] {
    width: 16px;
    height: 16px;
    accent-color: #737373;
    cursor: pointer;
  }

  .checkbox-label {
    position: static;
    color: #b3b3b3;
    font-size: 13px;
    font-weight: 400;
    cursor: pointer;
    transform: none;
    pointer-events: auto;
    transition: none;
  }

  .help-link {
    color: #b3b3b3;
    text-decoration: none;
    font-size: 13px;
  }

  .help-link:hover {
    text-decoration: underline;
  }

  /* ═══════════════════════════════════════════════════════════════════
     SIGNUP PROMPT
     ═══════════════════════════════════════════════════════════════════ */
  .login-signup-now {
    margin-top: 64px;
    font-size: 16px;
    color: #737373;
  }
  .login-signup-now a {
    color: #fff;
    font-weight: 600;
    text-decoration: none;
    margin-left: 4px;
  }
  .login-signup-now a:hover { text-decoration: underline; }

  /* ═══════════════════════════════════════════════════════════════════
     DISCLAIMER (reCAPTCHA)
     ═══════════════════════════════════════════════════════════════════ */
  .login-disclaimer {
    margin-top: 11px;
  }

  .login-disclaimer p {
    font-size: 13px;
    color: #737373;
    line-height: 1.4;
  }

  .login-disclaimer a {
    color: #0071eb;
    text-decoration: none;
  }

  .login-disclaimer a:hover {
    text-decoration: underline;
  }

  /* ═══════════════════════════════════════════════════════════════════
     FOOTER
     ═══════════════════════════════════════════════════════════════════ */
  .login-footer {
    position: relative;
    z-index: 3;
    background: rgba(0, 0, 0, 0.75);
    padding: 30px 0;
    margin-top: auto;
  }

  .footer-content {
    max-width: 1000px;
    margin: 0 auto;
    padding: 0 5%;
  }

  .footer-top-msg {
    color: #737373;
    font-size: 16px;
    margin: 0 0 30px;
  }

  .footer-links {
    list-style: none;
    padding: 0;
    margin: 0 0 24px;
    display: flex;
    flex-wrap: wrap;
    gap: 0;
  }

  .footer-links li {
    width: 25%;
    margin-bottom: 16px;
    min-width: 120px;
  }

  .footer-links a {
    color: #737373;
    text-decoration: none;
    font-size: 13px;
  }

  .footer-links a:hover {
    text-decoration: underline;
  }

  .footer-lang select {
    background: transparent;
    color: #737373;
    border: 1px solid #333;
    padding: 10px 36px 10px 16px;
    font-size: 14px;
    border-radius: 2px;
    appearance: auto;
    cursor: pointer;
  }

  /* ═══════════════════════════════════════════════════════════════════
     RESPONSIVE
     ═══════════════════════════════════════════════════════════════════ */
  @media (max-width: 740px) {
    .login-card {
      max-width: 100%;
      padding: 60px 5% 40px;
      margin: 0;
      min-height: calc(100vh - 80px);
      border-radius: 0;
      background-color: rgba(0, 0, 0, 0.9);
    }

    .bg-image, .bg-overlay {
      opacity: 0;
    }

    .netflix-logo {
      width: 108px;
      height: 30px;
    }

    .footer-links li {
      width: 50%;
    }
  }
</style>
