# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 08:42:27 2024

@author: student
"""

import random

def guess_number():
    # 產生一個隨機數字
    secret_number = random.randint(1, 100)
    
    while True:
        # 輸入猜測的數字
        guess = int(input("請猜一個1到100之間的整數："))
        
        # 檢查猜測的數字是否正確
        if guess == secret_number:
            print("恭喜你猜對了！")
            break
        elif guess < secret_number:
            print("猜的太低了，請再試一次。")
        else:
            print("猜的太高了，請再試一次。")

# 呼叫函式開始猜數字遊戲
guess_number()
99