# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 09:07:37 2024

@author: student
"""

import random

# 創建包含問題和答案的字典
questions_dict = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What element does 'O' represent on the periodic table?": "Oxygen",
    "In what year did the Titanic sink?": "1912"
}

def select_random_items(dictionary, count):
    # 若選擇數量超出字典大小，則設定為字典大小
    count = min(count, len(dictionary))
    # 隨機選擇指定數量的項目
    selected_items = random.sample(dictionary.items(), count)
    return dict(selected_items)

# 選擇顯示的項目數量
num_items_to_display = 3

# 隨機選擇並顯示指定數量的項目
selected_questions = select_random_items(questions_dict, num_items_to_display)

# 格式化並顯示選擇的項目
for question, answer in selected_questions.items():
    print(f"{question}: {answer}")
