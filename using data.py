from util import Util

utility = Util()
file = utility.read_file('mega.txt')  # file = Lista de strings

aux_file = []
for index in file:
    aux_file.append(index.replace(',\n', '').split(','))

all_lottery = aux_file
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
    #print('Número sorteado:', item, ' \tQtd de vezes', numbers_frequency[item], '\tPosição:', position)
    numbers_position.update({item:position})
    position +=1

mom_bets = [[10,11,14,15,16,18,28,58],
            [1,4,9,13,27,31,51,56],
            [3,9,27,34,41,46,51,56],
            [1,4,13,31,34,41,46,51],
            [5,10,11,15,18,20,28,43],
            [5,6,8,10,18,28,29,40],
            [1,4,24,31,33,34,37,41],
            [4,12,24,27,34,37,41,44],
            [1,3,4,12,24,27,33,44]
            ]

mom_bets_positions = []

for bet in mom_bets:
    aux_mbp = []
    for number in bet:
        aux_mbp.append(numbers_position.get(number))

    mom_bets_positions.append(aux_mbp)


for bet in mom_bets_positions:
    print(bet)

