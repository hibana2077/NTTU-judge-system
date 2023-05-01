<!--
 * @Author: hibana2077 hibana2077@gmaill.com
 * @Date: 2023-01-24 17:15:14
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2023-05-01 15:35:02
 * @FilePath: /NTTU-new-gen-judge-system/work_log/worklog.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->

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
- 然後`session`真是個好東西，可以用來存放登入資訊，並且可以在不同的頁面之間傳遞資訊。

## 2023/05/01

### 進度報告

- 把前端streamlit換成nuxt.js,因為streamlit的功能太少了，而且不太好用。
- 使用docker-compose建立一個stack，裡面包含了mongoDB,backend,frontend，並且驗證了內部網路可以互通。 -> lab/connect_test