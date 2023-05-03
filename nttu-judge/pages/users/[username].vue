<!--
 * @Author: hibana2077 hibana2077@gmaill.com
 * @Date: 2023-05-02 12:58:16
 * @LastEditors: hibana2077 hibana2077@gmail.com
 * @LastEditTime: 2023-05-03 09:23:57
 * @FilePath: /NTTU-new-gen-judge-system/nttu-judge/pages/users/[id].vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
    <div class="bg-white py-24">
      <div class="flex flex-col items-center">
        <h1 class="text-3xl text-gray-600">这里是 Users 动态路由页面</h1>
        <p class="my-8 text-3xl text-gray-600">
          匹配到的 Id: <span class="text-5xl font-semibold text-blue-600">{{ username }}</span>
        </p>
      </div>
    </div>
  </template>
  
<script setup>
  const route = useRoute()
  const { username } = route.params
</script>