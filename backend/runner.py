import os,sys
import argparse

parser = argparse.ArgumentParser(description='A test program.')

parser.add_argument('--judge_file', type=str, default='judge.py',help="輸入要評判的檔案")
parser.add_argument('--complier', type=str, default='python3',help="輸入要評判的語言")
parser.add_argument('--input_file', type=str, default='in.txt',help="輸入要評判的測資")
parser.add_argument('--output_file', type=str, default='out.txt',help="輸入要作為比對的答案")
args = parser.parse_args()#骨幹

file_name = args.judge_file
complier = args.complier
input_file = args.input_file
output_file = args.output_file
recive_file = "recive.txt"

os.system(complier + " " + file_name + " < " + input_file + " > " + recive_file)
jud_result = "jud_result.txt"
os.system("diff " + recive_file + " " + output_file + " > " + jud_result)