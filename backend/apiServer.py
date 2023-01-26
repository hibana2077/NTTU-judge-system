'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2023-01-16 22:13:39
LastEditors: hibana2077 hibana2077@gmaill.com
LastEditTime: 2023-01-26 10:51:25
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
    id: str #user id + problem id + session id
    question_id: str #question id
    code: str #code
    language: str #language -> python3, node, ruby, c, cpp

class Judge():
    def __init__(self, id, code, language, judge_mode, time_limit, question_id):
        self.id = id
        self.code = code
        self.language = language
        self.judge_mode = judge_mode
        self.time_limit = time_limit
        self.question_id = question_id
    
    def judge(self):
        new_dir_path = f"./temp"
        if not os.path.exists(new_dir_path):
            os.mkdir(new_dir_path)
        os.chdir(new_dir_path)
        if self.language == "python3":
            os.system(f"echo {self.code} > {self.id}.py")
        elif self.language == "node":
            os.system(f"echo {self.code} > {self.id}.js")
        elif self.language == "ruby":
            os.system(f"echo {self.code} > {self.id}.rb")
        elif self.language == "c":
            os.system(f"echo {self.code} > {self.id}.c")
        elif self.language == "cpp":
            os.system(f"echo {self.code} > {self.id}.cpp")
        elif self.language == "lua":
            os.system(f"echo {self.code} > {self.id}.lua")
        elif self.language == "rust":
            os.system(f"echo {self.code} > {self.id}.rs")
        elif self.language == "go":
            os.system(f"echo {self.code} > {self.id}.go")

        
        


app = FastAPI()
mogodb_client = pymongo.MongoClient("mongodb://localhost:27017/")#先放在本地 之後看有沒有要放到雲端去

@app.get("/")
def read_root():
    return {"System": "NTTU Online Judge System"}

