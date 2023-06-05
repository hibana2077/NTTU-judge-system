#!/bin/bash

output_file="envcheck.txt"

echo "檢查C編譯器(gcc)..."
if command -v gcc >/dev/null 2>&1; then
    echo "C編譯器(gcc)已安裝。"
    gcc --version | head -n 1
    "gcc : $(gcc --version | head -n 1)" >> $output_file
else
    echo "C編譯器(gcc)未安裝。"
fi

echo "檢查C++編譯器(g++)..."
if command -v g++ >/dev/null 2>&1; then
    echo "C++編譯器(g++)已安裝。"
    g++ --version | head -n 1
    "g++ : $(g++ --version | head -n 1)" >> $output_file
else
    echo "C++編譯器(g++)未安裝。"
fi

echo "檢查Node.js..."
if command -v node >/dev/null 2>&1; then
    echo "Node.js已安裝。"
    node --version
    "node : $(node --version)" >> $output_file
else
    echo "Node.js未安裝。"
fi

echo "檢查Python 3..."
if command -v python3 >/dev/null 2>&1; then
    echo "Python 3已安裝。"
    python3 --version
    "python3 : $(python3 --version)" >> $output_file
else
    echo "Python 3未安裝。"
fi

echo "檢查Rust..."
if command -v rustc >/dev/null 2>&1; then
    echo "Rust已安裝。"
    rustc --version
    "rustc : $(rustc --version)" >> $output_file
else
    echo "Rust未安裝。"
fi