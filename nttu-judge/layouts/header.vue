<!--
 * @Author: hibana2077 hibana2077@gmail.com
 * @Date: 2023-05-02 21:36:33
 * @LastEditors: hibana2077 hibana2077@gmail.com
 * @LastEditTime: 2023-05-03 00:17:11
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
  >
    <el-menu-item index="0" class="font-semibold">NTTUOJ</el-menu-item>
    <div class="flex-grow" />
    <el-menu-item index="1">
      <el-icon color="#409EFC" class="no-inherit">
        <User />
      </el-icon>
      Login</el-menu-item>
    <el-sub-menu index="2">
      <template #title>Workspace</template>
      <el-menu-item index="2-1">item one</el-menu-item>
      <el-menu-item index="2-2">item two</el-menu-item>
      <el-menu-item index="2-3">item three</el-menu-item>
      <el-sub-menu index="2-4">
        <template #title>item four</template>
        <el-menu-item index="2-4-1">item one</el-menu-item>
        <el-menu-item index="2-4-2">item two</el-menu-item>
        <el-menu-item index="2-4-3">item three</el-menu-item>
      </el-sub-menu>
    </el-sub-menu>
  </el-menu>
  <slot />
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
</script>

<style>
.flex-grow {
  flex-grow: 1;
}
</style>