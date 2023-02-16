from random import randint
count = randint(10, 20)
list_rand = []
for i in range(count):
    list_rand.append(randint(-10, 10))
print(f'Массив: {list_rand}')

min_elem = int(input('Введите минимальное значение диапазона: '))
max_elem = int(input('Введите максимальное значение диапазона: '))

print(f'Диапазон значений: [{min_elem}, {max_elem}]')
print('Индексы элементов, которые входят в диапазон: ')
for i in range(len(list_rand)):
    if min_elem <= list_rand[i] <= max_elem:
        print(f'{i} ', end='')