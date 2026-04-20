<script>
  import { onMount, onDestroy } from 'svelte';
  import { goto } from '$app/navigation';

  let isScrolled = false;
  let menuVisible = false;

  const handleScroll = () => {
    isScrolled = window.scrollY > 50;
  };

  onMount(() => {
    window.addEventListener('scroll', handleScroll);
  });

  onDestroy(() => {
    if (typeof window !== 'undefined') {
      window.removeEventListener('scroll', handleScroll);
    }
  });

  function cerrarSesion() {
    // Limpiar cualquier dato de sesión simulado en localStorage/sessionStorage
    localStorage.removeItem('usuario');
    sessionStorage.removeItem('usuario');
    menuVisible = false;
    goto('/');
  }

  function toggleMenu() {
    menuVisible = !menuVisible;
  }
</script>

<!-- Click fuera cierra el menú -->
<svelte:window on:click={(e) => {
  const el = /** @type {Element} */ (e.target);
  if (!el.closest('.profile-menu-wrapper')) menuVisible = false;
}} />

<nav class="navbar" class:scrolled={isScrolled}>
  <div class="nav-left">
    <!-- Logo SVG Oficial Netflix -->
    <a href="/browse" class="logo-link" aria-label="Netflix Inicio">
      <img src="/logo.png" alt="Netflix Logo" class="logo" />
    </a>
    <ul class="nav-links">
      <li><a href="/browse" class="active">Inicio</a></li>
      <li><a href="#series">Series</a></li>
      <li><a href="#peliculas">Películas</a></li>
      <li><a href="#novedades">Novedades populares</a></li>
      <li><a href="#milista">Mi lista</a></li>
    </ul>
  </div>

  <div class="nav-right">
    <button class="icon-btn" aria-label="Buscar">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
    </button>
    <a href="#kids" class="kids-link">Niños</a>
    <button class="icon-btn" aria-label="Notificaciones">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>
    </button>

    <!-- Avatar + Menú desplegable -->
    <div class="profile-menu-wrapper">
      <button class="profile-avatar" on:click|stopPropagation={toggleMenu} aria-expanded={menuVisible} aria-label="Menú de perfil">
        <img src="https://upload.wikimedia.org/wikipedia/commons/0/0b/Netflix-avatar.png" alt="Perfil" />
        <svg viewBox="0 0 24 24" class="caret-icon" class:rotated={menuVisible} fill="currentColor">
          <path d="M7 10l5 5 5-5z"/>
        </svg>
      </button>

      {#if menuVisible}
        <div class="profile-dropdown">
          <!-- Perfiles al estilo Netflix -->
          <div class="dropdown-profile-row">
            <img class="dropdown-avatar" src="https://upload.wikimedia.org/wikipedia/commons/0/0b/Netflix-avatar.png" alt="Mi Perfil" />
            <span>Mi Perfil</span>
          </div>
          <hr class="dropdown-divider" />
          <a href="#account" class="dropdown-item">Cuenta</a>
          <a href="#help" class="dropdown-item">Centro de ayuda</a>
          <hr class="dropdown-divider" />
          <button class="dropdown-item logout-btn" on:click={cerrarSesion}>
            Cerrar sesión de Netflix
          </button>
        </div>
      {/if}
    </div>
  </div>
</nav>

<style>
  .navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 68px;
    padding: 0 4%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: transparent;
    background-image: linear-gradient(to bottom, rgba(0,0,0,0.7) 10%, rgba(0,0,0,0));
    z-index: 100;
    transition: background-color 0.4s ease;
    box-sizing: border-box;
  }

  .navbar.scrolled {
    background-color: #141414;
    background-image: none;
  }

  .nav-left, .nav-right {
    display: flex;
    align-items: center;
  }

  .logo-link {
    margin-right: 32px;
    display: flex;
    align-items: center;
    flex-shrink: 0;
  }

  .logo {
    width: 150px;
    height: auto;
  }

  .nav-links {
    list-style: none;
    display: flex;
    gap: 20px;
    margin: 0;
    padding: 0;
  }

  .nav-links a {
    color: #e5e5e5;
    text-decoration: none;
    font-size: 0.85rem;
    transition: color 0.4s;
  }

  .nav-links a:hover, .nav-links a.active {
    color: #ffffff;
    font-weight: 500;
  }

  .nav-right {
    gap: 20px;
  }

  .icon { width: 24px; height: 24px; color: white; }

  .icon-btn {
    background: transparent;
    border: none;
    cursor: pointer;
    padding: 0;
    display: flex;
    align-items: center;
  }

  .kids-link {
    color: #e5e5e5;
    text-decoration: none;
    font-size: 0.85rem;
  }

  /* ── Avatar y dropdown ── */
  .profile-menu-wrapper {
    position: relative;
  }

  .profile-avatar {
    display: flex;
    align-items: center;
    gap: 6px;
    cursor: pointer;
    background: transparent;
    border: none;
    padding: 0;
  }

  .profile-avatar img {
    border-radius: 4px;
    width: 32px;
    height: 32px;
    object-fit: cover;
  }

  .caret-icon {
    width: 16px;
    height: 16px;
    color: white;
    transition: transform 0.3s;
  }

  .caret-icon.rotated {
    transform: rotate(180deg);
  }

  /* Dropdown */
  .profile-dropdown {
    position: absolute;
    top: calc(100% + 16px);
    right: 0;
    min-width: 200px;
    background-color: rgba(0, 0, 0, 0.9);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 4px;
    padding: 8px 0;
    display: flex;
    flex-direction: column;
    animation: fadeIn 0.2s ease;
    z-index: 200;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(-6px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  /* Triángulito apuntador */
  .profile-dropdown::before {
    content: '';
    position: absolute;
    top: -6px;
    right: 16px;
    border-left: 6px solid transparent;
    border-right: 6px solid transparent;
    border-bottom: 6px solid rgba(255,255,255,0.15);
  }

  .dropdown-profile-row {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 16px;
    color: white;
    font-size: 13px;
  }

  .dropdown-avatar {
    width: 28px;
    height: 28px;
    border-radius: 4px;
  }

  .dropdown-divider {
    border: none;
    border-top: 1px solid rgba(255,255,255,0.15);
    margin: 4px 0;
  }

  .dropdown-item {
    display: block;
    padding: 10px 16px;
    color: #b3b3b3;
    font-size: 13px;
    text-decoration: none;
    text-align: left;
    background: transparent;
    border: none;
    width: 100%;
    cursor: pointer;
    font-family: inherit;
    transition: color 0.2s;
  }

  .dropdown-item:hover {
    color: white;
  }

  .logout-btn {
    color: #b3b3b3;
  }

  @media (max-width: 800px) {
    .nav-links { display: none; }
    .logo { width: 80px; }
  }
</style>
