import sqlite3

class Database:

    def __init__(self, name):
        self.name = "db/" + name


    def get_data_from_table(self, tablename):

        # Подключаемся к БД и получаем все данные
        connection = sqlite3.connect(self.name)
        cursor = connection.cursor()
        
        cursor.execute('''SELECT * FROM ''' + tablename)
        users = cursor.fetchall()

        return users