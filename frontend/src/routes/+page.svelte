<script>
  import { registrarUsuario } from '$lib/api';

  /** @type {string} */
  let nombre = '';

  /** @type {string} */
  let apellido = '';

  /** @type {string} */
  let contrasena = '';

  /** @type {string} */
  let confirmar = '';

  /** @type {boolean} */
  let cargando = false;

  /** @type {string | null} */
  let error = null;

  /** @type {boolean} */
  let exito = false;

  async function handleSubmit() {
    error = null;

    if (!nombre || !apellido || !contrasena || !confirmar) {
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
      await registrarUsuario({ nombre, apellido, contrasena });
      exito = true;
      nombre = '';
      apellido = '';
      contrasena = '';
      confirmar = '';
    } catch (e) {
      error = e instanceof Error ? e.message : 'Error desconocido';
    } finally {
      cargando = false;
    }
  }
</script>

<main>
  <div class="bg-grid"></div>

  <div class="card">
    <div class="brand">
      <span class="logo-icon">▶</span>
      <span class="logo-text">NetflixApp</span>
    </div>

    <h1>Crear cuenta</h1>
    <p class="subtitle">Únete y empieza a disfrutar el contenido</p>

    {#if exito}
      <div class="success">
        <span class="success-icon">✓</span>
        <div>
          <strong>¡Registro exitoso!</strong>
          <p>Tu cuenta ha sido creada correctamente.</p>
        </div>
      </div>
    {/if}

    {#if error}
      <div class="error">⚠ {error}</div>
    {/if}

    <form on:submit|preventDefault={handleSubmit}>
      <div class="row">
        <div class="field">
          <label for="nombre">Nombre</label>
          <input
            id="nombre"
            type="text"
            bind:value={nombre}
            placeholder="Juan"
            autocomplete="given-name"
          />
        </div>
        <div class="field">
          <label for="apellido">Apellido</label>
          <input
            id="apellido"
            type="text"
            bind:value={apellido}
            placeholder="Pérez"
            autocomplete="family-name"
          />
        </div>
      </div>

      <div class="field">
        <label for="contrasena">Contraseña</label>
        <input
          id="contrasena"
          type="password"
          bind:value={contrasena}
          placeholder="Mínimo 6 caracteres"
          autocomplete="new-password"
        />
      </div>

      <div class="field">
        <label for="confirmar">Confirmar contraseña</label>
        <input
          id="confirmar"
          type="password"
          bind:value={confirmar}
          placeholder="Repite tu contraseña"
          autocomplete="new-password"
        />
      </div>

      <button type="submit" disabled={cargando}>
        {#if cargando}
          <span class="spinner"></span> Registrando…
        {:else}
          Crear cuenta
        {/if}
      </button>
    </form>

    <p class="login-link">¿Ya tienes cuenta? <a href="/login">Inicia sesión</a></p>
  </div>
</main>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@400;500;600&display=swap');

  :global(*, *::before, *::after) { box-sizing: border-box; margin: 0; padding: 0; }

  :global(body) {
    background: #0d0d0d;
    color: #f0eeea;
    font-family: 'DM Sans', sans-serif;
    min-height: 100vh;
  }

  main {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2rem 1rem;
    position: relative;
    overflow: hidden;
  }

  .bg-grid {
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(#e5000015 1px, transparent 1px),
      linear-gradient(90deg, #e5000015 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
  }

  .card {
    position: relative;
    z-index: 1;
    background: #161616;
    border: 1px solid #2a2a2a;
    border-radius: 16px;
    padding: 2.5rem 2rem;
    width: 100%;
    max-width: 460px;
    box-shadow: 0 0 60px #e5000018;
  }

  .brand {
    display: flex;
    align-items: center;
    gap: .5rem;
    margin-bottom: 1.75rem;
  }

  .logo-icon {
    background: #e50000;
    color: #fff;
    font-size: .75rem;
    width: 28px;
    height: 28px;
    border-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .logo-text {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.3rem;
    letter-spacing: .05em;
    color: #f0eeea;
  }

  h1 {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2rem;
    letter-spacing: .03em;
    color: #f0eeea;
    margin-bottom: .35rem;
  }

  .subtitle {
    font-size: .875rem;
    color: #666;
    margin-bottom: 1.75rem;
  }

  form { display: flex; flex-direction: column; gap: 1rem; }

  .row { display: flex; gap: .75rem; }
  .row .field { flex: 1; }

  .field { display: flex; flex-direction: column; gap: .4rem; }

  label {
    font-size: .78rem;
    font-weight: 600;
    color: #888;
    letter-spacing: .04em;
    text-transform: uppercase;
  }

  input {
    background: #0d0d0d;
    border: 1px solid #2a2a2a;
    border-radius: 8px;
    padding: .7rem 1rem;
    color: #f0eeea;
    font-family: 'DM Sans', sans-serif;
    font-size: .9rem;
    outline: none;
    transition: border-color .2s;
    width: 100%;
  }

  input:focus { border-color: #e50000; }
  input::placeholder { color: #3a3a3a; }

  button[type="submit"] {
    margin-top: .5rem;
    background: #e50000;
    border: none;
    border-radius: 8px;
    padding: .85rem;
    color: #fff;
    font-family: 'DM Sans', sans-serif;
    font-weight: 600;
    font-size: 1rem;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: .5rem;
    transition: background .2s, transform .1s;
  }

  button[type="submit"]:hover:not(:disabled) { background: #cc0000; transform: translateY(-1px); }
  button[type="submit"]:disabled { opacity: .5; cursor: not-allowed; }

  .spinner {
    width: 16px; height: 16px;
    border: 2px solid #ffffff40;
    border-top-color: #fff;
    border-radius: 50%;
    animation: spin .7s linear infinite;
    display: inline-block;
  }
  @keyframes spin { to { transform: rotate(360deg); } }

  .error {
    background: #e5000015;
    border: 1px solid #e5000040;
    color: #ff4444;
    border-radius: 8px;
    padding: .7rem 1rem;
    font-size: .85rem;
    margin-bottom: .5rem;
  }

  .success {
    background: #00c85315;
    border: 1px solid #00c85340;
    border-radius: 8px;
    padding: .85rem 1rem;
    display: flex;
    align-items: flex-start;
    gap: .75rem;
    margin-bottom: .75rem;
  }

  .success-icon {
    background: #00c853;
    color: #fff;
    border-radius: 50%;
    width: 22px; height: 22px;
    display: flex; align-items: center; justify-content: center;
    font-size: .75rem;
    font-weight: 700;
    flex-shrink: 0;
    margin-top: 2px;
  }

  .success strong { font-size: .9rem; color: #00c853; }
  .success p { font-size: .82rem; color: #666; margin-top: .2rem; }

  .login-link {
    text-align: center;
    margin-top: 1.25rem;
    font-size: .85rem;
    color: #555;
  }

  .login-link a { color: #e50000; text-decoration: none; font-weight: 600; }
  .login-link a:hover { text-decoration: underline; }
</style>