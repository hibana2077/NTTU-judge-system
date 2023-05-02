<!--
 * @Author: hibana2077 hibana2077@gmaill.com
 * @Date: 2023-05-01 17:51:11
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2023-05-01 17:52:44
 * @FilePath: /NTTU-new-gen-judge-system/nttu-judge/pages/[...slug].vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
    <div class="bg-white py-24">
      <div class="flex flex-col items-center">
        <h1 class="text-8xl font-semibold text-red-500">404</h1>
        <p class="my-8 text-3xl text-gray-800">Not Found</p>
        <p class="my-8 text-xl text-gray-800">真的是找不到这个页面啦 (;-;) </p>
      </div>
    </div>
  </template>
  
  <script setup>
  setResponseStatus(404)
  </script>