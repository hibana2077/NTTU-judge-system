'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2023-09-14 11:59:48
LastEditors: hibana2077 hibana2077@gmaill.com
LastEditTime: 2023-09-14 12:00:58
FilePath: /NTTU-new-gen-judge-system/test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
file_name = "test.txt"

#read file
with open(file_name, 'r') as f:
    lines = f.readlines()

#process
each_line = set(lines)

#write file
with open(file_name, 'w') as f:
    for line in each_line:
        f.write(line)