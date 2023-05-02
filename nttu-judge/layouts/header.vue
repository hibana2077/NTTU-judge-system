<!--
 * @Author: hibana2077 hibana2077@gmaill.com
 * @Date: 2023-05-02 14:44:41
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2023-05-02 16:14:50
 * @FilePath: /NTTU-new-gen-judge-system/nttu-judge/layouts/Header.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
    <div style="background-color: white;">
      <el-container>
        <el-header>
            <el-text class="flex justify-center text-4xl font-bold text-gray-700">
                NTTU OJ
            </el-text>
            <div style="display: flex; text-align: center;">
                <el-avatar>H</el-avatar>
            </div>
        </el-header>
      </el-container>
      <slot />
    </div>
</template>