'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2023-09-17 13:19:39
LastEditors: hibana2077 hibana2077@gmaill.com
LastEditTime: 2023-09-17 13:21:18
FilePath: /NTTU-new-gen-judge-system/lab/pyyaml_test/lab.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import yaml
from pprint import pprint

file_loc = "lab.yaml"

data = dict()

with open(file_loc, 'r') as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

pprint(data)