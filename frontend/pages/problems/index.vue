<!--
 * @Author: hibana2077 hibana2077@gmail.com
 * @Date: 2023-10-10 15:48:40
 * @LastEditors: hibana2077 hibana2077@gmail.com
 * @LastEditTime: 2023-10-10 16:39:01
 * @FilePath: \NTTU-judge-system\frontend\pages\problems\index.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<script setup>

//const 
//layout name
const layout = 'navbar'
</script>



<template>
    <ClientOnly>
        <!-- nav bar -->
        <NuxtLayout :name="layout" />
    
        <!-- Content -->
        <UCard>
            <template #header>
                <h2 class="text-xl font-semibold">Questions</h2>
            </template>
        </UCard>
        
        <!-- below block is for randering the content of the page -->
        <template #fallback>
            <div class="fixed inset-0 flex items-center justify-center">
                <div class="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-primary-500"></div>
            </div>
        </template>
        <!-- end -->
    </ClientOnly>
</template>
  