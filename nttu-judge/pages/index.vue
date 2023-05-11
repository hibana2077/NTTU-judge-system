<!--
 * @Author: hibana2077 hibana2077@gmaill.com
 * @Date: 2023-05-03 11:45:56
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2023-05-09 16:33:22
 * @FilePath: /NTTU-new-gen-judge-system/nttu-judge/pages/index.vue 
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
  <div class="flex">
    <el-card class="box-card flex-1 p-4" style="margin-top: 1% ; margin-left: 5%; margin-right: 5%; margin-bottom: 2%;">
    <template #header>
      <div class="card-header">
        <span class="font-bold">Billboard</span>
        <el-button class="button" type="primary" round plain>Refresh</el-button>
      </div>
    </template>
    <!-- <div v-for="o in 4" :key="o" class="text item">{{ 'List item ' + o }}</div> -->
    <div v-for="item in Billboards" :key="item" class="text item">
      <div class="flex">
        <div class="flex-1">
          <span class="font-bold">
            <el-button @click="item.visibale = true" type="primary" text round>
              {{ item.title }}
            </el-button>
          </span>
        </div>
        <div class="flex-1">
          <span class="font-bold">{{ item.time }}</span>
        </div>
        <div class="flex-3">
          <span class="font-bold">{{ item.author }}</span>
        </div>
        <el-dialog
          v-model="item.visibale"
          title="{{ item.title }}"
          width="30%"
          :before-close="handleClose"
        >
          <span>{{ item.data }}</span>
          <template #footer>
            <span class="dialog-footer">
              <el-button type="primary" @click="item.visibale = false">
                Confirm
              </el-button>
            </span>
          </template>
        </el-dialog>
          
      </div>
    </div>
  </el-card>
  </div>
</template>

<script setup>
import { ElMessageBox } from '~/.nuxt/imports';

const handleClose = (done) => {
  ElMessageBox.confirm('Are you sure to close this dialog?')
    .then(() => {
      done();
    })
    .catch(() => {});
};

const Billboards = [
  {
    title: 'Event 1',
    time: '2021-05-09 15:23:25',
    author: 'admin',
    data: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sodales, quam quis dignissim sollicitudin, erat ligula placerat justo, at aliquet nisi ipsum vel diam. Sed erat lorem, accumsan malesuada fermentum at, pretium id leo. Suspendisse faucibus felis at justo efficitur egestas. Nulla sed bibendum dolor. In eget scelerisque velit. Curabitur eu semper orci. Pellentesque maximus, massa sit amet mattis malesuada, nulla mauris porttitor ex, et gravida nisl velit et massa. Ut aliquet, tortor viverra malesuada rutrum, erat erat ullamcorper ante, condimentum sagittis velit justo vel quam.",
    visibale: ref(false),
  },
  {
    title: 'please do test2 contest',
    time: '2021-05-07 15:23:25',
    author: 'admin',
    data: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sodales, quam quis dignissim sollicitudin, erat ligula placerat justo, at aliquet nisi ipsum vel diam. Sed erat lorem, accumsan malesuada fermentum at, pretium id leo. Suspendisse faucibus felis at justo efficitur egestas. Nulla sed bibendum dolor. In eget scelerisque velit. Curabitur eu semper orci. Pellentesque maximus, massa sit amet mattis malesuada, nulla mauris porttitor ex, et gravida nisl velit et massa. Ut aliquet, tortor viverra malesuada rutrum, erat erat ullamcorper ante, condimentum sagittis velit justo vel quam.",
    visibale: ref(false),
  }
]

</script>

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
