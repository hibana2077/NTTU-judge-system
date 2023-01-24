'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2023-01-24 15:45:34
LastEditors: hibana2077 hibana2077@gmaill.com
LastEditTime: 2023-01-24 17:14:15
FilePath: /NTTU-new-gen-judge-system/backend/database/lab.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

import pymongo

location = "mongodb://172.104.73.224:27017/"

client = pymongo.MongoClient(location)

print(client.list_database_names())

database = client.grade

print(database.list_collection_names())

# database.create_collection("question_pdf")

# print(database.list_collection_names())

import base64

with open("backend/database/test.pdf", "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

database.question_pdf.insert_one({"question_id": "1", "pdf": base64_pdf})

print(database.question_pdf.find_one({"question_id": "1"}))