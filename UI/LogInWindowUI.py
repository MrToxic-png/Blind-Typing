# Form implementation generated from reading ui file 'LogInWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(949, 487)
        Dialog.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 58, 58);")
        Dialog.setSizeGripEnabled(False)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(230, 20, 311, 131))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(350, 120, 351, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(200, 270, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_4.setObjectName("label_4")
        self.username_log_edit = QtWidgets.QLineEdit(parent=Dialog)
        self.username_log_edit.setGeometry(QtCore.QRect(290, 270, 491, 20))
        self.username_log_edit.setObjectName("username_log_edit")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(200, 340, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_5.setObjectName("label_5")
        self.password_log_edit = QtWidgets.QLineEdit(parent=Dialog)
        self.password_log_edit.setGeometry(QtCore.QRect(290, 340, 491, 21))
        self.password_log_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_log_edit.setObjectName("password_log_edit")
        self.ready_butt = QtWidgets.QPushButton(parent=Dialog)
        self.ready_butt.setGeometry(QtCore.QRect(750, 420, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ready_butt.setFont(font)
        self.ready_butt.setFlat(False)
        self.ready_butt.setObjectName("ready_butt")
        self.back_butt = QtWidgets.QPushButton(parent=Dialog)
        self.back_butt.setGeometry(QtCore.QRect(830, 20, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.back_butt.setFont(font)
        self.back_butt.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Images/Back_butt.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.back_butt.setIcon(icon)
        self.back_butt.setIconSize(QtCore.QSize(100, 100))
        self.back_butt.setFlat(True)
        self.back_butt.setObjectName("back_butt")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(390, 230, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Blind "))
        self.label_2.setText(_translate("Dialog", "Typing"))
        self.label_4.setText(_translate("Dialog", "Username:"))
        self.label_5.setText(_translate("Dialog", "Password:"))
        self.ready_butt.setText(_translate("Dialog", "Готово"))
        self.label_3.setText(_translate("Dialog", "Вход:"))
