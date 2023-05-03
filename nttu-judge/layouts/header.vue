<!--
 * @Author: hibana2077 hibana2077@gmail.com
 * @Date: 2023-05-02 21:36:33
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2023-05-03 12:43:25
 * @FilePath: \NTTU-new-gen-judge-system\nttu-judge\layouts\header.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
  <el-menu
    :default-active="activeIndex"
    class="el-menu-demo"
    mode="horizontal"
    :ellipsis="false"
    @select="handleSelect"
    menu-trigger="hover"
  >
    <el-menu-item index="0" class="font-semibold">
      <NuxtLink to="/">NTTUOJ</NuxtLink>
    </el-menu-item>
    <div class="flex-grow" />
    <el-menu-item index="1">
      <el-icon color="#409EFC" class="no-inherit">
        <User />
      </el-icon>
      <p v-if="islogin">
        <NuxtLink :to="`/users/${username}`">{{ username }}</NuxtLink>
      </p>
      <p v-else>Sign in/up</p>
    </el-menu-item>
    <el-sub-menu index="2">
      <template #title>
        <el-icon color="#409EFC" class="no-inherit">
          <Menu />
        </el-icon>
        Menu
      </template>
      <el-menu-item index="2-1">
        <el-icon color="#409EFC" class="no-inherit">
          <Setting />
        </el-icon>
        Settings
      </el-menu-item>
      <el-menu-item index="2-2">
        <el-icon color="#409EFC" class="no-inherit">
          <ChatDotRound />
        </el-icon>
        Forum
      </el-menu-item>
      <el-menu-item index="2-3">
        <el-icon color="#409EFC" class="no-inherit">
          <Notebook />
        </el-icon>
        Notebook
      </el-menu-item>
      <el-sub-menu index="2-4">
        <template #title>
          <el-icon color="#409EFC" class="no-inherit">
            <Trophy />
          </el-icon>
          contest
        </template>
        <el-menu-item v-for="item in 10" :key="item" :index="`2-4-${item}`">
          item {{ item }}
        </el-menu-item>
      </el-sub-menu>
    </el-sub-menu>
  </el-menu>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
//add this if you want to use icons
import * as ElementPlusIcons from '@element-plus/icons-vue'

//add this if you want to use icons
const nuxtApp = useNuxtApp()
for (const [key, component] of Object.entries(ElementPlusIcons)) {
  nuxtApp.vueApp.component(key, component)
}
//to this
const activeIndex = ref('1')
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const islogin = ref(true) //TODO: change this to vue state management
const username = ref('hibana2077') //TODO: change this to vue state management
</script>

<style>
.flex-grow {
  flex-grow: 1;
}
</style>