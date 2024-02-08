# Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число

a = float(input("Введите число: "))
t = str(input("Введите действие: "))
b = float(input("Введите число: "))

if t == "+":
    m = a + b
    print(m)

elif t == "-":
    (m) = a - b
    print(m)

elif t == "/":
    (m) = a / b
    print(m)

elif t == "*":
    (m) = a * b
    print(m)

else:
    print("Ошибка ввода")
