/*
 * @Author: hibana2077 hibana2077@gmail.com
 * @Date: 2023-04-28 14:52:16
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2023-05-01 11:37:36
 * @FilePath: \NTTU-new-gen-judge-system\backend\lab.cpp
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>

using namespace std;

const std::string check_has_env(std::string lang){
    std::string cmd = "which " + lang + " > temp.txt";
    system(cmd.c_str());
    std::cout << std::ifstream("temp.txt").rdbuf();
    if(!ifstream("temp.txt")){
        return "no";
    }else{
        return "yes";
    }
    return "no";
}

int main(){
    // std::cout << check_has_env("g++") << std::endl;
    std::cout << check_has_env("rust") << std::endl;
    return 0;
}