echo "install c++ compiler"
apt-get install g++
echo "install nodejs"
apt-get install nodejs
echo "install python3"
apt-get install python3
apt-get install python3-pip
echo "install rust"
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
echo "install done!"