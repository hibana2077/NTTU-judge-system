<template>
    <div class="flex flex-col items-center justify-center h-screen">
        <svg viewBox="0 0 1000 1000" xmlns="http://www.w3.org/2000/svg"><defs><clipPath id="a"><path fill="currentColor" d="M849.5 627q-46.5 127-167 175.5t-264 68Q275 890 168.5 775t-119-279.5Q37 331 189 278t272.5-147q120.5-94 208 29.5t157 231.5q69.5 108 23 235Z"/></clipPath></defs><g clip-path="url(#a)"><path fill="#22c55e" d="M849.5 627q-46.5 127-167 175.5t-264 68Q275 890 168.5 775t-119-279.5Q37 331 189 278t272.5-147q120.5-94 208 29.5t157 231.5q69.5 108 23 235Z"/></g></svg>
    </div>
    <!-- glass effect card -->
    <div class="absolute inset-0 flex items-center justify-center">
        <UCard class="w-96 h-96 bg-white bg-opacity-10 rounded-2xl backdrop-filter backdrop-blur-lg flex flex-col items-center justify-center">
            <h1 class="text-4xl font-bold text-white mb-4">Login</h1>
            <UInput v-model="username" placeholder="Username" class="mb-4" />
            <UInput v-model="password" placeholder="Password" class="mb-4" type="password" />
            <UButton color="primary" class="mb-4 text-white" :ui="{ rounded: 'rounded-full' }"  @click="login">Login</UButton>
        </UCard>
    </div>
</template>

<script setup>

const username = ref('')
const password = ref('')
</script>