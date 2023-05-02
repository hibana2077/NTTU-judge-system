<!--
 * @Author: hibana2077 hibana2077@gmaill.com
 * @Date: 2023-05-02 14:44:41
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2023-05-02 14:50:30
 * @FilePath: /NTTU-new-gen-judge-system/nttu-judge/layouts/Header.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
    <div>
      <el-container>
        <el-header class="text-6xl font-semibold text-rose-400" style="background-color: #409EFF;">Header</el-header>
      </el-container>
      <slot />
    </div>
</template>