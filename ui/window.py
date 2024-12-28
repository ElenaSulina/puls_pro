from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView

from .design import Ui_MainWindow

class Window(QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
 
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.setRowCount(25)

        self.ui.pushButton.clicked.connect(self.show_data)


    def set_data(self, data: list[tuple]):
        self.data = data


    def set_headers(self, headers: tuple):
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)


    def show_data(self):

        # Задаем нужную длину таблицы и заполняем данными
        self.ui.tableWidget.setRowCount(len(self.data))

        row = 0
        for tup in self.data:
            col = 0
 
            for item in tup[1:]:
                cellinfo = QTableWidgetItem(str(item))

                #Делаем данные в ячейке недоступными для изменения пользователем
                cellinfo.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )

                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1
 
            row += 1