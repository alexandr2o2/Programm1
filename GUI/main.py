import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.dialog = None
        uic.loadUi("First_try_UI.ui", self)

        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])

        toolbar = NavigationToolbar(self.sc, self)

        self.QVBoxLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.QVBoxLayout_2.setObjectName("QVBoxLayout_2")

        self.QVBoxLayout_2.addWidget(self.sc)
        self.QVBoxLayout_2.addWidget(toolbar)

        self.pushButton.clicked.connect(self.on_pushButton_clicked)

    def on_pushButton_clicked(self):
        self.dialog = PathWindow_Data()
        # self.dialogs.append(dialog)
        self.dialog.show()


class PathWindow_Data(QtWidgets.QDialog):
    def __init__(self):
        super(PathWindow_Data, self).__init__()
        uic.loadUi("PathWindow_Data.ui", self)

        self.pushButton.clicked.connect(self.getfile)
        self.pushButton_2.clicked.connect(self.getfile_2)

    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "Data file (* *.data)")
        self.lineEdit.setText(fname[0])

    def getfile_2(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "Data file (* *.data)")
        self.lineEdit_2.setText(fname[0])


def startGUI():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # window = PathWindow_Data()
    # window.show()
    sys.exit(app.exec_())


def main():
    pass


if __name__ == "__main__":
    startGUI()
