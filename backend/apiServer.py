'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2023-01-16 22:13:39
LastEditors: hibana2077 hibana2077@gmaill.com
LastEditTime: 2023-06-05 11:41:10
FilePath: /NTTU-new-gen-judge-system/backend/apiServer.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from fastapi import FastAPI
from pydantic import BaseModel
from runner import Judge
import subprocess
import sys
import uvicorn
import pymongo
import os
import base64

#---------------------model--------------------->

class User(BaseModel):
    username: str
    password: str

#session 要手動寫

class session(BaseModel):
    id: str
    user_id: str
    start_time: str
    end_time: str

class Sumbit(BaseModel):
    id: str #(user id + problem id + session id + time)Hash -> 用來當檔案名稱
    question_id: str #question id
    code: str #code
    language: str #language -> python3, node, ruby, c, cpp

#---------------------model---------------------<

#---------------------function----------------->

def create_JWT_token():
    '''
    @description: 建立JWT token
    @param {*}
    @return: str
    '''
    random_str = os.urandom(24)
    return base64.b64encode(random_str).decode("utf-8")

#create a directory to store the runtimes
os.mkdir("runtime")
os.chdir("runtime")
                
#test
app = FastAPI()
mogodb_client = pymongo.MongoClient("mongodb://localhost:27017/")#先放在本地 之後看有沒有要放到雲端去

@app.get("/")
async def read_root():
    return {"System": "NTTU Online Judge System"}

@app.get("/doc/support")
async def read_support():
    return {"support": "python3, node, rust, c, cpp"}

#預留一個接口給前端做登入
@app.post("/api/vue_login")
async def vue_login(user: User):
    '''
    @description: 前端登入
    @param {user} -> username, password
    @return: dict
    '''
    db = mogodb_client["user"]
    collection = db["user"]
    user_data = collection.find_one({"username": user.username})
    if user_data == None:
        return {"status": "fail", "message": "user not found","code":"004"}#沒找到直接回傳錯誤
    else:
        if user_data["password"] == user.password:
            #正確後建立JWT token 存放在session跟DB
            token = create_JWT_token()
            
        else:
            return {"status": "fail", "message": "password incorrect"}

#client -> server
@app.get("/api/login_data")
def login_data():
    '''
    @description: 取得登入資料
    @param {*}
    @return: dict
    '''
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)