# Вывести первые N чисел кратные M и больше K
N = 5
M = 3
K = -5
a = [0, N+1]
N += 1
for i in a:
    if i % M == 0 or i > K:
        print(i)