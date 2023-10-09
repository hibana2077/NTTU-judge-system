<template>
    <div class="flex h-full bg-gray-100">
      <!-- Sidebar -->
      <div class="bg-white w-64 flex flex-col p-4">
        <h1 class="text-2xl font-semibold mb-4 text-primary">Docs</h1>
        <ul>
            <li class="mb-2"><ULink to="/">Home</ULink></li>
            <li class="mb-2"><a href="#section1">Section 1</a></li>
            <li class="mb-2"><a href="#section2">Section 2</a></li>
            <li class="mb-2"><a href="#section3">Section 3</a></li>
        </ul>
      </div>
  
      <!-- Content -->
      <div class="flex-1 p-8">
        <h1 class="text-3xl font-bold mb-4" id="section1">Section 1</h1>
        <p class="mb-4">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio.</p>
        <img class="mb-4" src="https://via.placeholder.com/400x300" alt="Placeholder Image">
  
        <h2 class="text-2xl font-bold mb-4" id="section2">Section 2</h2>
        <p class="mb-4">Sed cursus ante dapibus diam. Nulla quis sem at nibh elementum imperdiet.</p>
        <img class="mb-4" src="https://via.placeholder.com/400x300" alt="Placeholder Image">
  
        <h3 class="text-xl font-bold mb-4" id="section3">Section 3</h3>
        <p class="mb-4">Nullam quis risus eget urna mollis ornare vel eu leo.</p>
        <img class="mb-4" src="https://via.placeholder.com/400x300" alt="Placeholder Image">
      </div>

      <UButton @click="scrollToTop" class="fixed bottom-4 right-4 p-4 text-white rounded-full" icon="i-heroicons-arrow-up-20-solid" />

    </div>
  </template>
  
<script setup>
const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
};
</script>
  
  <style scoped>
  /* Your custom styles here */
  </style>
  