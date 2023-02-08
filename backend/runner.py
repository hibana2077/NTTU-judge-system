'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2023-01-25 10:29:35
LastEditors: hibana2077 hibana2077@gmaill.com
LastEditTime: 2023-02-08 22:41:30
FilePath: /NTTU-new-gen-judge-system/backend/database/runner.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os
import subprocess

class Judge():
    def __init__(self, id, code, language, judge_mode, time_limit, question_id,infile, outfile):
        self.id = id #submission id
        self.code = code #code
        self.language = language #language of code
        self.judge_mode = judge_mode #judge mode
        self.time_limit = time_limit #time limit
        self.question_id = question_id #question id
        self.infile = infile #輸入測資
        self.outfile = outfile #輸出測資

    def init_env(self):
        '''
        @description: 初始化環境
        @param {*}
        @return {*}
        '''
        os.mkdir(self.id)   
        os.chdir(self.id)
        os.mkdir("judge")
        os.chdir("judge")
        os.mkdir("code")
        os.chdir("code")
        self.code2file()
        os.chdir("..")
        os.chdir("..")


    def case2file(self, case):
        '''
        @description: 將測資寫入檔案
        @param {*}
        @return: 檔案名稱
        '''
        file_name = self.id + "_" + case + ".txt"
        localaciton = os.path.join(os.getcwd(), "judge", "case", file_name)
        with open(localaciton, "w") as f:
            f.write(self.infile)
        self.infile = file_name
        return file_name

    def ans2file(self, case_ans):
        '''
        @description: 將答案寫入檔案
        @param {*}
        @return: 檔案名稱
        '''
        file_name = self.id + "_" + case_ans + ".txt"
        localaciton = os.path.join(os.getcwd(), "judge", "case", file_name)
        with open(localaciton, "w") as f:
            f.write(self.outfile)
        self.outfile = file_name
        return file_name
    
    def clean_up(self):
        '''
        @description: 清理測資檔案
        @param {*}
        @return {*}
        '''
        self.del_file(self.infile)
        self.del_file(self.outfile)
        if self.language in ["c", "cpp"]:
            self.del_file(self.id)
            self.del_file(self.id + ".out")
    
    def finish(self):
        '''
        @description: 清理環境
        @param {*}
        @return {*}
        '''
        os.chdir("..")
        os.chdir("..")
        os.rmdir(self.id)
    
    def code2file(self):
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
            "cpp": "cpp",
            "rust": "rs"
        }
        file_name = self.id + "." + language_mapping[self.language]
        localaciton = os.path.join(os.getcwd(), "judge", "code", file_name)
        with open(localaciton, "w") as f:
            f.write(self.code)
        return file_name
    
    def del_file(self, file_name):
        '''
        @description: 刪除檔案
        @param {*}
        @return {*}
        '''
        localaciton = os.path.join(os.getcwd(), "judge", "code", file_name)
        os.remove(localaciton)
        return True
    
    def judge(self, file_name):
        '''
        @description: 判斷
        @param {*}
        @return: dict
        '''
        #judge_mode = 0 -> 寬鬆模式 -> 不考慮輸出格式，只要輸出正確就算正確
        #judge_mode = 1 -> 嚴格模式 -> 要考慮輸出格式，輸出格式錯誤就算錯誤
        if self.judge_mode:
            #按照語言進行編譯
            if self.language == "c":
                cmd = ["gcc","-o","/judge/code/"+self.id,"/judge/code/"+file_name,"&&","/judge/code/"+self.id,"<","/judge/data/"+self.infile,">","/judge/code/"+self.id+".out"]
            elif self.language == "cpp":
                cmd = ["g++","-o","/judge/code/"+self.id,"/judge/code/"+file_name,"&&","/judge/code/"+self.id,"<","/judge/data/"+self.infile,">","/judge/code/"+self.id+".out"]
            elif self.language == "python3":
                cmd = ["python3","/judge/code/"+file_name,"<","/judge/data/"+self.infile,">","/judge/code/"+self.id+".out"]
            elif self.language == "node":
                cmd = ["node","/judge/code/"+file_name,"<","/judge/data/"+self.infile,">","/judge/code/"+self.id+".out"]
            elif self.language == "ruby":
                cmd = ["ruby","/judge/code/"+file_name,"<","/judge/data/"+self.infile,">","/judge/code/"+self.id+".out"]
            elif self.language == "rust":
                cmd = ["rustc","/judge/code/"+file_name,"&&","/judge/code/"+self.id,"<","/judge/data/"+self.infile,">","/judge/code/"+self.id+".out"]#尚待測試
            else:
                return {"status": "error", "message": "language didn't support"}
            #執行編譯
        # diff -B -w --> 寬鬆模式
        # diff -i --> 嚴格模式
            try:
                subprocess.run(cmd, timeout=self.time_limit, check=True)
            except subprocess.TimeoutExpired:
                return {"status": "error", "message": "TLE"}
            except subprocess.CalledProcessError:
                return {"status": "error", "message": "RE"} #RE -> Runtime Error
            
            #執行diff

            cmd = ["diff","-B","-w","/judge/code/"+self.id+".out","/judge/data/"+self.outfile]

            resault = subprocess.run(cmd, timeout=10, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if resault.returncode == 0:
                return {"status": "success", "message": "AC"}
            else:
                return {"status": "error", "message": "WA"}
        else:
            #按照語言進行編譯
            if self.language == "c":
                cmd = ["gcc","-o","/judge/code/"+self.id,"/judge/code/"+file_name,"&&","/judge/code/"+self.id,"<","/judge/data/"+self.infile,">","/judge/code/"+self.id+".out"]
            elif self.language == "cpp":
                cmd = ["g++","-o","/judge/code/"+self.id,"/judge/code/"+file_name,"&&","/judge/code/"+self.id,"<","/judge/data/"+self.infile,">","/judge/code/"+self.id+".out"]
            elif self.language == "python3":
                cmd = ["python3","/judge/code/"+file_name,"<","/judge/data/"+self.infile,">","/judge/code/"+self.id+".out"]
            elif self.language == "node":
                cmd = ["node","/judge/code/"+file_name,"<","/judge/data/"+self.infile,">","/judge/code/"+self.id+".out"]
            elif self.language == "ruby":
                cmd = ["ruby","/judge/code/"+file_name,"<","/judge/data/"+self.infile,">","/judge/code/"+self.id+".out"]
            elif self.language == "rust":
                cmd = ["rustc","/judge/code/"+file_name,"&&","/judge/code/"+self.id,"<","/judge/data/"+self.infile,">","/judge/code/"+self.id+".out"]
            else:
                return {"status": "error", "message": "language didn't support"}
            
            #執行編譯
            try:
                subprocess.run(cmd, timeout=self.time_limit, check=True)
            except subprocess.TimeoutExpired:
                return {"status": "error", "message": "TLE"}
            except subprocess.CalledProcessError:
                return {"status": "error", "message": "RE"}
            
            #執行diff

            cmd = ["diff","-i","/judge/code/"+self.id+".out","/judge/data/"+self.outfile]

            resault = subprocess.run(cmd, timeout=10, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if resault.returncode == 0:
                return {"status": "success", "message": "AC"}
            else:
                return {"status": "error", "message": "WA"}
            

            