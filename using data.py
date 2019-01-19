from util import Util
from treatment import Treatment

utility = Util()
file = utility.read_file('mega.txt')  # file = Lista de strings

aux_file = []
for index in file:
    aux_file.append(index.replace(',\n', '').split(','))

all_lottery = aux_file
# all_lottery stores all result of lottery as a list of lists

del aux_file

numbers_frequency = {key: 0 for key in range(1,61)}

for x in range(1,61):
    for lottery in all_lottery:
        for number in lottery:
            if number == str(x):
                numbers_frequency[x] += 1

'''
print(len(all_lottery*6))
total = 0
for key in numbers_frequency.keys():
    total += numbers_frequency.get(key)
print(total)
print(numbers_frequency)
'''

position = 1
numbers_position = {}
for item in sorted(numbers_frequency, key=numbers_frequency.get, reverse=True):
    # print('Número sorteado:', item, ' \tQtd de vezes',
    #  numbers_frequency[item], '\tPosição:', position)
    numbers_position.update({item: position})
    position += 1

treatment = Treatment()
even_quantity = treatment.how_many_pairs(all_lottery)

neighbors_1 = treatment.neighborhood(all_lottery, 1)
neighbors_2 = treatment.neighborhood(all_lottery, 2)
neighbors_3 = treatment.neighborhood(all_lottery, 3)
neighbors_4 = treatment.neighborhood(all_lottery, 4)
neighbors_5 = treatment.neighborhood(all_lottery, 5)

print('Quantidade de pares:\n', even_quantity)
print('\n\n Distância 1\n', neighbors_1)
print('\n\n Distância 2\n', neighbors_2)
print('\n\n Distância 3\n', neighbors_3)
print('\n\n Distância 4\n', neighbors_4)
print('\n\n Distância 5\n', neighbors_5)
