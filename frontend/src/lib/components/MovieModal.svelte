<script>
  import { createEventDispatcher } from 'svelte';
  export let movie;
  
  const dispatch = createEventDispatcher();
  
  function close() {
    dispatch('close');
  }
</script>

<!-- Clic fuera de la modal también cierra la ventana -->
<!-- svelte-ignore a11y-click-events-have-key-events a11y-no-static-element-interactions -->
<div class="modal-backdrop" on:click={close}>
  <div class="modal-content" on:click|stopPropagation>
    <button class="close-btn" aria-label="Cerrar modal" on:click={close}>✕</button>
    
    <div class="modal-hero">
      <img src={movie.image} alt={movie.title} class="modal-poster" />
      <div class="modal-gradient"></div>
    </div>
    
    <div class="modal-info">
      <h2 class="modal-title">{movie.title}</h2>
      
      <div class="modal-meta">
        <span class="match-score">98% para ti</span>
        <span class="year">2024</span>
        <span class="rating">TV-MA</span>
        <span class="duration">2h 15m</span>
      </div>
      
      <p class="modal-desc">{movie.description || 'Esta película es uno de los mayores éxitos de la plataforma. Una imperdible historia ahora disponible.'}</p>
      
      <div class="modal-cast">
        <strong>Reparto:</strong> {movie.cast || 'Estrellas de Hollywood, Director Reconocido'}
      </div>
    </div>
  </div>
</div>

<style>
  .modal-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.8);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9999;
    animation: fadeIn 0.3s ease;
  }
  
  .modal-content {
    background: #181818;
    width: 90%;
    max-width: 800px;
    border-radius: 8px;
    overflow: hidden;
    position: relative;
    box-shadow: 0 15px 30px rgba(0,0,0,0.5);
    animation: slideUp 0.3s ease;
  }
  
  .modal-hero {
    position: relative;
    width: 100%;
    height: 380px;
  }
  
  .modal-poster {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  .modal-gradient {
    position: absolute;
    inset: 0;
    background: linear-gradient(to top, #181818 0%, rgba(24,24,24,0) 60%);
  }
  
  .close-btn {
    position: absolute;
    top: 15px;
    right: 15px;
    background: #181818;
    color: white;
    border: none;
    border-radius: 50%;
    width: 36px;
    height: 36px;
    font-size: 1.2rem;
    font-weight: bold;
    cursor: pointer;
    z-index: 10;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: background 0.2s;
  }
  .close-btn:hover {
    background: #333;
  }
  
  .modal-info {
    padding: 0 40px 40px;
    margin-top: -50px;
    position: relative;
    z-index: 2;
    color: white;
  }
  
  .modal-title {
    font-size: 2.5rem;
    font-weight: 900;
    margin-bottom: 15px;
    text-shadow: 1px 1px 4px rgba(0,0,0,0.8);
  }
  
  .modal-meta {
    margin-bottom: 20px;
    font-size: 1.05rem;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  
  .match-score {
    color: #46d369;
    font-weight: bold;
  }
  .rating {
    border: 1px solid rgba(255,255,255,0.4);
    padding: 0 4px;
    font-size: 0.85rem;
  }
  
  .modal-desc {
    font-size: 1.15rem;
    line-height: 1.5;
    margin-bottom: 20px;
    color: #d2d2d2;
    max-width: 650px;
  }
  
  .modal-cast {
    font-size: 0.9rem;
    color: #777;
    margin-top: 10px;
  }
  .modal-cast strong {
    color: #a3a3a3;
  }
  
  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }
  @keyframes slideUp {
    from { transform: translateY(30px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
  }
  
  @media (max-width: 600px) {
    .modal-hero { height: 250px; }
    .modal-info { padding: 0 20px 20px; margin-top: -30px; }
    .modal-title { font-size: 1.8rem; }
  }
</style>
