# print("Hi, PyCharm")
# x = 43
# y = 32
# print(x*y)
# print("End line")

# name = input("Введите ваше имя: ")
# if name == "Urban":
#     print("Здравствуйте, администратор")
# if name == "Roman":
#     print("Здравствуйте, студент")
# else:
#     print("Привет", name)

# number = int(input("Ведите число: ")) #Fizz, Buzz, FizzBuss
# if number % 3 == 0 and number % 5 == 0:  # and строгий оператор, or не строгий  ("И" и "ИЛИ")
#     print("FizzBuzz")
# elif number % 3 == 0:
#     print("Fizz")
# elif number % 5 == 0:
#     print("Buzz")
# else:
#     print("Число не подходит")

first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))
if first == second and first == third:
    print(3)
elif first == second or first == third:
    print(2)
elif second == third:
    print(2)
else:
    print(0)
