import sqlite3


class Database:
    def __init__(self, db_name, api_key, lang='ru'):
        self.db_name = db_name
        self.api_key = api_key
        self.lang = lang
        self.__init_db__()

    def __init_db__(self):
        try:
            self.__connection__ = sqlite3.connect(self.db_name)
            cur = self.__connection__.cursor()
            cur.execute('CREATE TABLE settings ()')
        except sqlite3.Error as error:
            print("Error with connect to database", error)
        finally:
            if self.__connection__:
                self.__connection__.close()
                print("Connection was closed")

    def execute(self, request):
        self.__connection__.execute(request)
