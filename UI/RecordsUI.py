# Form implementation generated from reading ui file 'Records.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(1123, 895)
        Dialog.setStyleSheet("background-color: rgb(58, 58, 58);")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(350, 30, 311, 131))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(470, 130, 351, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(410, 250, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_3.setObjectName("label_3")
        self.records_table = QtWidgets.QTableWidget(parent=Dialog)
        self.records_table.setGeometry(QtCore.QRect(80, 320, 1001, 501))
        self.records_table.setMinimumSize(QtCore.QSize(1001, 501))
        self.records_table.setMaximumSize(QtCore.QSize(16777215, 501))
        self.records_table.setStyleSheet("color: rgb(0, 170, 0);")
        self.records_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.records_table.setAutoScroll(True)
        self.records_table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.records_table.setRowCount(40)
        self.records_table.setObjectName("records_table")
        self.records_table.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.records_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.records_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.records_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.records_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.records_table.setHorizontalHeaderItem(4, item)
        self.records_table.horizontalHeader().setDefaultSectionSize(192)
        self.back_butt = QtWidgets.QPushButton(parent=Dialog)
        self.back_butt.setGeometry(QtCore.QRect(990, 30, 101, 101))
        self.back_butt.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/Back_butt.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.back_butt.setIcon(icon)
        self.back_butt.setIconSize(QtCore.QSize(100, 100))
        self.back_butt.setFlat(True)
        self.back_butt.setObjectName("back_butt")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Blind "))
        self.label_2.setText(_translate("Dialog", "Typing"))
        self.label_3.setText(_translate("Dialog", "Топ 40 Рекордов:"))
        item = self.records_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Username"))
        item = self.records_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Training mode"))
        item = self.records_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Speed"))
        item = self.records_table.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Accuracy"))
        item = self.records_table.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Time"))
