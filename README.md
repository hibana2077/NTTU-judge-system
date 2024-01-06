<!--
 * @Author: hibana2077 hibana2077@gmail.com
 * @Date: 2023-01-14 16:59:36
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2024-01-06 15:46:38
 * @FilePath: \NTTU-new-gen-judge-system\README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# Simple Online Judge System

![Nodejs](https://img.shields.io/badge/Nodejs-18.15.0-339933?style=plastic-square&logo=Node.js)
![docker](https://img.shields.io/badge/docker-20.10.8-2496ED?style=plastic-square&logo=docker)
![Svelte](https://img.shields.io/badge/Svelte-3.44.0-FF3E00?style=plastic-square&logo=Svelte)
![Tailwindcss](https://img.shields.io/badge/Tailwindcss-2.2.17-38B2AC?style=plastic-square&logo=Tailwind%20CSS)

## Introduction

This is a **Easy use** and **Easy deploy** , **Easy maintain** Online Judge System. Based on [Domjudge](https://www.domjudge.org/).

## Features

- [x] **Easy use** and **Easy deploy** , **Easy maintain**
- [ ] Modern UI

## Quick Start

Git clone this repo

```bash
git clone https://github.com/hibana2077/simple-oj.git
```

Run cgroup setup script

```bash
cd simple-oj
bash cgroup-setup.sh
```

Reboot your machine and run setup script

```bash
bash setup.sh
```

When the setup script is done, you can see the admin password in the terminal. You can use it to login to the admin page.

This application is running on port 8080. You can change type `http://{your ip}:8080` in your browser to see the application.

## Support OS

- [x] Ubuntu 22.04
- [x] Debian 12

## Reference

- [Domjudge](https://www.domjudge.org/)