<!--
 * @Author: hibana2077 hibana2077@gmail.com
 * @Date: 2023-05-01 20:11:46
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2023-05-03 12:38:47
 * @FilePath: \NTTU-new-gen-judge-system\nttu-judge\pages\index.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
  <div class="common-layout">
    <el-container>
      <el-row :gutter="12">
    <el-col :span="10">
      <el-card shadow="always"> Always </el-card>
    </el-col>
    <el-col :span="10">
      <el-card shadow="hover"> Hover </el-card>
    </el-col>
    <el-col :span="10">
      <el-card shadow="never"> Never </el-card>
    </el-col>
  </el-row>
    </el-container>
  </div>
</template>