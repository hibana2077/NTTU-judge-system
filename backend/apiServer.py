'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2023-01-16 22:13:39
LastEditors: hibana2077 hibana2077@gmaill.com
LastEditTime: 2023-02-10 19:36:22
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

class User(BaseModel):
    username: str
    password: str

#session 要手動寫

class Sumbit(BaseModel):
    id: str #(user id + problem id + session id + time)Hash -> 用來當檔案名稱
    question_id: str #question id
    code: str #code
    language: str #language -> python3, node, ruby, c, cpp

#create a directory to store the runtimes
os.mkdir("runtime")
os.chdir("runtime")
                

app = FastAPI()
mogodb_client = pymongo.MongoClient("mongodb://localhost:27017/")#先放在本地 之後看有沒有要放到雲端去

@app.get("/")
def read_root():
    return {"System": "NTTU Online Judge System"}

#預留一個接口給前端做登入

#client -> server
@app.get("/api/login_data")
def login_data():
    '''
    @description: 取得登入資料
    @param {*}
    @return: dict
    '''
    