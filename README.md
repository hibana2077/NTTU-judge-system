<!--
 * @Author: hibana2077 hibana2077@gmail.com
 * @Date: 2023-01-14 16:59:36
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2023-01-16 22:35:45
 * @FilePath: \NTTU-new-gen-judge-system\README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# NTTUjudge 台東大學程式設計評判系統

![python](https://img.shields.io/badge/python-3.10-blue?style=plastic-square&logo=python)
![streamlit](https://img.shields.io/badge/streamlit-1.14.0-FF4B4B?style=plastic-square&logo=streamlit)
![fastapi](https://img.shields.io/badge/fastapi-0.85.1-009688?style=plastic-square&logo=fastapi)
![mongodb](https://img.shields.io/badge/mongodb-4.4.6-47A248?style=plastic-square&logo=mongodb)
![docker](https://img.shields.io/badge/docker-20.10.8-2496ED?style=plastic-square&logo=docker)
![Guvicorn](https://img.shields.io/badge/Guvicorn-0.19.0-499848?style=plastic-square&logo=Gunicorn)

## 介紹

NTTUjudge 是一個簡單的程式設計評判系統，使用者可以在網頁上編輯程式碼，並且在網頁上即時看到程式的執行結果。

本系統使用 [streamlit](https://streamlit.io/) 作為前端，使用 [fastapi](https://fastapi.tiangolo.com/) 作為後端，使用 [mongodb](https://www.mongodb.com/) 作為資料庫。

## 技術架構

### 前端

- streamlit
    - streamlit-auth
    - requests

### 後端

- fastapi
    - uvicorn
    - pymongo
    - requests
    - pydantic

### 資料庫

- mongodb

## 工作流程

### 前端

1. 使用者在網頁上編輯程式碼
2. 使用者按下執行按鈕
3. 前端將程式碼傳送到後端
4. 後端將程式碼傳送到 runner
5. runner 執行程式碼
6. runner 回傳執行結果給後端
7. 後端將執行結果傳送到前端。

### 後端

#### API

- /login
    - POST
        - username
        - password
    - GET
        - username
        - password

- /problem
    - POST
        - submit_code -> call runner
    - GET
        - problem_id
        - excute_result

- /scoreboard
    - GET
        - problem_states

- /group_discussion
    - POST
        - message
    - GET
        - messages

- /admin
    - POST
        - problem_detail
    - GET
        - problem_detail

#### runner

執行程式碼，並且回傳執行結果。


## Docker compose 功能

### 啟動

1. 啟動 mogoDB image port:207701
2. 啟動 後端 image port:207702 -> 如果覺得太慢 可以改成Load balancer 架構
3. 啟動 前端 image port:80 -> No ssl -> 考慮跟老師建議使用 streamlit share -> 穩定度高