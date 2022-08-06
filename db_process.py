import sqlite3


class Database:
    def __init__(self, db_name, api_key, lang='ru'):
        self.db_name = db_name
        self.api_key = api_key
        self.lang = lang
        self.__connection__ = self.__init_db__()
        self.__cursor__ =

    def __init_db__(self):
        try:
            con = sqlite3.connect(self.db_name)
            cur = con.cursor()
        except sqlite3.Error as error:
            print("Error with connect to database", error)
        finally:
            if con:
                con.close()
                print("Connection was closed")


    def execute(self, request):
        self.__connection__.execute()

