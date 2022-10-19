# 3.Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


from functools import reduce
list_1 = [1.1, 1.2, 3.1, 5, 10.01]
fractional_list = []

for i in list_1:
    if i != 0:
        fractional_list.append(round(i % 1, 2))

fractional_list.remove(0)

max_num_in_list_1 = reduce(lambda a,b: a if (a>b) else b, fractional_list)
min_num_in_list_1 = reduce(lambda a,b: a if (a<b) else b, fractional_list)
result = max_num_in_list_1 - min_num_in_list_1
print(result)


# fractional_list = []
# result = 0

# for i in list_1:
#     if i != 0:
#         fractional_list.append(round(i % 1, 5))

# max_fract = fractional_list[0]
# min_fract = fractional_list[0]

# for i in fractional_list:
#     if max_fract < i:
#         max_fract = i
#     if (min_fract > i and i > 0):
#         min_fract = i

# result = max_fract - min_fract
# print(f'{fractional_list} => {result}')
