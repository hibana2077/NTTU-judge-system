#!/bin/bash
output_file="envcheck.txt"

echo "Checking output file ($output_file) existence..."
if [ -f $output_file ]; then
    echo "Output file ($output_file) exists. Removing it..."
    rm $output_file
fi

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

echo "Checking Go..."
if command -v go >/dev/null 2>&1; then
    echo "Go is installed."
    go version
    echo "go : $(go version)" >> $output_file
else
    echo "Go is not installed."
fi

echo "Checking Ruby..."
if command -v ruby >/dev/null 2>&1; then
    echo "Ruby is installed."
    ruby --version
    echo "ruby : $(ruby --version)" >> $output_file
else
    echo "Ruby is not installed."
fi

echo "Check done. See $output_file for details."
```