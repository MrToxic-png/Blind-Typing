# Form implementation generated from reading ui file 'Verification.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(1126, 903)
        Dialog.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 58, 58);")
        self.pixmap = QtGui.QPixmap(f'../Images/Backgroung.jpg')
        self.picture = QtWidgets.QLabel(parent=Dialog)
        self.picture.resize(1126, 903)
        self.picture.setPixmap(self.pixmap)
        self.login_butt = QtWidgets.QPushButton(parent=Dialog)
        self.login_butt.setGeometry(QtCore.QRect(440, 470, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.login_butt.setFont(font)
        self.login_butt.setStyleSheet("color: rgb(255, 148, 60);")
        self.login_butt.setFlat(True)
        self.login_butt.setObjectName("login_butt")
        self.reg_butt = QtWidgets.QPushButton(parent=Dialog)
        self.reg_butt.setGeometry(QtCore.QRect(410, 600, 291, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.reg_butt.setFont(font)
        self.reg_butt.setStyleSheet("color: rgb(255, 148, 60);")
        self.reg_butt.setFlat(True)
        self.reg_butt.setObjectName("reg_butt")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(370, 140, 311, 131))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel { background-color: transparent; color: rgba(255, 255, 255, 150); }")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(490, 240, 351, 91))
        self.label_2.setStyleSheet("QLabel { background-color: transparent; color: rgba(255, 255, 255, 150); }")
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.login_butt.setText(_translate("Dialog", "Войти"))
        self.reg_butt.setText(_translate("Dialog", "Зарегистрироваться"))
        self.label.setText(_translate("Dialog", "Blind "))
        self.label_2.setText(_translate("Dialog", "Typing"))
