/*
 * @Author: hibana2077 hibana2077@gmail.com
 * @Date: 2023-04-27 17:57:53
 * @LastEditors: hibana2077 hibana2077@gmail.com
 * @LastEditTime: 2023-05-01 20:36:43
 * @FilePath: \NTTU-new-gen-judge-system\backend\runner.cpp
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */


#include <iostream>
#include <map>
#include <string>


using ll = long long;
using ins_mp = std::map<std::string, std::string>;

ins_mp compile = {
    {"cpp","g++ %s -o out"},
    {"c","gcc %s -o out"}
};

/*
format:
./runner lang=cpp sourcefile=main.cpp inputfile=input.txt outputfile=output.txt
*/

ins_mp util_map = {
    {"envcheck","./envcheck.sh"},
};

ins_mp run = {
    {"cpp","./out "},
    {"c","./out"},
    {"py","python3 %s < %s > %s"},//python3 sourcefile < inputfile > outputfile
    {"js","nodejs %s < %s > %s"}
};

std::string run_compile(std::string lang, std::string sourcefile){
    std::string cmd = compile[lang];
    cmd.replace(cmd.find("%s"), 2, sourcefile);
    system(cmd.c_str());
    return cmd;
}

int main(int argc, char *argv[])
{
    std::map<std::string, std::string> args;
    if (argc == 0){
        std::cout << "no args" << std::endl;
        return 1;
    }else{
        
        for (int i = 1; i < argc; ++i){
            std::string arg = argv[i];
            std::string key = arg.substr(0, arg.find("="));
            std::string value = arg.substr(arg.find("=") + 1);
            args[key] = value;
        }
    }

    return 0;
}