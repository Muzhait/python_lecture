# print(5, 8, 6)

# n = 1.89
# print(n)

#  n = 'hhggff'
#  print(n)

"""
n = 'g"gg"f'
print(n)
"""

# a = 5
# b = 5.17
# c = 'hello'

# print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a,b,c))

# print('Введите первое число: ')
# a = input()

# b = input('Введите второе число: ')

# a = input('Введите первое число: ')
# b = input('Введите второе число: ')
# a = int(a)
# b = int(b)

# print(a, '+', b, '=', a + b)

# a = 5.8895
# b = 4.59687
# print(round(a*b, 2))

# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter *5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5 (целочисленное деление)
# iter %= 5 # iter = iter %  5 (остаток от деления)
# iter **= 5 # iter = iter ** 5 (возведение в степень)

# a = 1 > 4
# print(a) # False

# a = 1 < 4 and 5 > 2
# print(a) # True

# a = 1 == 2
# print(a) # False

# a = 1 != 2
# print(a) # True

# a = 'qwe'
# b = 'qwe'
# print(a == b) # True

# a = 1 < 3 < 5 < 10
# print (a) # True

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)


# n = int(input())
# if n % 2 == 0 and n % 3 == 0:
# print('Число кратно 6')
# if n % 5 == 0 and n % 3 == 0:
# print('Число кратно 15')

# n = 4023
# summa = 0
# while summa > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa) # 9

# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(i)


# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1


# r = range(5) # 0 1 2 3 4
# r = range(2, 5) # 2 3 4
# r = range(-5, 0) # ----
# r = range(1, 10, 2) # 1 3 5 7 9
# r = range(100, 0, -20) # 100 80 60 40 20
# r = range(100, 0, -20) # range(100, 0, -20)
# for i in r:
#     print(i)
# # 100 80 60 40 20

# a = 'qwerty'

# for i in a:
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.lower()) # съешь ещё этих мягких французских булок
# print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
# print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок


# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # съешь ещё этих мягких французских булок
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...
