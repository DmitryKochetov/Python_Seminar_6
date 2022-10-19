
# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача -
# сформировать файл, содержащий сумму многочленов.

# 4x^2+2x+5
# 6x^2+4x+8


# with open('file_task5_1.txt', 'r') as f:
#     line_1 = f.readline()
# with open('file_task5_2.txt', 'r') as f:
#     line_2 = f.readline()

line_1 = '4x^2+2x+5'
line_2 = '6x^2+4x+8'
list_1 = list(filter(lambda x: x.isdigit(), line_1))
list_2 = list(filter(lambda x: x.isdigit(), line_2))
list_1.pop(1)
list_2.pop(1)
list_res = list(map(lambda x,y: int(x) + int(y), list_1, list_2))

result = str(list_res[0]) + 'x^2+' + str(list_res[1]) + 'x+' + str(list_res[2])
print(result)


# with open('file_task5_3.txt', 'w') as f:
#     f.write(result)
# f.close()