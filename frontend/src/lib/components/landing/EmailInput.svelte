<script>
  import { goto } from '$app/navigation';
  let emailValue = '';

  function submitEmail() {
    // Pasar el email por query params a la ruta /signup
    // Ej: /signup?email=test@correo.com
    if(emailValue) {
      goto(`/signup?email=${encodeURIComponent(emailValue)}`);
    } else {
      goto('/signup');
    }
  }
</script>

<form class="email-form" on:submit|preventDefault={submitEmail}>
  <p class="form-title">¿Quieres ver Netflix ya? Ingresa tu email para crear una cuenta o reiniciar tu membresía de Netflix.</p>
  <div class="input-container">
    <div class="input-wrapper">
      <input 
        type="email" 
        id="heroEmail" 
        bind:value={emailValue} 
        required 
        placeholder=" "
      />
      <label for="heroEmail">Email</label>
    </div>
    <button type="submit" class="submit-btn" aria-label="Comenzar">
      Comenzar
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="chevron-icon">
        <path fill-rule="evenodd" clip-rule="evenodd" d="M7.29289 2.29289C7.68342 1.90237 8.31658 1.90237 8.70711 2.29289L18.7071 12.2929C19.0976 12.6834 19.0976 13.3166 18.7071 13.7071L8.70711 23.7071C8.31658 24.0976 7.68342 24.0976 7.29289 23.7071C6.90237 23.3166 6.90237 22.6834 7.29289 22.2929L16.5858 13L7.29289 3.70711C6.90237 3.31658 6.90237 2.68342 7.29289 2.29289Z" fill="currentColor"/>
      </svg>
    </button>
  </div>
</form>

<style>
  .email-form {
    text-align: center;
    max-width: 950px;
    margin: 0 auto;
  }

  .form-title {
    font-size: 20px;
    font-weight: 400;
    margin-bottom: 16px;
    line-height: 1.5;
  }

  .input-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
  }

  .input-wrapper {
    position: relative;
    flex: 1;
    min-width: 250px;
    max-width: 400px;
  }

  input {
    width: 100%;
    height: 56px;
    border: 1px solid rgba(128, 128, 128, 0.7);
    border-radius: 4px;
    background-color: rgba(22, 22, 22, 0.7);
    color: #fff;
    font-size: 16px;
    padding: 24px 16px 8px;
    outline: none;
    transition: background-color 0.2s, box-shadow 0.2s;
  }

  input:focus {
    background-color: rgba(0, 0, 0, 0.5);
    box-shadow: inset 0 0 0 2px white;
    border-color: transparent;
  }

  label {
    position: absolute;
    left: 16px;
    top: 50%;
    transform: translateY(-50%);
    color: rgba(255, 255, 255, 0.7);
    font-size: 16px;
    font-weight: 500;
    pointer-events: none;
    transition: all 0.15s ease;
  }

  input:focus + label,
  input:not(:placeholder-shown) + label {
    top: 14px;
    font-size: 12px;
  }

  .submit-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    height: 56px;
    padding: 0 24px;
    background-color: #E50914;
    color: #fff;
    border: none;
    border-radius: 4px;
    font-size: 24px;
    font-weight: 500;
    cursor: pointer;
    transition: background-color 0.2s;
  }

  .submit-btn:hover {
    background-color: #C11119;
  }

  .chevron-icon {
    width: 24px;
  }

  @media (max-width: 600px) {
    .input-container {
      flex-direction: column;
      align-items: stretch;
    }
    .input-wrapper {
      max-width: 100%;
    }
    .submit-btn {
      font-size: 18px;
      padding: 12px 24px;
      margin-top: 8px;
      align-self: flex-start;
    }
  }
</style>
