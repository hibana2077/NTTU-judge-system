'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2024-01-05 14:30:08
LastEditors: hibana2077 hibana2077@gmaill.com
LastEditTime: 2024-01-05 15:16:08
FilePath: /NTTU-judge-system/domjudge/modify.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import yaml

def judge_host_template(num:int,object_name:str,api_secret:str,origin_dict:dict):
    for i in range(num):
        temp_dict = {
            f"judgehost_{i+1}_{object_name}": {
                "container_name": f"judgehost_{i+1}_{object_name}",
                "image": "domjudge/judgehost:latest",
                "privileged": True,
                "hostname": f"judgedaemon_{i+1}",
                "volumes": [
                    "/sys/fs/cgroup:/sys/fs/cgroup:ro",
                ],
                "environment": [
                    "CONTAINER_TIMEZONE=Asia/Taipei",
                    f"DAEMON_ID={i}",
                    f"JUDGEDAEMON_PASSWORD={api_secret}",
                ],
                "links": [
                    f"domserver_{object_name}:domserver",
                ]
            }
        }
        origin_dict.update(temp_dict)
    return origin_dict