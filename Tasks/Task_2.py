# 3 Задать список из n чисел последовательности (1+1/n)**n и вывести на экран их сумму

# n = int(input("Введите натуральное число n "))
# res = []
# sum = 0

# for i in range(1, n+1):
#     res.append(round(((1+1/i)**i),2))
#     sum+=res[i-1]

# print(res[0:(len(res))])
# print(f'Сумма всех чисел: {round(sum,2)}')



n = int(input("Введите натуральное число n "))
res = [(1+1/i)**i for i in range(1, n+1)]
print(f'Сумма всех чисел: {round(sum(res),2)}')