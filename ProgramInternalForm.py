class ProgramInternalForm:
    def __init__(self):
        self.__content = []

    def add(self, code, symbol):
        self.__content.append((code, symbol))

    def __str__(self):
        return str(self.__content)

    def get_data(self):
        return self.__content
