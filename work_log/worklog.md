
# 工作進度紀錄

## 2023/01/24

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