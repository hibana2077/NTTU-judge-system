/*
 * @Author: hibana2077 hibana2077@gmaill.com
 * @Date: 2023-04-29 03:54:10
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2023-10-07 22:52:17
 * @FilePath: /NTTU-new-gen-judge-system/frontend/nuxt.config.ts
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    pages: true,
    modules: ['@nuxt/ui'],
    ui: {
        primary: 'green',
        gray: 'slate',
        notifications: {
            // Show toasts at the top right of the screen
            position: 'top-0 right-0'
        }
    }
  }) 