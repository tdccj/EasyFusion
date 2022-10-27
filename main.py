# coding=utf-8
# 用于编写达芬奇fusion表达式

from PySide2 import QtCore, QtWidgets, QtGui
from mainui import Ui_Form

version = 0.1
Time = ''
Beginning = ''
Change = ''
Duration = ''
Function_Easing = []
Method_Easing = []
Choose_Function = ''
Choose_Method = ''



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

        # 设置缓动函数选择框
        self.comboBox_functions.addItems(Function_Easing)
        self.comboBox_method.addItems(Method_Easing)

        self.pushButton.clicked.connect(getdata)



def getdata():
    # 获取信息
    global Time, Beginning, Change, Duration,Choose_Function,Choose_Method
    # 获取TBCD信息
    Time = Main_window.lineEdit_time.text()
    Beginning = Main_window.lineEdit_beginning.text()
    Change = Main_window.lineEdit_change.text()
    Duration = Main_window.lineEdit_Duration.text()
    # 获取函数选择
    Choose_Function = Main_window.comboBox_functions.currentText()
    Choose_Method = Main_window.comboBox_method.currentText()
    print(Time, Beginning, Change, Duration,Choose_Function,Choose_Method)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    Main_window = Ui()
    Main_window.set_main()
    Main_window.show()
    app.exec_()
