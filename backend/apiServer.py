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
import time
import psutil
import json
import subprocess
import sys
import uvicorn
import pymongo
import os
import base64

#---------------------const--------------------->
MONGO_DB_LOC = "mongodb://mongo:27017/"
#---------------------const---------------------<

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
    id: str #(user id + problem id + session id + time)Base56 -> 用來當檔案名稱
    problem_id: str #problem id
    code: str #code
    language: str #language -> python3, node, ruby, c, cpp

#---------------------model---------------------<

#---------------------function----------------->

def check_token_state(token:str):
    '''
    @description: 檢查token的狀態是否合法
    @param {token} -> token
    @return: dict{state:bool, error_code:int}
    '''
    db_client = pymongo.MongoClient(MONGO_DB_LOC)
    db = db_client["NTTU_Judge_System"]
    session_collection = db["session"]

    #取得session
    session = session_collection.find_one({"token":token})

def create_JWT_token():
    '''
    @description: 建立JWT token
    @param {*}
    @return: str
    '''
    random_str = os.urandom(24)
    return base64.b64encode(random_str).decode("utf-8")

def init_DB(db_loc:str,admin:str,admin_password:str,sessions:dict):
    '''
    @description: 初始化資料庫
    @param {db} -> mongodb client
    @param {admin} -> admin username
    @param {admin_password} -> admin password
    @param {sessions} -> session dict{"token":token,"user_id":user_id,"expire_time":expire_time}
    @return: None
    '''
    db_client = pymongo.MongoClient(db_loc)
    #create user collection
    db = db_client["NTTU_Judge_System"]
    user_collection = db["user"]
    user_collection.insert_one({"username": admin, "password": admin_password})
    #create session collection
    session_collection = db["session"]
    session_collection.insert_one(sessions)


#---------------------function-----------------<

#---------------------main--------------------->
#create a directory to store the runtimes 讓環境盡量乾淨
os.mkdir("runtime")
os.chdir("runtime")
                
#test
app = FastAPI()
mogodb_client = pymongo.MongoClient("mongodb://mongo:27017/")#先放在本地 之後看有沒有要放到雲端去 -> 最後用 docker 的 link 連接 所以要改成 mongodb://mongo:27017/

@app.get("/")
async def read_root():
    return {"System": "NTTU Online Judge System"}

@app.get("/doc")
async def read_doc():
    return {"doc": "This is a doc"}

@app.get("/doc/support")
async def read_support():
    '''
    @description: 支援的語言
    @param {*}
    @return: dict{support: list}
    '''
    return {"support": ["python3", "node", "ruby", "c", "cpp"]}

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
            expire_time = time.time() + 60 * 60 * 24 * 7 #一週後過期
            
        else:
            return {"status": "fail", "message": "password incorrect"}

@app.post("/api/submission")
async def submission(submit: Sumbit):
    '''
    @description: 提交程式碼並且執行評判
    @param {submit} -> id, problem_id, code, language
    @return: dict
    '''
    return {'state':'building'}

#---------------------main---------------------<

#---------------------server------------------->

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)#run on 8000 port

#---------------------server-------------------<