from util import Util

utility = Util()
file = utility.read_file('mega.txt')  # file = Lista de strings

print(file)
print(len(file))

new_file = []
for index in file:
    index.replace(',\n', '')
    #index.split(',')

print(file)
