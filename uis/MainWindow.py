# Form implementation generated from reading ui file '.\uis\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1398, 794)
        MainWindow.setMinimumSize(QtCore.QSize(1398, 794))
        MainWindow.setMaximumSize(QtCore.QSize(1398, 16777215))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.timeTable1 = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.timeTable1.setMinimumSize(QtCore.QSize(1091, 383))
        self.timeTable1.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked|QtWidgets.QAbstractItemView.EditTrigger.EditKeyPressed)
        self.timeTable1.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.timeTable1.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.timeTable1.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.timeTable1.setObjectName("timeTable1")
        self.timeTable1.setColumnCount(6)
        self.timeTable1.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable1.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable1.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable1.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable1.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable1.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable1.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable1.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable1.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable1.setHorizontalHeaderItem(5, item)
        self.timeTable1.horizontalHeader().setDefaultSectionSize(175)
        self.timeTable1.verticalHeader().setDefaultSectionSize(60)
        self.verticalLayout.addWidget(self.timeTable1)
        self.timeTable2 = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.timeTable2.setMinimumSize(QtCore.QSize(1091, 383))
        self.timeTable2.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked|QtWidgets.QAbstractItemView.EditTrigger.EditKeyPressed)
        self.timeTable2.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.timeTable2.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.timeTable2.setObjectName("timeTable2")
        self.timeTable2.setColumnCount(6)
        self.timeTable2.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable2.setHorizontalHeaderItem(5, item)
        self.timeTable2.horizontalHeader().setDefaultSectionSize(175)
        self.timeTable2.verticalHeader().setDefaultSectionSize(60)
        self.verticalLayout.addWidget(self.timeTable2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeWidget = QtWidgets.QTreeWidget(parent=self.centralwidget)
        self.treeWidget.setMinimumSize(QtCore.QSize(280, 0))
        self.treeWidget.setTextElideMode(QtCore.Qt.TextElideMode.ElideLeft)
        self.treeWidget.setAutoExpandDelay(-1)
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayout_2.addWidget(self.treeWidget)
        self.buttonPushSetup = QtWidgets.QPushButton(parent=self.centralwidget)
        self.buttonPushSetup.setEnabled(False)
        self.buttonPushSetup.setObjectName("buttonPushSetup")
        self.verticalLayout_2.addWidget(self.buttonPushSetup)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scheduler"))
        item = self.timeTable1.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "8:00"))
        item = self.timeTable1.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "9:40"))
        item = self.timeTable1.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "11:30"))
        item = self.timeTable1.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "13:20"))
        item = self.timeTable1.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "15:00"))
        item = self.timeTable1.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "16:40"))
        item = self.timeTable1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mon"))
        item = self.timeTable1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tue"))
        item = self.timeTable1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Wed"))
        item = self.timeTable1.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Thu"))
        item = self.timeTable1.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Fri"))
        item = self.timeTable1.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Sat"))
        item = self.timeTable2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "8:00"))
        item = self.timeTable2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "9:40"))
        item = self.timeTable2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "11:30"))
        item = self.timeTable2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "13:20"))
        item = self.timeTable2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "15:00"))
        item = self.timeTable2.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "16:40"))
        item = self.timeTable2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mon"))
        item = self.timeTable2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tue"))
        item = self.timeTable2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Wed"))
        item = self.timeTable2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Thu"))
        item = self.timeTable2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Fri"))
        item = self.timeTable2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Sat"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Group selection"))
        self.buttonPushSetup.setText(_translate("MainWindow", "Push to Google Calendar"))
