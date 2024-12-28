import sys

from PyQt5 import QtWidgets

from db.database import Database
from ui.window import Window

DB_NAME: str = "users_database.db"
TABLE_NAME: str = "Users"
TABLE_HEADRES: tuple = ('Имя', 'Фамилия', 'Возраст')

#Подключаемся к БД и получаем данные из нужной таблицы
users_db = Database(DB_NAME)
users = users_db.get_data_from_table(TABLE_NAME)

# Создаем виджеты и главное окно
app = QtWidgets.QApplication([])
application = Window()

# Задаем заголовки и данные для отображения
application.set_headers(TABLE_HEADRES)
application.set_data(users)

# Запускаем приложение
application.show()
sys.exit(app.exec())
