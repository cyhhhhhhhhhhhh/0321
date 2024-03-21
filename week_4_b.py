# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 08:39:18 2024

@author: student
"""

# 原始的元組
my_tuple = (1, 2, 3, 4, 5)

# 將元組轉換成列表
my_list = list(my_tuple)

# 向列表中添加新元素
my_list.append(6)
my_list.append(7)

# 將更新後的列表轉換回元組
updated_tuple = tuple(my_list)

print("更新後的元組:", updated_tuple)
