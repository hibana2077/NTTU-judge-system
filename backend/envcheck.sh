#!/bin/bash

echo "檢查C++編譯器(g++)..."
if command -v g++ >/dev/null 2>&1; then
    echo "C++編譯器(g++)已安裝。"
    g++ --version | head -n 1
else
    echo "C++編譯器(g++)未安裝。"
fi

echo "檢查Node.js..."
if command -v node >/dev/null 2>&1; then
    echo "Node.js已安裝。"
    node --version
else
    echo "Node.js未安裝。"
fi

echo "檢查Python 3..."
if command -v python3 >/dev/null 2>&1; then
    echo "Python 3已安裝。"
    python3 --version
else
    echo "Python 3未安裝。"
fi

echo "檢查Rust..."
if command -v rustc >/dev/null 2>&1; then
    echo "Rust已安裝。"
    rustc --version
else
    echo "Rust未安裝。"
fi