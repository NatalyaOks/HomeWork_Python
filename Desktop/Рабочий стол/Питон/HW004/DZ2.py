'''2. Задайте натуральное число N. Напишите программу, которая составит список простых 
множителей числа N.'''

n = int(input('Введите число: '))
lst = []
i = 2
while i <= n:
    while n % i == 0:
        n = n / i
        lst.append(i)
    i += 1
print(lst)
