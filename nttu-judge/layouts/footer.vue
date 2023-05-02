<script setup>
import { ref } from 'vue';

const year = ref(new Date().getFullYear());
</script>


<template>
    <el-footer class="font-semibold text-black-400">
        <div class="text-center">
            <span>Powered by
                <el-link href="https://github.com/hibana2077/NTTU-new-gen-judge-system" class="font-semibold text-black-400">
                    <div class="font-semibold text-black-400">
                        NTTUOJ
                    </div>
                </el-link>
                - {{ year }}
            </span>
        </div>
    </el-footer>
</template>