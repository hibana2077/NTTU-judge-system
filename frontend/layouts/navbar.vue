<!--
 * @Author: hibana2077 hibana2077@gmail.com
 * @Date: 2023-10-10 15:53:49
 * @LastEditors: hibana2077 hibana2077@gmail.com
 * @LastEditTime: 2023-10-10 16:20:19
 * @FilePath: \NTTU-judge-system\frontend\layouts\navbar.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->

<script setup>
// dark mode function
const colorMode = useColorMode()

const isDark = computed({
  get () {
    return colorMode.value === 'dark'
  },
  set () {
    colorMode.preference = colorMode.value === 'dark' ? 'light' : 'dark'
  }
})
// dark mode function end

// table of contents function
const columns = [
  {
    key: 'id',
    label: '#'
  },
  {
    key: 'title',
    label: 'Title'
  },
  {
    key: 'content',
    label: 'Content'
  },
  {
    key: 'author',
    label: 'Author'
  },
  {
    key: 'date',
    label: 'Date'
  },
  {
    key: 'action'
  }
]
</script>

<template>
    <UContainer class="border-black-200 border-b-2 max-w-none">
      <nav class="flex justify-start items-center py-5 text-gray-600 border-slate-200 w-full">
        <ULink to="/" class="flex items-center space-x-2">
          <UImage
            src="/logo.png"
            alt="logo"
            width="40"
            height="40"
            class="rounded-full"
          />
          <span class="text-xl font-bold text-green-700">NTTUOJ</span>
        </ULink>
        <div class="flex-grow"></div>
        <div class="flex items-center space-x-2">
            <ULink to="/docs" class="px-3 py-2 rounded-md hover:bg-gray-700 hover:text-white flex items-center">
                <UIcon name="i-heroicons-book-open-20-solid" class="mr-2" />
                Docs
            </ULink>
          <ULink to="/problems" class="px-3 py-2 rounded-md hover:bg-gray-700 hover:text-white flex items-center">
            <UIcon name="i-heroicons-cube-20-solid" class="mr-2" />
            Problems
          </ULink>
          <ULink to="/examples" class="px-3 py-2 rounded-md hover:bg-gray-700 hover:text-white flex items-center">
            <UIcon name="i-heroicons-trophy-20-solid" class="mr-2" />
            Contests
          </ULink>
          <ULink to="/blog" class="px-3 py-2 rounded-md hover:bg-gray-700 hover:text-white flex items-center">
            <UIcon name="i-heroicons-newspaper-20-solid" class="mr-2" />
            Status
          </ULink>
          <ULink to="login" class="px-3 py-2 rounded-3xl bg-green-700 text-white hover:bg-gray-700 hover:text-white">
            Login
          </ULink>
          <UButton
          :icon="isDark ? 'i-heroicons-moon-20-solid' : 'i-heroicons-sun-20-solid'"
          color="gray"
          variant="ghost"
          aria-label="Theme"
          @click="isDark = !isDark"
          />
        </div>
      </nav>
    </UContainer>
</template>