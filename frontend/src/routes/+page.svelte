<script>
  // Importamos todos los componentes construidos
  import HeroSection from '$lib/components/landing/HeroSection.svelte';
  import TrendingSection from '$lib/components/landing/TrendingSection.svelte';
  import FeatureCards from '$lib/components/landing/FeatureCards.svelte';
  import FaqAccordion from '$lib/components/landing/FaqAccordion.svelte';
  import Footer from '$lib/components/landing/Footer.svelte';
</script>

<svelte:head>
  <title>Netflix Colombia: ve series online, ve películas online</title>
</svelte:head>

<main class="landing-page">
  <HeroSection />
  
  <div class="separator"></div>
  <TrendingSection />
  
  <div class="separator"></div>
  <FeatureCards />
  
  <div class="separator"></div>
  <FaqAccordion />

  <div class="separator"></div>
  <Footer />
</main>

<style>
  :global(body) {
    margin: 0;
    padding: 0;
    background-color: #000;
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    color: #fff;
    -webkit-font-smoothing: antialiased;
  }

  .landing-page {
    display: flex;
    flex-direction: column;
  }

  .separator {
    height: 8px;
    background-color: #232323;
    width: 100%;
  }

  /* Evitar scroll horizontal si algún elemento crece mucho */
  :global(*, *::before, *::after) {
    box-sizing: border-box;
  }
</style>
