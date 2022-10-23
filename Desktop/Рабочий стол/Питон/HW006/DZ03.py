'''Задайте список из вещественных чисел. Напишите программу, которая 
найдёт разницу между максимальным и минимальным значением дробной 
части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''

from functools import reduce

lst = [1.1, 1.2, 3.1, 5, 10.01]
# new_lst = []

# for i in range(len(lst)):
#     if type(lst[i]) == float:
#         new_lst.append(lst[i] % 1)

# print(round(max(new_lst) - min(new_lst), 3))

print(round(reduce(lambda a,b: a%1 if (a%1 > b%1) else b%1, lst) - reduce(lambda a,b: a%1 if (a%1 < b%1) else b%1, lst), 3))

