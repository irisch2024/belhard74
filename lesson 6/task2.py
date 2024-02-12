# Дан список чисел, необходимо для каждого элемента посчитать сумму его соседей,
# для крайних чисел одним из соседей является число с противоположной стороны списка

# a=[1, -35, 12, 103, -59, -5, 7, -13]
line = input("Введите список целых чисел, разделённых пробелами: ")
numbers = list(map(int, line.split()))
if len(numbers) == 1:
    print(numbers[0])
else:
    neighbours = numbers[-1:] + numbers + numbers[:1]
    print(*[a + b for a, b in zip(neighbours, neighbours[2:])])
