

class Menu:
    def __init__(self, attributes: list):
        self.api = self.__get_api__()
        self.item_counter = 0
        self.__attributes = attributes
        self.__input: int = 0

    def execute(self,):
        res:str = ""
        self.__input = int(input('Please, type chosen variant: '))

    def set_attributes(self, attr):
        self.__attributes = attr

    def get_input(self):
        return self.__input

    def __enter__(self):
        if self.item_counter == len(self.__attributes) - 1:
            print(f'-1 : {self.__attributes[self.item_counter]}')
        else:
            print(f'{self.item_counter + 1} : {self.__attributes[self.item_counter]}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.item_counter += 1

    def __get_api__(self):
        return str(input('Please, past here your API key from dadata service: '))

