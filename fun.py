# age = input('Введите ваш возраст: ')
# if age >= 14:
#     print('Пожалуйста, предоставьте паспорт')
# else:
#     print('Пожалуйста, предоставьте свидетельство о рождении')

# num = int(input("Введите число: "))
# if num%2==0:
#     print('Число четное')
# else:
#     print('нечетное')

# year = int(input("введите год:"))
# if (year%4==0 and year%100!=0) or year%400==0:
#     print('год високосный')
# else:
#     print('Not')

# print('welcome to quizz')
# answer = input('Who is live in pineapple?\nanswer:').lower()
# if answer == 'sponge bob':
#     print(f'You are right! it is {answer}!')

#------M1U4---------------------------------------------
# a = int(input('Input first side: '))
# b = int(input('Input second side: '))
# c = int(input('Input third side: '))
# if a + b > c and a + c > b and b + c > a:
#     if a==b==c:
#         print("Треугольник равносторонний")
#     elif a==b or a==c or b==c:
#         print('Треугольник равнобедренный')
#     else:
#         print("Разносторонний")
# else:
#     print("Такой треугольник не возможен!")

# print('Добро пожаловать на сайт "Превысил или нет"')
# vehicle = int(input("Выберите:\n1 - если у вас машина\n2 - если мотоцикл\nВыбор:"))
# if vehicle == 2:
#     speed = int(input("Введите вашу скорость: "))
#     if speed>60:
#         print("Нарушение")
#     else:
#         print("Нет нарушения")
# elif vehicle == 1:
#     speed = int(input("Введите вашу скорость: "))
#     if speed>80:
#         print("Нарушение")
#     else:
#         print("Нет нарушения")
# else:
#     print("Данного траспорта ещё нет в системе, или, Вы, ввели не верный транспорт")

# month = input('please input month: ').lower()
# if month == "январь" or month == "март" or month == "май" or month == "июль" or month == "август" or month == "октябрь" or month == "декабрь":
#     print(f'В месяце {month.capitalize()} - 31 день')
# elif month == 'апрель' or month == 'июнь' or month == 'сентябрь' or month == 'ноябрь':
#     print(f'В месяце {month.capitalize()} - 30 дней')
# elif month == 'февраль':
#     print(f'В месяце {month.capitalize()} - 28 или 29 дней')
# else:
#     print(f'Слово: "{month}" не является месяцом!')

# day = input('Введите день недели:').lower()
# time = input("Введите время начала сеанса (в формате чч:мм): ")
# h = int(time.split(":")[0])
# count = int(input("Цена за 1 билет - 100\nВведите кол-во билетов: "))
# if day in ("понедельник", "вторник", "среда"):
#     if 7<h<12:
#         print(count*100-(count*100*0.3))
#     elif 12<=h<=17:
#         print(count*100-(count*100*0.1))
#     elif 18<=h<=23:
#         print(count*100+(count*100*0.15))

# elif day in ("четверг", "пятница", "суббота", "воскресенье"):
#     if 7<h<12:
#         print(count*100-(count*100*0.2))
#     elif 12<=h<=17:
#         print(count*100)
#     elif 18<=h<=23:
#         print(count*100+(count*100*0.25))

# print("Выберите напиток:")
# print("1 — Кофе")
# print("2 — Чай")
# print("3 — Сок")
# choice = input("Введите номер (1-3): ")
# if choice == '1':
#     sugar = input("Нужен сахар? (да/нет): ").lower()
#     if sugar == 'да':
#         print("Ваш заказ: кофе с сахаром")
#     elif sugar == 'нет':
#         print("Ваш заказ: кофе без сахара")
#     else:
#         print("Непонятный ответ про сахар")
# elif choice == '2':
#     print("Какой чай?")
#     print("1 — Чёрный")
#     print("2 — Зелёный")
#     tea_type = input("Выберите: ")
#     if tea_type == '1':
#         print("Ваш заказ: чай чёрный")
#     elif tea_type == '2':
#         print("Ваш заказ: чай зелёный")
#     else:
#         print("Неизвестный тип чая")
# elif choice == '3':
#     print("Выберите сок:")
#     print("1 — Апельсиновый")
#     print("2 — Яблочный")
#     print("3 — Томатный")
#     juice_type = input("Ваш выбор: ")
#     if juice_type == '1':
#         print("Ваш заказ: сок апельсиновый")
#     elif juice_type == '2':
#         print("Ваш заказ: сок яблочный")
#     elif juice_type == '3':
#         print("Ваш заказ: сок томатный")
#     else:
#         print("Такого сока нет")
# else:
#     print("Такого напитка нет в меню")

# print("Введите цифру месяца от 1 до 12 вклчительно.")
# month=int(input("Введите число месяца: "))
# day = int(input("Введите день месяца: "))
# if month in (1,2,12):
#     print(f"Ваша дата {day} относится к зиме")
# elif month in (3,4,5):
#     print(f"Ваша дата {day} относится к весне")
# elif month in (6,7,8):
#     print(f"Ваша дата {day} относится к лету")
# elif month in (9,10,11):
#     print(f"Ваша дата {day} относится к осени")
# else:
#     print("Вы ошиблись, такого номера месяца не существует")

# age = int(input('Введите возраст: '))
# rait = int(input("Введите рейтинг, где 1-G, 2-PG-13, 3-R, 4-NC-17\nВыбор: "))
# if rait == 1:
#     print('Просмотр фильма разрешен')
# elif rait == 2:
#     if age >= 13:
#         print("Просмотр фильма разрешен")
#     else:
#         print('sorry you are too young')
# elif rait in (3,4):
#     if age >= 18:
#         print("Просмотр фильма разрешен")
#     else:
#         print('sorry you are too young')
# else:
#     print('нет такого рейтинга')    

# if weter<14:
#     if 0 <= temp <= 15:
#         print("Температура комфортная")
#         if osadki == 1:
#             print('рекомендуется надеть теплую куртку, шапку и перчатки')
#         elif osadki == 2:
#             print('рекомендуется надеть легкую одежду и солнцезащитные очки')
#         elif osadki == 3:
#             print('следует взять зонт')
#         elif osadki == 4:
#             print('рекомендуется оставаться дома')
#         else:
#             print('No such command')
# BOOOOOOOORING

# i = 0
# summ = 0
# while i != -1:
#     summ += i
#     i = int(input('Число: '))
# print(summ)

# i = -1
# summ = 0
# count = 0
# while i != 0:
#     i = int(input('Число: '))
#     if i != 0:
#         count += 1
#         summ = summ+i
# print(summ/count)

# while True:
#     i = int(input('Введите число: '))
#     if i == -1:
#         break
#     print(f'Куб числа: {i**3}\nКвадрат числа: {i**2}')

# n = int(input('Введите число: '))
# a = 0
# i = 1
# while True:
#     if n % i == 0:
#         a += 1
#     i+=1
#     if i > n:
#         break
# print(f"У вас {a} делителей")    

# n = int(input('Введите число: '))
# a = 2
# i = 2
# while True:
#     if n % i == 0:
#         a=i
#         break
#     i+=1
#     if i > n:
#         break
# print(f"Ваше число {a}")  

# a = 0
# the = 0 
# i = 0
# text = input('Текст: ').lower()
# text = text.split()
# while i < len(text):
#     if 'a' == text[i]:
#         a+=1
#     if 'the' == text[i]:
#         the+=1
#     i+=1
# print(f'{a} а повторений\n{the} the повторений')

# n = int(input('Введите число: '))
# i=1
# while i <= n:
#     print('*'*i)
#     i+=1

# n = int(input('Введите число: '))
# i=n-1
# x=0
# while i>1:
#     if n % i == 0:
#         x+=1
#     i-=1
# if x == 0:
#     print('простое')
# else:
#     print('не простое')

# t = input("введите слово: ")
# x = 0
# a=True
# while x <= len(t)-1:
#     if t[len(t)-1-x] != t[x]:
#         a=False
#         break
#     x+=1
# if a:
#     print('полиндром')
# else:
#     print("нет")

#----------------- M2U2 -----------------------------------------------
# n = int(input("число н (кол-во звезд): "))
# a = int(input("число a: "))
# for i in range(a):
#     print('*'*n)

# fak = 1
# n = int(input("Введите число: "))
# for i in range(1,n+1):
#     fak *= i
# print(fak)

# search = input('Искомый символ: ')
# text = input('Ваша строка: ').lower()
# count = 0
# for i in text:
#     if search == i:
#         count += 1
# if count >= 1:
#     print(f'Символ "{search}" повторился {count} раз!')
# else:
#     print('Повторений нуль')
#______________________________________________________
#____________ m2u3 ____________________________________

# symbol = input('Введите символ: ')
# base = int(input("Введите основание: "))
# height = int(input("Введите высоту: "))
# step = base // height  # шаг, сколько символов добавляем на строку
# for i in range(1, height + 1):
#     for j in range(step * i):
#         print(symbol, end='')
#     print()

# def lesser_of_two_evens(x, y):
#     if x % 2 == 0 and y % 2 == 0:
#         return min(x, y)
#     return max(x, y)
# print(lesser_of_two_evens(2,4))
# # проверка
# print(lesser_of_two_evens(2,5))

# def animal_crackers(text):
#     words = text.split()
#     return words[0][0].lower() == words[1][0].lower()
# # проверка
# print(animal_crackers('Levelheaded Llama'))
# # проверка
# print(animal_crackers('Crazy Kangaroo'))

def makes_twenty(n1,n2):
    return n1==20 or n2==20 or n1+n2==20
# проверка
print(makes_twenty(10,10))
# проверка
print(makes_twenty(2,3))




