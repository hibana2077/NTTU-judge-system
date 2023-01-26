'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2023-01-25 14:01:52
LastEditors: hibana2077 hibana2077@gmaill.com
LastEditTime: 2023-01-25 14:02:14
FilePath: /NTTU-new-gen-judge-system/frontend/lab.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import streamlit_authenticator as stauth

hashed_passwords = stauth.Hasher('admin').generate()
print(hashed_passwords)