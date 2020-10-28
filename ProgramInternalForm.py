class ProgramInternalForm:
    def __init__(self):
        self.__content = []

    def add(self, symbol_code, symbol_index):
        self.__content.append((symbol_code, symbol_index))

    def __str__(self):
        return str(self.__content)

    def get_data(self):
        return self.__content
