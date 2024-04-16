'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2024-01-05 14:30:08
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2024-04-17 00:19:29
FilePath: /NTTU-judge-system/domjudge/modify.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# 先docker-compose up -d -> docker exec -it domserver cat /opt/domjudge/domserver/etc/restapi.secret -> 

import yaml
import os
import sys

def read_yaml(path):
    with open(path, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data

def write_yaml(path, data):
    with open(path, 'w') as f:
        yaml.dump(data, f)

def judge_host_template(num:int,object_name:str,api_secret:str,origin_dict:dict):
    for i in range(num):
        temp_dict = {
            f"judgehost_{i+1}_{object_name}": {
                "container_name": f"judgehost_{i+1}_{object_name}",
                "image": "domjudge/judgehost:8.2.0",
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


# using pipeline as input
# python3 ./modify.py < startup {object_name}
if __name__ == '__main__':
    # startup {object_name}
    # judgehost {num} {object_name} {api_secret}
    input_text = input("")
    input_list= input_text.split(" ")
    command = ""
    object_name = ""
    num = 0
    api_secret = ""
    if len(input_list) == 2:
        command, object_name = input_list
    elif len(input_list) == 4:
        command, num, object_name, api_secret = input_list
        api_secret = api_secret.replace("\r","")
    print(command, object_name, num, api_secret)
    if command == "startup":
        # read yaml
        data = read_yaml('./temp.yaml')
        # change : 
        # mariadb -> mariadb_{object_name}
        #   container_name: mariadb_{object_name}
        # domserver -> domserver_{object_name}
        #   container_name: domserver_{object_name}
        #   links: [mariadb_{object_name}:mariadb]
        data['services'][f"mariadb_{object_name}"] = data['services'].pop("mariadb")
        data['services'][f'mariadb_{object_name}']['container_name'] = f"mariadb_{object_name}"
        data['services'][f"domserver_{object_name}"] = data['services'].pop("domserver")
        data['services'][f'domserver_{object_name}']['container_name'] = f"domserver_{object_name}"
        data['services'][f'domserver_{object_name}']['links'] = [f"mariadb_{object_name}:mariadb"]

        # save yaml
        write_yaml('./changed.yaml', data)
    elif command == "judgehost":
        # read yaml
        data = read_yaml('./changed.yaml')
        # change : 
        # judgehost_{num}_{object_name}
        #   container_name: judgehost_{num}_{object_name}
        #   hostname: judgedaemon_{num}
        #   environment: [DAEMON_ID={num}, JUDGEDAEMON_PASSWORD={api_secret}]
        #   links: [domserver_{object_name}:domserver]
        num = int(num)
        data['services'] = judge_host_template(num, object_name, api_secret, data['services'])
        # save yaml
        write_yaml('./changed.yaml', data)
    else:
        print("command error")
        sys.exit(0)