class Util:

    def read_file(self, file_name):
        file = open(file_name, "r+")
        lines = file.readlines()
        file.close()

        return lines

    def write_to_file(self, text, file_name):
        file = open(file_name, "a+")
        file.write(text)
        file.close()

    def write_list_to_file(self, list, file_name):
        text = ""
        for index in list:
            text += index

        file = open(file_name, "w+")
        file.write(text)
        file.close()
