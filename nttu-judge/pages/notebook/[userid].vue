<!--
 * @Author: hibana2077 hibana2077@gmaill.com
 * @Date: 2023-05-03 13:04:17
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2023-05-03 14:10:44
 * @FilePath: /NTTU-new-gen-judge-system/nttu-judge/pages/notebook/[userid].vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
    <el-container>
        <el-card style="display: flex; margin-top: 1.5%; margin-left: 5%; margin-right: 5%;">
            <el-button type="primary" :icon="CirclePlusFilled" size="small" style="margin-left: 1%; margin-right: 1%;">新增</el-button>
            <el-tabs type="border-card" style="margin-left: 1%; margin-right: 1%; margin-top: 2%;">
                <el-tab-pane v-for="(content, title) in note" :label="title" :name="title">
                    {{ content }}
                </el-tab-pane>
            </el-tabs>
        </el-card>
    </el-container>
</template>

<script setup>
//TODO: import CKEditor
import { CirclePlusFilled } from '@element-plus/icons-vue';


const route = useRoute()
const { userid } = route.params
//TODO: get user's notebook
const note = {
    "title 1":"content 1",
    "title 2":"content 2",
    "title 3":"content 3",
}
</script>