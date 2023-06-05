/*
 * @Author: hibana2077 hibana2077@gmaill.com
 * @Date: 2023-06-05 10:18:50
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2023-06-05 10:28:17
 * @FilePath: /NTTU-new-gen-judge-system/lab/script/nodetest.js
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
function input() {
    return require('fs').readFileSync('/dev/stdin', 'utf8').trim();
} 
function print(x) {
    console.log(x);
}

function main() {
    print(input());
}

main();
//run fllow command to test
//node nodetest.js < test.txt