# Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число

a = float(input("Введите число: "))
с = str(input("Введите действие: "))
b = float(input("Введите число: "))

if с == "+":
    m = a + b
    print(m)

elif с == "-":
    m = a - b
    print(m)

elif с == "/":
    m = a / b
    print(m)

elif с == "*":
    m = a * b
    print(m)

else:
    print("Неверные данные")










