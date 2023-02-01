
# 工作進度紀錄

## 2023/01/24

### 進度報告

- mongoDB
    - 初次使用docker運行mongoDB
    - 使用Linode的vm模擬辦公室的伺服器
    ```bash
    mkdir data
    cd data
    docker run --name db01 -v $(pwd)/data:/data/db -d -p 27017:27017 --rm mongo
    ```
    - 使用mongoDB compass連線到mongoDB
    - 使用pymongo連線到mongoDB，且確認資料存放方式。
    - 使用pymongo寫入資料
    - 程式碼紀錄位於`backend/database/lab.py`

### 新增事項

- 考慮到部署時，是直接拉官方的image，所以要加一個`database_setup.py`，用來建立資料庫的collection，並且建立一個admin帳號。以及在`docker-compose.yml`加入建立`database`資料夾。

## 2023/02/01

### 進度報告

- client.py
    - 透過`stauth`套件，完成不同身份的登入，並且將登入資訊存入`session`中。
    - 透過`session`，完成不同身份的頁面跳轉。
    - UX/UI 些微優化。