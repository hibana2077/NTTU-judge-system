echo "regulate apt update"
apt-get update
echo "install vim curl git"
apt-get install -y vim curl git
echo "install c compiler"
apt-get install -y gcc
echo "install c++ compiler"
apt-get install -y g++
echo "install nodejs"
apt-get install -y nodejs
echo "install python3"
apt-get install -y python3
apt-get install -y python3-pip
echo "install done!"