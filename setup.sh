#!/bin/bash
###
 # @Author: hibana2077 hibana2077@gmail.com
 # @Date: 2023-11-09 10:52:11
 # @LastEditors: hibana2077 hibana2077@gmaill.com
 # @LastEditTime: 2024-01-05 16:34:24
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

echo -e "${YELLOW}Project Start up Script ${GREEN}v${VERSION}${NC}"

print_separator

echo -e "${YELLOW}Checking for necessary dependencies...${NC}"

# Check if docker, docker-compose, requirements.txt exist

# Check if docker exists, yes->continue, no->install
if ! [ -x "$(command -v docker)" ]; then
  echo -e "${RED}Error: docker is not installed.${NC}" >&2
  echo -e "${YELLOW}Installing docker...${NC}"
  curl -sSL https://get.docker.com | sh
  echo -e "${GREEN}Successfully installed docker.${NC}"
else
  echo -e "${GREEN}docker is installed.${NC}"
fi

# Check if docker-compose exists, yes->continue, no->install
if ! [ -x "$(command -v docker-compose)" ]; then
  echo -e "${RED}Error: docker-compose is not installed.${NC}" >&2
  echo -e "${YELLOW}Installing docker-compose...${NC}"
  sudo apt install docker-compose
  echo -e "${GREEN}Successfully installed docker-compose.${NC}"
else
  echo -e "${GREEN}docker-compose is installed.${NC}"
fi

# Check if requirements.txt exists, yes->install, no->continue
if [ -f "requirements.txt" ]; then
  echo -e "${YELLOW}Installing python dependencies...${NC}"
  sudo pip3 install -r requirements.txt
  echo -e "${GREEN}Successfully installed python dependencies.${NC}"
else
  echo -e "${GREEN}requirements.txt does not exist.${NC}"
fi

print_separator

echo -e "${YELLOW}Start to start up the project...${NC}"

sudo docker-compose up --build -d || { echo -e "${RED}docker-compose up failed${NC}" ; exit 1; }

print_separator

echo -e "${GREEN}Successfully started up the project.${NC}"