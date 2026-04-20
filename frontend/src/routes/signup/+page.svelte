<script>
  import { goto } from '$app/navigation';
  import { page } from '$app/stores';
  import { onMount } from 'svelte';
  import { registrarUsuario } from '$lib/api';
  import Swal from 'sweetalert2';

  let nombre = '';
  let apellido = '';
  let email = '';
  let contrasena = '';
  let confirmar = '';
  let cargando = false;
  /** @type {string|null} */
  let error = null;
  let exito = false;
  let showPassword = false;
  let showConfirm = false;

  onMount(() => {
    const params = new URLSearchParams(window.location.search);
    const emailParam = params.get('email');
    if (emailParam) email = emailParam;
  });

  async function handleSubmit() {
    error = null;
    if (!nombre || !apellido || !email || !contrasena || !confirmar) {
      error = 'Todos los campos son obligatorios.';
      return;
    }
    if (contrasena !== confirmar) {
      error = 'Las contraseñas no coinciden.';
      return;
    }
    if (contrasena.length < 6) {
      error = 'La contraseña debe tener al menos 6 caracteres.';
      return;
    }
    cargando = true;
    try {
      await registrarUsuario({ nombre, apellido, email, contrasena });
      await Swal.fire({
        icon: 'success',
        title: '¡Cuenta creada!',
        text: 'Tu cuenta ha sido creada exitosamente. Redirigiendo...',
        background: '#333',
        color: '#fff',
        confirmButtonColor: '#e50914',
        timer: 2500,
        showConfirmButton: false
      });
      goto('/login');
    } catch (e) {
      error = e instanceof Error ? e.message : 'Error desconocido';
      Swal.fire({
        icon: 'error',
        title: 'Error de registro',
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
  <title>Registro – Netflix Colombia</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
</svelte:head>

<div class="signup-page">
  <!-- Fondo igual a la página de login (colage de pósters con overlay) -->
  <div class="bg-image" aria-hidden="true"></div>
  <div class="bg-overlay" aria-hidden="true"></div>

  <!-- Header -->
  <header class="top-header">
    <a href="/" aria-label="Netflix Inicio">
      <img src="/logo.png" alt="Netflix Logo" class="logo" />
    </a>
  </header>

  <!-- Formulario -->
  <main class="signup-wrapper">
    <div class="signup-card">

      {#if exito}
        <div class="success-screen">
          <div class="success-icon-wrap">
            <svg viewBox="0 0 52 52" class="checkmark-svg">
              <circle cx="26" cy="26" r="25" fill="none" stroke="#46d369" stroke-width="2" class="checkmark-circle"/>
              <path fill="none" stroke="#46d369" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" d="M14 27l8 8 16-16" class="checkmark-check"/>
            </svg>
          </div>
          <h2>¡Cuenta creada con éxito!</h2>
          <p>Redirigiendo al inicio de sesión…</p>
        </div>

      {:else}
        <h1>Crear cuenta</h1>

        {#if error}
          <div class="error-banner" role="alert">
            <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor" class="err-icon">
              <path d="M8 1C4.13 1 1 4.13 1 8s3.13 7 7 7 7-3.13 7-7-3.13-7-7-7zm-.5 3h1v5h-1V4zm.5 8a.75.75 0 110-1.5.75.75 0 010 1.5z"/>
            </svg>
            <span>{error}</span>
          </div>
        {/if}

        <form on:submit|preventDefault={handleSubmit} novalidate>
          <!-- Nombre + Apellido -->
          <div class="row-fields">
            <div class="form-input-wrapper" class:has-value={nombre !== ''}>
              <input type="text" id="signupNombre" bind:value={nombre} placeholder=" " autocomplete="given-name" required />
              <label for="signupNombre">Nombre</label>
            </div>
            <div class="form-input-wrapper" class:has-value={apellido !== ''}>
              <input type="text" id="signupApellido" bind:value={apellido} placeholder=" " autocomplete="family-name" required />
              <label for="signupApellido">Apellido</label>
            </div>
          </div>

          <!-- Email -->
          <div class="form-input-wrapper" class:has-value={email !== ''}>
            <input type="email" id="signupEmail" bind:value={email} placeholder=" " autocomplete="email" required />
            <label for="signupEmail">Email o teléfono</label>
          </div>

          <!-- Contraseña -->
          <div class="form-input-wrapper" class:has-value={contrasena !== ''}>
            <input
              type={showPassword ? 'text' : 'password'}
              id="signupPassword"
              bind:value={contrasena}
              placeholder=" "
              autocomplete="new-password"
              required
            />
            <label for="signupPassword">Contraseña</label>
            {#if contrasena.length > 0}
              <button type="button" class="toggle-pw" on:click={() => showPassword = !showPassword}>
                {showPassword ? 'OCULTAR' : 'MOSTRAR'}
              </button>
            {/if}
          </div>

          <!-- Confirmar -->
          <div class="form-input-wrapper" class:has-value={confirmar !== ''}>
            <input
              type={showConfirm ? 'text' : 'password'}
              id="signupConfirm"
              bind:value={confirmar}
              placeholder=" "
              autocomplete="new-password"
              required
            />
            <label for="signupConfirm">Confirmar contraseña</label>
            {#if confirmar.length > 0}
              <button type="button" class="toggle-pw" on:click={() => showConfirm = !showConfirm}>
                {showConfirm ? 'OCULTAR' : 'MOSTRAR'}
              </button>
            {/if}
          </div>

          <!-- Submit -->
          <button type="submit" class="submit-btn" id="signupSubmit" disabled={cargando}>
            {#if cargando}
              <span class="spinner"></span>
            {:else}
              Crear cuenta
            {/if}
          </button>
        </form>

        <div class="login-link">
          <span>¿Ya tienes una cuenta?</span>
          <a href="/login">Inicia sesión.</a>
        </div>

        <div class="disclaimer">
          <p>Esta página está protegida por Google reCAPTCHA para asegurarnos de que no eres un robot.
          <a href="#learn-more">Más info.</a></p>
        </div>
      {/if}

    </div>
  </main>

  <!-- Footer -->
  <footer class="signup-footer">
    <div class="footer-content">
      <p>¿Preguntas? Llama al 01-800-123-4567</p>
      <ul class="footer-links">
        <li><a href="#faq">Preguntas frecuentes</a></li>
        <li><a href="#help">Centro de ayuda</a></li>
        <li><a href="#terms">Términos de uso</a></li>
        <li><a href="#privacy">Privacidad</a></li>
        <li><a href="#cookies">Preferencias de cookies</a></li>
        <li><a href="#corporate">Información corporativa</a></li>
      </ul>
      <select aria-label="Idioma">
        <option value="es">Español</option>
        <option value="en">English</option>
      </select>
    </div>
  </footer>
</div>

<style>
  /* ─── Global Reset ─── */
  :global(*, *::before, *::after) { box-sizing: border-box; }
  :global(body) {
    margin: 0; padding: 0;
    background: #000;
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    color: #fff;
    -webkit-font-smoothing: antialiased;
  }

  /* ─── Page Layout ─── */
  .signup-page {
    position: relative;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }

  /* ─── Background ─── */
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
    background: rgba(0,0,0,0.45);
    background-image: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0) 50%, rgba(0,0,0,0.85) 100%);
    z-index: 1;
  }

  /* ─── Header ─── */
  .top-header {
    position: relative;
    z-index: 3;
    padding: 20px 3%;
    flex-shrink: 0;
  }
  .logo { width: 148px; height: auto; }

  /* ─── Main Wrapper ─── */
  .signup-wrapper {
    position: relative;
    z-index: 2;
    flex: 1;
    display: flex;
    justify-content: center;
    padding: 0 5%;
  }

  /* ─── Card ─── */
  .signup-card {
    background-color: rgba(0,0,0,0.75);
    border-radius: 4px;
    width: 100%;
    max-width: 450px;
    padding: 48px 68px 40px;
    margin-bottom: 90px;
  }

  h1 {
    font-size: 32px;
    font-weight: 700;
    margin: 0 0 28px;
  }

  /* ─── Error Banner ─── */
  .error-banner {
    background: #e87c03;
    border-radius: 4px;
    padding: 10px 16px;
    margin-bottom: 16px;
    font-size: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
    line-height: 1.4;
  }
  .err-icon { flex-shrink: 0; }

  /* ─── Form layout ─── */
  form { display: flex; flex-direction: column; gap: 16px; }
  .row-fields { display: flex; gap: 12px; }
  .row-fields .form-input-wrapper { flex: 1; }

  /* ─── Floating Label Inputs ─── */
  .form-input-wrapper { position: relative; }

  .form-input-wrapper input {
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
    transition: background .2s, border-color .2s;
  }
  .form-input-wrapper input:focus {
    background: #454545;
    border-bottom-color: #e87c03;
  }

  /* Floating label */
  .form-input-wrapper label {
    position: absolute;
    left: 20px;
    top: 50%;
    transform: translateY(-50%);
    color: #8c8c8c;
    font-size: 16px;
    pointer-events: none;
    transition: top .15s, font-size .15s, transform .15s;
  }
  .form-input-wrapper input:focus + label,
  .form-input-wrapper input:not(:placeholder-shown) + label {
    top: 8px;
    transform: translateY(0);
    font-size: 11px;
    font-weight: 700;
  }

  /* Toggle show/hide */
  .toggle-pw {
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    background: transparent;
    border: none;
    color: #8c8c8c;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: .8px;
    cursor: pointer;
    padding: 4px 8px;
    font-family: inherit;
  }
  .toggle-pw:hover { color: #e5e5e5; }

  /* ─── Submit Button ─── */
  .submit-btn {
    width: 100%;
    min-height: 48px;
    background: #E50914;
    color: #fff;
    font-size: 16px;
    font-weight: 700;
    font-family: inherit;
    border: none;
    border-radius: 4px;
    padding: 16px;
    margin-top: 24px;
    cursor: pointer;
    transition: background .2s;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .submit-btn:hover:not(:disabled) { background: #f40612; }
  .submit-btn:disabled { background: #e5091488; cursor: not-allowed; }

  .spinner {
    width: 22px; height: 22px;
    border: 3px solid rgba(255,255,255,.3);
    border-top-color: #fff;
    border-radius: 50%;
    animation: spin .65s linear infinite;
  }
  @keyframes spin { to { transform: rotate(360deg); } }

  /* ─── Login Link ─── */
  .login-link {
    margin-top: 16px;
    font-size: 16px;
    color: #737373;
  }
  .login-link a { color: #fff; text-decoration: none; margin-left: 4px; }
  .login-link a:hover { text-decoration: underline; }

  /* ─── Disclaimer ─── */
  .disclaimer { margin-top: 11px; }
  .disclaimer p { font-size: 13px; color: #737373; line-height: 1.4; }
  .disclaimer a { color: #0071eb; text-decoration: none; }
  .disclaimer a:hover { text-decoration: underline; }

  /* ─── Success screen ─── */
  .success-screen {
    text-align: center;
    padding: 20px 0 10px;
  }
  .success-icon-wrap { margin-bottom: 20px; display: flex; justify-content: center; }
  .checkmark-svg { width: 70px; height: 70px; }
  .checkmark-circle { stroke-dasharray: 160; stroke-dashoffset: 160; animation: draw-circle .6s ease forwards; }
  .checkmark-check { stroke-dasharray: 60; stroke-dashoffset: 60; animation: draw-check .4s .5s ease forwards; }
  @keyframes draw-circle { to { stroke-dashoffset: 0; } }
  @keyframes draw-check { to { stroke-dashoffset: 0; } }
  .success-screen h2 { font-size: 26px; font-weight: 700; color: #46d369; margin-bottom: 8px; }
  .success-screen p { font-size: 15px; color: #737373; }

  /* ─── Footer ─── */
  .signup-footer {
    position: relative;
    z-index: 3;
    background: rgba(0,0,0,0.75);
    padding: 30px 0;
    margin-top: auto;
  }
  .footer-content {
    max-width: 1000px;
    margin: 0 auto;
    padding: 0 5%;
  }
  .footer-content > p { color: #737373; font-size: 16px; margin: 0 0 20px; }
  .footer-links {
    list-style: none;
    padding: 0; margin: 0 0 16px;
    display: flex; flex-wrap: wrap;
  }
  .footer-links li { width: 25%; margin-bottom: 16px; min-width: 110px; }
  .footer-links a { color: #737373; text-decoration: none; font-size: 13px; }
  .footer-links a:hover { text-decoration: underline; }
  .footer-content select {
    background: transparent;
    color: #737373;
    border: 1px solid #333;
    padding: 8px 32px 8px 14px;
    font-size: 14px;
    border-radius: 2px;
    cursor: pointer;
  }

  /* ─── Responsive ─── */
  @media (max-width: 740px) {
    .signup-card { max-width: 100%; padding: 48px 5% 40px; margin: 0; border-radius: 0; }
    .row-fields { flex-direction: column; }
    .logo { width: 108px; }
    .footer-links li { width: 50%; }
  }
</style>