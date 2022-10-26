# coding=utf-8
# 用于编写达芬奇fusion表达式

from PySide2 import QtCore,QtWidgets,QtGui
from mainui import Ui_Form


class Ui:
    def __init__(self):
        self.ui = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(self.ui)

        self.set_icon()


    def set_icon(self,):








if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    Main_window = Ui()
    Main_window.ui.show()
    app.exec_()
