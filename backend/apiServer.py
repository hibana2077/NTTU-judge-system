'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2023-01-16 22:13:39
LastEditors: hibana2077 hibana2077@gmaill.com
LastEditTime: 2023-02-01 18:08:05
FilePath: /NTTU-new-gen-judge-system/backend/apiServer.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
import sys
import uvicorn
import pymongo
import os

class User(BaseModel):
    username: str
    password: str

class Sumbit(BaseModel):
    id: str #(user id + problem id + session id + time)Hash -> 用來當檔案名稱
    question_id: str #question id
    code: str #code
    language: str #language -> python3, node, ruby, c, cpp

#create judge temp dir
if not os.path.exists("judge"):
    os.mkdir("judge")
    os.mkdir("judge/code")
elif not os.path.exists("judge/code"):
    os.mkdir("judge/code")
else:
    pass

class Judge():
    def __init__(self, id, code, language, judge_mode, time_limit, question_id):
        self.id = id
        self.code = code
        self.language = language
        self.judge_mode = judge_mode
        self.time_limit = time_limit
        self.question_id = question_id
    
    def to_file(self):
        '''
        @description: 將code寫入檔案
        @param {*}
        @return: 檔案名稱
        '''
        language_mapping = {
            "python3": "py",
            "node": "js",
            "ruby": "rb",
            "c": "c",
            "cpp": "cpp"
        }
        file_name = self.id + "." + language_mapping[self.language]
        localaciton = os.path.join(os.getcwd(), "judge", "code", file_name)

        
        


app = FastAPI()
mogodb_client = pymongo.MongoClient("mongodb://localhost:27017/")#先放在本地 之後看有沒有要放到雲端去

@app.get("/")
def read_root():
    return {"System": "NTTU Online Judge System"}

