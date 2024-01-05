#!/bin/bash
###
 # @Author: hibana2077 hibana2077@gmail.com
 # @Date: 2023-11-09 10:52:11
 # @LastEditors: hibana2077 hibana2077@gmail.com
 # @LastEditTime: 2024-01-06 00:47:50
 # @FilePath: \work_2023_fall\stop_all.sh
 # @Description: This script should be run in sudo mode. 
 # It includes error handling and user prompts for critical actions with color-coded messages.
 # The script updates the source code, stops all containers, removes all containers, cleans up the Docker system, 
 # rebuilds and starts up containers. 
 # The script uses color-coded messages to indicate success or failure of each step.
###

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Version
VERSION="1.0.0beta"

# Variables
object_name=""
judge_host_num=0
api_secret=""

# Function to print a separator line
print_separator() {
  echo -e "${BLUE}--------------------------------------------------------------------------------${NC}"
}

clear

echo -e "${BLUE}

 _______ _____ _______  _____         _______       _____  _____
 |______   |   |  |  | |_____] |      |______      |     |   |  
 ______| __|__ |  |  | |       |_____ |______      |_____| __|  
                                                                

${NC}                                                                             
"
print_separator

echo -e "${YELLOW}Simple OJ Cgroup setup Script ${GREEN}v${VERSION}${NC}"

print_separator

# 檔案路徑
GRUB_FILE="/etc/default/grub"

# 檢查是否是使用了 cgroup v2 的現代發行版
if grep -q "systemd.unified_cgroup_hierarchy=0" "$GRUB_FILE"; then
    # 如果已經包含了 'systemd.unified_cgroup_hierarchy=0'，則只添加 'cgroup_enable=memory swapaccount=1'
    sudo sed -i "/GRUB_CMDLINE_LINUX_DEFAULT/c\GRUB_CMDLINE_LINUX_DEFAULT=\"cgroup_enable=memory swapaccount=1\"" "$GRUB_FILE"
else
    # 如果沒有包含，則添加兩個參數
    sudo sed -i "/GRUB_CMDLINE_LINUX_DEFAULT/c\GRUB_CMDLINE_LINUX_DEFAULT=\"cgroup_enable=memory swapaccount=1 systemd.unified_cgroup_hierarchy=0\"" "$GRUB_FILE"
fi

# 更新 GRUB 配置
sudo update-grub

# 重啟系統提示
echo -e "${GREEN}Please reboot your system to apply the changes.${NC}"

print_separator

echo -e "${GREEN}Successfully setup cgroup.${NC}"