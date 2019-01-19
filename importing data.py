import xlrd

def read_xls(arq_xls):
    """
    Gerador que le arquivo .xls
    """

    # Abre o arquivo
    xls = xlrd.open_workbook(arq_xls)
    # Pega a primeira planilha do arquivo
    plan = xls.sheets()[0]

    # Para i de zero ao numero de linhas da planilha
    for i in range(plan.nrows):
        # Le os valores nas linhas da planilha
        yield plan.row_values(i)

newlist = []
prepare = []
for linha in read_xls('mega.xls'):
    prepare = linha[0:6]
    if '' not in prepare:
        newlist.append(prepare)

another_list = []
for item in newlist:
    item = [int(item[x]) for x in range(0,6)]
    another_list.append(item)

newlist.clear()
#print(another_list)


def to_write(list):
    text = ''
    for index in list:
        for subindex in range(0,6):
            if subindex != 5:
                text += str(index[subindex]) + ','
            else:
                text += str(index[subindex]) + ',\n'

    return text


def write_to_file(text, file_name):
    file = open(file_name, "a+")
    file.write(text)
    file.close()


write_to_file(to_write(another_list), 'mega.txt')

