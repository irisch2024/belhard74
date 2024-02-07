# Вывести первые N чисел кратные M и больше K
N = 5
M = 5
P = -6


i = k = P
while i != N:
    if k % M == 0 and k > P:
        print(k)
        i += 1
    k += 1



















