#!/bin/bash
###
 # @Author: hibana2077 hibana2077@gmaill.com
 # @Date: 2023-06-17 11:17:06
 # @LastEditors: hibana2077 hibana2077@gmaill.com
 # @LastEditTime: 2023-06-19 13:50:50
 # @FilePath: /NTTU-new-gen-judge-system/backend/envcheck.sh
 # @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
### 
output_file="envcheck.txt"

echo "Checking C compiler (gcc)..."
if command -v gcc >/dev/null 2>&1; then
    echo "C compiler (gcc) is installed."
    gcc --version | head -n 1
    echo "gcc : $(gcc --version | head -n 1)" >> $output_file
else
    echo "C compiler (gcc) is not installed."
fi

echo "Checking C++ compiler (g++)..."
if command -v g++ >/dev/null 2>&1; then
    echo "C++ compiler (g++) is installed."
    g++ --version | head -n 1
    echo "g++ : $(g++ --version | head -n 1)" >> $output_file
else
    echo "C++ compiler (g++) is not installed."
fi

echo "Checking Node.js..."
if command -v node >/dev/null 2>&1; then
    echo "Node.js is installed."
    node --version
    echo "node : $(node --version)" >> $output_file
else
    echo "Node.js is not installed."
fi

echo "Checking Python 3..."
if command -v python3 >/dev/null 2>&1; then
    echo "Python 3 is installed."
    python3 --version
    echo "python3 : $(python3 --version)" >> $output_file
else
    echo "Python 3 is not installed."
fi

echo "Checking Rust..."
if command -v rustc >/dev/null 2>&1; then
    echo "Rust is installed."
    rustc --version
    echo "rustc : $(rustc --version)" >> $output_file
else
    echo "Rust is not installed."
fi
