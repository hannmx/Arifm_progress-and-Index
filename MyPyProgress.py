a1 = int(input('Введите первый элемент арифметической прогрессии: '))
d = int(input('Введите разность арифметической прогрессии: '))
n = int(input('Введите количество элементов арифметической прогрессии: '))
list_progress = []
for i in range(n):
    list_progress.append(a1 + i * d)

print(f'Арифметическая прогрессия: {list_progress}')