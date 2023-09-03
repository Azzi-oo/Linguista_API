# class Vehicle:
#     def print_details(self):
#         print("Это родительский метод из класса Vehicle")
#
# # создание класса, который наследует Vehicle
# class Car(Vehicle):
#     def print_details(self):
#         print("Это дочерний метод из класса Car")
#
# # создание класса Cycle, который наследует Vehicle
# class Cycle(Vehicle):
#     def print_details(self):
#         print("Это дочерний метод из класса Cycle")
#
# veh = Vehicle()
# veh.print_details()
#
# veh_1 = Car()
# veh_1.print_details()
#
# veh_2 = Cycle()
# veh_2.print_details()
# import sys
# from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout, QVBoxLayout
#
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#
#     def initUI(self):
#
#         okButton = QPushButton("OK")
#         cancelButton = QPushButton("Cancel")
#
#         hbox = QHBoxLayout()
#         hbox.addStretch(1)
#         hbox.addWidget(okButton)
#         hbox.addWidget(cancelButton)
#
#         vbox = QVBoxLayout()
#         vbox.addStretch(1)
#         vbox.addLayout(hbox)
#
#         self.setLayot(vbox)
#
#         self.setGeometry(300, 300, 300, 150)
#
#         self.WindowTitle('Buttons')
#         self.show()
#
#         # lbl1 = QLabel('Zetcode', self)
#         # lbl1.move(15, 10)
#         #
#         # lbl2 = QLabel('tutorials', self)
#         # lbl2.move(35, 40)
#         #
#         # lbl3 = QLabel('for programmers', self)
#         # lbl3.move(55, 70)
#         #
#         # self.setGeometry(300, 300, 250, 150)
#         # self.setWindowTitle('Absolute')
#         # self.show()
#
#
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.QtWidgets import (QWidget, QPushButton,
#      QGridLayout, QApplication)
#
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#
#     def initUI(self):
#
#         grid = QGridLayout()
#         self.setLayout(grid)
#
#         names = ['Cls', 'Bck', '', 'Close',
#                  '7', '8', '9', '/',
#                  '4', '5', '6', '*',
#                  '1', '2', '3', '-',
#                  '0', '.', '=', '+']
#
#         positions = [(i, j) for i in range(5) for j in range(4)]
#
#         for position, name in zip(positions, names):
#
#             if name == '':
#                 continue
#             button = QPushButton(name)
#             grid.addWidget(button, *position)
#
#         self.move(300, 150)
#         self.setWindowTitle('Calculator')
#         self.show()
#
#
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
