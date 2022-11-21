from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie

from functools import partial

from PyQt5.QtWidgets import QTextBrowser


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Calculator")
        Dialog.resize(379, 497)
        Dialog.setMinimumSize(QtCore.QSize(379, 497))
        Dialog.setMaximumSize(QtCore.QSize(379, 497))

        #self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        #self.lcdNumber.setGeometry(QtCore.QRect(80, 10, 280, 91))
        #self.lcdNumber.setObjectName("lcdNumber")

        self.pushButton_dot = QtWidgets.QPushButton(Dialog)
        self.pushButton_dot.setGeometry(QtCore.QRect(120, 290, 61, 41))

        self.pushButton_add = QtWidgets.QPushButton(Dialog)
        self.pushButton_add.setGeometry(QtCore.QRect(290, 290, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(13)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setStyleSheet("background-color: rgba(227, 227, 227, 100);")
        self.pushButton_add.setObjectName("pushButton")

        self.pushButton_subtraction = QtWidgets.QPushButton(Dialog)
        self.pushButton_subtraction.setGeometry(QtCore.QRect(290, 190, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(13)
        self.pushButton_subtraction.setFont(font)
        self.pushButton_subtraction.setStyleSheet("background-color: rgba(227, 227, 227, 100);")
        self.pushButton_subtraction.setObjectName("pushButton")

        self.pushButton_clear = QtWidgets.QPushButton(Dialog)
        self.pushButton_clear.setGeometry(QtCore.QRect(290, 350, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(13)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setStyleSheet("background-color: rgba(227, 227, 227, 100);")
        self.pushButton_clear.setObjectName("pushButton")

        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(190, 290, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(13)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgba(227, 227, 227, 100);")
        self.pushButton_9.setObjectName("pushButton_4")

        self.pushButton_mult = QtWidgets.QPushButton(Dialog)
        self.pushButton_mult.setGeometry(QtCore.QRect(20, 440, 75, 24))
        self.pushButton_mult.setObjectName("pushButton_5")

        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(110, 290, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(13)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgba(227, 227, 227, 100);")
        self.pushButton_8.setObjectName("pushButton_6")

        self.pushButton_div = QtWidgets.QPushButton(Dialog)
        self.pushButton_div.setGeometry(QtCore.QRect(110, 440, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(13)
        self.pushButton_div.setFont(font)
        self.pushButton_div.setStyleSheet("background-color: rgba(227, 227, 227, 100);")
        self.pushButton_div.setObjectName("pushButton_8")

        self.pushButton_equal = QtWidgets.QPushButton(Dialog)
        self.pushButton_equal.setGeometry(QtCore.QRect(210, 440, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(13)
        self.pushButton_equal.setFont(font)
        self.pushButton_equal.setStyleSheet("background-color: rgba(227, 227, 227, 100);")
        self.pushButton_equal.setObjectName("pushButton_9")


        self.label = QtWidgets.QLabel(Dialog)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 0, 381, 501))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(55)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(381, 501))
        self.label.setMaximumSize(QtCore.QSize(381, 501))
        self.label.setText("")
        self.label.setObjectName("label")



        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(80, 10, 280, 91))
        font = QtGui.QFont()
        font.setFamily("")
        font.setPointSize(22)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgba(227, 227, 227, 100);")

        #self.movie = QMovie("anime-hips.gif")
        #self.label.setMovie(self.movie)
        #self.movie.start()


        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 290, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(13)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgba(227, 227, 227, 100);")
        self.pushButton_7.setObjectName("pushButton_10")

        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(190, 230, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(13)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgba(227, 227, 227, 100);")
        self.pushButton_6.setObjectName("pushButton_11")

        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 230, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(13)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgba(227, 227, 227, 100);")
        self.pushButton_5.setObjectName("pushButton_12")

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 230, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(13)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgba(227, 227, 227, 100);")
        self.pushButton_4.setObjectName("pushButton_13")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 170, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(13)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgba(227, 227, 227, 100);")
        self.pushButton_3.setObjectName("pushButton_14")


        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 170, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(13)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgba(227, 227, 227, 100);")
        self.pushButton_2.setObjectName("pushButton_15")

        self.pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_1.setGeometry(QtCore.QRect(30, 170, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(13)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("background-color: rgba(227, 227, 227, 100);")
        self.pushButton_1.setObjectName("pushButton_16")
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(13)

        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 301, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.label.raise_()
        self.textBrowser.raise_()
        self.pushButton_add.raise_()
        self.pushButton_div.raise_()
        self.pushButton_equal.raise_()
        self.pushButton_mult.raise_()
        self.pushButton_9.raise_()
        self.pushButton_8.raise_()
        self.pushButton_7.raise_()
        self.pushButton_6.raise_()
        self.pushButton_5.raise_()
        self.pushButton_4.raise_()
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.pushButton_1.raise_()
        self.pushButton_clear.raise_()
        #self.lcdNumber.raise_()
        self.gridLayoutWidget.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_add.clicked.connect(partial(self.number, '+'))
        self.pushButton_div.clicked.connect(partial(self.number, '/'))
        self.pushButton_equal.clicked.connect(self.result)
        self.pushButton_mult.clicked.connect(partial(self.number, '*'))
        self.pushButton_9.clicked.connect(partial(self.number, '9'))
        self.pushButton_8.clicked.connect(partial(self.number, '8'))
        self.pushButton_7.clicked.connect(partial(self.number, '7'))
        self.pushButton_6.clicked.connect(partial(self.number, '6'))
        self.pushButton_5.clicked.connect(partial(self.number, '5'))
        self.pushButton_4.clicked.connect(partial(self.number, '4'))
        self.pushButton_3.clicked.connect(partial(self.number, '3'))
        self.pushButton_2.clicked.connect(partial(self.number, '2'))
        self.pushButton_1.clicked.connect(partial(self.number, '1'))

    number_1 = ''

    def number(self, name):
        self.name = name
        global number_1
        self.number_1 += name
        print(self.number_1)
        self.textBrowser.setText(self.number_1)

    def result(self):
        global number_1
        print(self.number_1)
        self.a = eval(self.number_1)
        self.textBrowser.setText(str(self.a))
        self.number_1 = ''
#str('{:.4f}'.format(float(eval(self.number_1))))

    def clear(self):
        global number_1
        self.number_1 = ''
        self.textBrowser.setText('0')


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calculator"))
        self.pushButton_clear.setText(_translate("Dialog", "C"))
        self.pushButton_add.setText(_translate("Dialog", "+"))
        self.pushButton_mult.setText(_translate("Dialog", "*"))
        self.pushButton_div.setText(_translate("Dialog", "/"))
        self.pushButton_equal.setText(_translate("Dialog", "="))
        self.pushButton_9.setText(_translate("Dialog", "&9"))
        self.pushButton_8.setText(_translate("Dialog", "&8"))
        self.pushButton_7.setText(_translate("Dialog", "&7"))
        self.pushButton_6.setText(_translate("Dialog", "&6"))
        self.pushButton_5.setText(_translate("Dialog", "&5"))
        self.pushButton_4.setText(_translate("Dialog", "&4"))
        self.pushButton_3.setText(_translate("Dialog", "&3"))
        self.pushButton_2.setText(_translate("Dialog", "&2"))
        self.pushButton_1.setText(_translate("Dialog", "&1"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

