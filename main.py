# coding=utf-8
# 用于编写达芬奇fusion表达式

from PySide2 import QtCore, QtWidgets, QtGui
from mainui import Ui_Form
from easing_functions import *

# import numpy as np
# from matplotlib import pyplot as plt

version = 0.2
Time = ''
Beginning = ''
Change = ''
Duration = ''
Function_Easing = ['quadratic', 'linear', 'sinusoidal', 'exponential']  # linear不得在第一
Method_Easing = ['In', 'Out']  # 暂时没有'InOut'选项
Choose_Function = ''
Choose_Method = ''
check_autoEasing = True
function_export = ''


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

        # 设置自动缓动选项
        self.checkBox_autoEasing.setChecked(True)

        # 设置默认值
        self.lineEdit_time.setText('(time/comp:GetPrefs("Comp.FrameFormat.Rate"))')

        self.pushButton.clicked.connect(getdata)

        self.comboBox_functions.currentIndexChanged.connect(switch)


def switch():
    # 用于切换线性和函数
    print(Main_window.comboBox_functions.currentText())
    if Main_window.comboBox_functions.currentText() == 'linear':
        Main_window.comboBox_method.clear()
        Main_window.comboBox_method.addItem('none')
    else:
        Main_window.comboBox_method.clear()
        Main_window.comboBox_method.addItems(Method_Easing)


def getdata():
    # 获取信息并判断
    global Time, Beginning, Change, Duration, Choose_Function, Choose_Method, function_export
    # 获取TBCD信息
    Time = Main_window.lineEdit_time.text()
    Beginning = Main_window.lineEdit_beginning.text()
    Change = Main_window.lineEdit_change.text()
    Duration = Main_window.lineEdit_Duration.text()
    # 获取函数选择
    Choose_Function = Main_window.comboBox_functions.currentText()
    Choose_Method = Main_window.comboBox_method.currentText()

    # 判断选择函数并输出
    function_export = judge(Choose_Function, Choose_Method, Time, Beginning, Change, Duration)
    export()


def export():
    # 用于显示输出

    # 如果出现--替换为空
    global function_export
    num = 0
    while function_export.find('--', num) != -1:
        num = function_export.find('--', num)
        front = function_export[:num]
        behind = function_export[num + 2:]
        function_export = front + behind
        num = num + 1

    # 用于判断显示输出
    if Main_window.checkBox_autoEasing.isChecked():
        auto_easing()
        Main_window.plainTextEdit_export.setPlainText(function_export)
    else:
        Main_window.plainTextEdit_export.setPlainText(function_export)

    # 设置函数图片显示(未完成）
    #
    # Main_window.graphicsView.set
    # Main_window.label_photo.setScaledContents(True)


def auto_easing():
    # 设置自动缓动
    global function_export
    function_export = f'iif({Time}<{Duration},{function_export},{float(Beginning) + float(Change)})'


if __name__ == "__main__":
    print("!请不要将程序文件夹放置在程序无法访问到的地方\n如nas、网盘等挂载分区上，否则可能不会显示GUI窗口\n")
    print("新版本、更新公告、问题反馈请前往：\nhttps://github.com/tdccj/EasyFusion/tree/master\n")
    print("!!!暂时请绝对不要使用exponential(指数)函数，\n有可能导致fusion无法启动(重装达芬奇无解，可能是vc库或别的地方出现了问题)")
    app = QtWidgets.QApplication([])
    Main_window = Ui()
    Main_window.set_main()
    Main_window.show()
    app.exec_()
