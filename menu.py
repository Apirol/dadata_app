

class Menu:
    def __init__(self, attributes: list, function: callable, config):
        self.api = self.__get_api__()
        self.item_counter = 0
        self.attributes = attributes
        self.__input__: int = 0

    def execute(self, function, config):
        self.__input__ = int(input('Please, type chosen variant: '))
        if self.__input__ == 1:
        if self.__input__ == 2:
        if self.__input__ == 3:

    def get_input(self):
        return self.__input__

    def __enter__(self):
        if self.item_counter == len(self.attributes) - 1:
            print(f'-1 : {self.attributes[self.item_counter]}')
        else:
            print(f'{self.item_counter + 1} : {self.attributes[self.item_counter]}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.item_counter += 1

    def __get_api__(self):
        return str(input('Please, past here your API key from dadata service: '))

