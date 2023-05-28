from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("LOLovskoe okno")
        self.setGeometry(300, 300, 300, 300)  # трактарист

        self.bt2 = QtWidgets.QLabel(self)

        self.text = QtWidgets.QLabel(self)
        self.text.setText("Ты пидр")
        self.text.move(150, 150)

        self.bt = QtWidgets.QPushButton(self)
        self.bt.move(50, 50)
        self.bt.setText("Я пидр")
        self.bt.clicked.connect(self.add_lol)

    def add_lol(self):
        self.bt2.setText("Да, ты пидр")
        self.bt2.move(10, 150)





def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
