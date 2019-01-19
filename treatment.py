'''
This class provides treatment to list of lists of ints
'''


class Treatment:

    def how_many_pairs(self, data):
        '''
        Levantar exceção caso data, não for uma lista de ints
        '''

        even_qtt = {x: 0 for x in range(0, 7)}
        for item in data:
            even = 0
            for sub_item in item:
                if int(sub_item) % 2 != 1:  # So is even
                    even += 1

            even_qtt[even] += 1
        return even_qtt

    def neighborhood(self, data, distance):

        neighbors_qtt = {x: 0 for x in range(0,7)}
        print(len(data))
        line = 1
        for item in data:
            item.sort()
            neighbors = 0
            for sub_item in range(0, len(item)):
                try:
                    if int(item[sub_item + 1]) - int(item[sub_item]) <= distance:
                        neighbors += 1
                except IndexError:
                    #  End of the sub list
                    pass
            if neighbors == 4 and distance == 1:
                print('linha:', line, '\tItem:', item)
            neighbors_qtt[neighbors] += 1
            line+=1

        return neighbors_qtt
