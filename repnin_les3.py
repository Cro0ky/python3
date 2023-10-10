#task1
# a = int(input('A: '))
# b = int(input('B: '))

# for i in range(a,b+1):
#     print(i)
# print('forend')

#task2
# a = int(input('A: '))
# b = int(input('B: '))
# if b > a:
#     for i in range(a, b+1):
#         print(i)
# else:
#     for i in range(a, b-1, -1):
#         print(i)

#task3
# n = int(input('n'))
# sum = 0

# for i in range(n):
#     sum += int(input())
#     print(sum)

#task 4
# c = 1
# num = int(input('num'))
# for i in range(1, num + 1):
#     c *= i
#     print(c)


#task 5
# n = int(input('n'))
# if n < 10 and n > 0:
#     for i in range(1, n+1):
#         print(str(i) * i)
# else:
#     print('число не в диапозоне от 1 до 9')

#task 6 squarelist
# n = int(input())
# i = 1
# while i <= n:
#      print(f'{i} в квадрате :{i **2}')
#      i += 1


# task
# n = int(input('n'))
# st = 0
# k = 1
# while k <= n//2:
#     st += 1
#     k += 2
#     print(st, k)

# #task 8
# x = int(input())
# y = int(input())
# day = 1
# while x < y:
#     x += 0.1*x
#     day += 1
# print(day)

#task 9
# d = 0
# i = int(input())
# while i != 0:
#     i = int(input())
#     d += 1
# print(d)

#task 10
# n = int(input())
# x0 = 0
# x1 = 1
# for i in range(n-1):
#     x2 = x1 + x0
#     x1, x0 = x2, x1
#     print(x2)

#task12
# a = [1,2,3,4,5,6]
# print(a[::2])

#task13
# a = [3,2,1,4,67,3,]
# print(sorted(a))

#task 14

# a = [2,6,4,5,7]
# print(max(a))


#task 15
# hieght = [179 , 178, 165, 163, 150]
# petyaHight = 165
# hieght.append(petyaHight)
# hieght.sort()
# print(hieght)
# print(hieght.index(petyaHight) + 1)

#task 16
# a = [1,2,4,54,6,7,8]
#
# for i in a:
#     if i % 2 == 0 and i == 0:
#         a[i], a[i + 1] = a[i + 1], a[i]
#     elif i % 2 == 1:
#         continue
# print(a)

#task 17
# a = [1,2,4,54,6,7,8]
#
# for i in a:
#     x2 = a.index(min(a))
#     x1 = a.index(max(a))
#     a[x2], a[x1] = a[x1], a[x2]
# print(a)
#task 18
# k = int(input('Введите индекс для удаления: '))
# list = [1,2,4,54,6,7,8]
#
# for i in list:
#     if i == k:
#         k = list.pop(k)
#         y = list.pop()
#
# print(list)


