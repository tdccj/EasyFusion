# coding=utf-8
# 用于编写达芬奇fusion表达式

from PySide2 import QtCore, QtWidgets, QtGui
from mainui import Ui_Form

version = 0.1
Time = ''
Beginning = ''
Change = ''
Duration = ''


class Ui(Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        # 初始化
        super().__init__()
        self.setupUi(self)

    def set_main(self):
        # 设置logo
        self.setWindowIcon(QtGui.QIcon('logo_fang_1.ico'))

        # 设置标题
        self.setWindowTitle(f" EasyFusion {version}")

        self.frame

        self.pushButton.clicked.connect(getdata)



def getdata():
    # 获取信息
    global Time, Beginning, Change, Duration
    Time = Main_window.lineEdit_time.text()
    Beginning = Main_window.lineEdit_beginning.text()
    Change = Main_window.lineEdit_change.text()
    Duration = Main_window.lineEdit_Duration.text()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    Main_window = Ui()
    Main_window.set_main()
    Main_window.show()
    app.exec_()
