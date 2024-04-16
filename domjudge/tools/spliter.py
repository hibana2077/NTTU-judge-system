'''
Author: hibana2077 hibana2077@gmail.com
Date: 2024-04-16 23:10:56
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2024-04-16 23:32:52
FilePath: \simple-oj\domjudge\tools\spliter.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
data:list[str] = list()
while True:
    try:
        data.append(input())
    except EOFError:
        print(data[-1].split()[-1])
        break