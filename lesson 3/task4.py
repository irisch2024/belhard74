# 3 числа, сказать сколько из них положительных и сколько отрицательных

a = 0
b = -267
c = -57

text = "Положительные"
qua_plus = 0
if a > 0: qua_plus += 1
if b > 0: qua_plus += 1
if c > 0: qua_plus += 1
print(text, qua_plus)

text = "Отрицательные"
qua_minus = 0
if a < 0: qua_minus += 1
if b < 0: qua_minus += 1
if c < 0: qua_minus += 1
print(text, qua_minus)
