<!--
 * @Author: hibana2077 hibana2077@gmaill.com
 * @Date: 2023-05-03 11:45:56
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2023-05-08 15:15:42
 * @FilePath: /NTTU-new-gen-judge-system/nttu-judge/pages/index.vue 
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
  <el-card class="box-card" style="margin-top: 1% ; margin-left: 5%; margin-right: 5%; margin-bottom: 2%;">
    <template #header>
      <div class="card-header">
        <span class="font-bold">Billboard</span>
        <el-button class="button" type="primary" round text>Refresh</el-button>
      </div>
    </template>
    <div v-for="o in 4" :key="o" class="text item">{{ 'List item ' + o }}</div>
  </el-card>
</template>

<style>
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.box-card {
  width: 480px;
}
</style>
