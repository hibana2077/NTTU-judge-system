import os
import time
import sys
import subprocess
import argparse

parser = argparse.ArgumentParser(description='A test program.')

parser.add_argument('--judge_file', type=str, default='judge.py',help="輸入要評判的檔案")
parser.add_argument('--complier', type=str, default='python3',help="輸入要評判的語言")
parser.add_argument('--input_file', type=str, default='in.txt',help="輸入要評判的測資")
parser.add_argument('--output_file', type=str, default='out.txt',help="輸入要作為比對的答案")
parser.add_argument('--judge_mode', type=str, default='loose',help="輸入評判模式：loose or strict")
parser.add_argument('--time_limit', type=int, default=2,help="輸入時間限制")
args = parser.parse_args()#骨幹

file_name = args.judge_file
complier = args.complier
input_file = args.input_file
output_file = args.output_file
recive_file = "recive.txt"

if complier in ["python3","node","ruby"]:
    os.system(f"{complier} {file_name} < {input_file} > {recive_file}")
    os.system(f"diff {recive_file} {output_file} > jud_result.txt")
elif complier in ["c","cpp"]:
    os.system(f"g++ -o {file_name}.out {file_name} && ./{file_name}.out < {input_file} > {recive_file}")
    os.system(f"diff {recive_file} {output_file} > jud_result.txt")

if args.judge_mode == "loose":
    diff_out = open("jud_result.txt","r").read()
    if diff_out == "" or "No newline at end of file" in diff_out:
        print("AC")
    else:
        print("WA")
elif args.judge_mode == "strict":
    diff_out = open("jud_result.txt","r").read()
    if diff_out == "":
        print("AC")
    else:
        print("WA")