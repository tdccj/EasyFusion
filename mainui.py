# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(460, 343)
        Form.setMinimumSize(QSize(460, 0))
        Form.setStyleSheet(u"font: 9pt \"HarmonyOS Sans SC\";")
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 0))
        self.pushButton.setToolTipDuration(-1)

        self.verticalLayout_3.addWidget(self.pushButton)

        self.verticalSpacer_3 = QSpacerItem(0, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.gridLayout_2.addWidget(self.frame, 2, 1, 1, 1)

        self.plainTextEdit_export = QPlainTextEdit(Form)
        self.plainTextEdit_export.setObjectName(u"plainTextEdit_export")
        self.plainTextEdit_export.setMinimumSize(QSize(0, 0))
        self.plainTextEdit_export.setMaximumSize(QSize(16777215, 60))
        self.plainTextEdit_export.setStyleSheet(u"font: 57 12pt \"HarmonyOS Sans SC Medium\";")
        self.plainTextEdit_export.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_export.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.plainTextEdit_export.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.gridLayout_2.addWidget(self.plainTextEdit_export, 2, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_2, 0, 2, 1, 1)

        self.verticalFrame = QFrame(Form)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setMinimumSize(QSize(220, 0))
        self.verticalFrame.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_time = QFrame(self.verticalFrame)
        self.frame_time.setObjectName(u"frame_time")
        self.frame_time.setFrameShape(QFrame.StyledPanel)
        self.frame_time.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_time)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_time)
        self.label.setObjectName(u"label")
        self.label.setAcceptDrops(False)
        self.label.setToolTipDuration(-1)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame_time)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setToolTipDuration(5)

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout_2.addWidget(self.frame_time)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.frame_beginning = QFrame(self.verticalFrame)
        self.frame_beginning.setObjectName(u"frame_beginning")
        self.frame_beginning.setFrameShape(QFrame.StyledPanel)
        self.frame_beginning.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_beginning)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_beginning)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame_beginning)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout_2.addWidget(self.frame_beginning)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.frame_change = QFrame(self.verticalFrame)
        self.frame_change.setObjectName(u"frame_change")
        self.frame_change.setFrameShape(QFrame.StyledPanel)
        self.frame_change.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_change)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame_change)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.frame_change)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_3.addWidget(self.lineEdit_3)


        self.verticalLayout_2.addWidget(self.frame_change)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.frame_6 = QFrame(self.verticalFrame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.frame_6)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_4.addWidget(self.lineEdit_4)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.gridLayout_2.addWidget(self.verticalFrame, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pushButton.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa", None))
#if QT_CONFIG(tooltip)
        self.frame_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u9ed8\u8ba4\u4e3a\u79d2</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u65f6\u95f4", None))
#if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u9ed8\u8ba4</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit.setStatusTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u9ed8\u8ba4</p></body></html>", None))
#endif // QT_CONFIG(statustip)
        self.label_2.setText(QCoreApplication.translate("Form", u"\u52a8\u753b\u8d77\u70b9", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u4ece\u5f00\u59cb\u5230\u7ed3\u675f\u8f93\u51fa\u503c\u7684\u53d8\u5316\u5dee\u503c</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Form", u"\u52a8\u753b\u5dee\u503c", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u5355\u4f4d\u8981\u4e0e\u5f53\u524d\u65f6\u95f4\u7edf\u4e00</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Form", u"\u6301\u7eed\u65f6\u95f4", None))
    # retranslateUi

