/*
 * @Author: hibana2077 hibana2077@gmaill.com
 * @Date: 2024-01-05 15:16:59
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2024-01-05 15:38:55
 * @FilePath: /NTTU-judge-system/frontend/tailwind.config.cjs
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
/** @type {import('tailwindcss').Config}*/
const config = {
  content: ['./src/**/*.{html,js,svelte,ts}', './node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}'],

  plugins: [require('flowbite/plugin')],

  darkMode: 'class',

  theme: {
    extend: {
      colors: {
        // flowbite-svelte
        primary: {
          '50': '#eff4fe',
          '100': '#e1ebfe',
          '200': '#c9d8fc',
          '300': '#a8bff9',
          '400': '#859bf4',
          '500': '#6879ec',
          '600': '#4b52e0',
          '700': '#4347c7',
          '800': '#34399f',
          '900': '#31367e',
          '950': '#1d2049',
        }
      }
    }
  }
};

module.exports = config;