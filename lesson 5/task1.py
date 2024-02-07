# Вывести первые N чисел кратные M и больше K
N = 5
M = 3
K = -5

for i in range(K, 1000):
    if i % M == 0 and i > K:
        print(i)






