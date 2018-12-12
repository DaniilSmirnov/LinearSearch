from PyQt5 import QtCore, QtGui, QtWidgets


def linearSearch(li, x):
    i = 0
    length = len(li)
    while i < length and x != li[i]:
        i += 1
    return i if i < length else None


def linearSearchBarrier(li, x):
    li.append(x)
    i = 0
    while li[i] != x:
        i += 1
    return i if i < len(li) - 1 else None


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(508, 470)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.linearedit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linearedit.sizePolicy().hasHeightForWidth())
        self.linearedit.setSizePolicy(sizePolicy)
        self.linearedit.setObjectName("linearedit")
        self.gridLayout.addWidget(self.linearedit, 1, 0, 1, 1)
        self.linearsearchedit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linearsearchedit.sizePolicy().hasHeightForWidth())
        self.linearsearchedit.setSizePolicy(sizePolicy)
        self.linearsearchedit.setObjectName("linearsearchedit")
        self.gridLayout.addWidget(self.linearsearchedit, 1, 1, 1, 1)
        self.linearlabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linearlabel.sizePolicy().hasHeightForWidth())
        self.linearlabel.setSizePolicy(sizePolicy)
        self.linearlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.linearlabel.setObjectName("linearlabel")
        self.gridLayout.addWidget(self.linearlabel, 0, 0, 1, 1)
        self.barrierserchedit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.barrierserchedit.sizePolicy().hasHeightForWidth())
        self.barrierserchedit.setSizePolicy(sizePolicy)
        self.barrierserchedit.setObjectName("barrierserchedit")
        self.gridLayout.addWidget(self.barrierserchedit, 3, 1, 1, 1)
        self.barrierresult = QtWidgets.QLabel(self.centralwidget)
        self.barrierresult.setObjectName("barrierresult")
        self.gridLayout.addWidget(self.barrierresult, 3, 2, 1, 1)
        self.barrierlabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.barrierlabel.sizePolicy().hasHeightForWidth())
        self.barrierlabel.setSizePolicy(sizePolicy)
        self.barrierlabel.setScaledContents(False)
        self.barrierlabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.barrierlabel.setObjectName("barrierlabel")
        self.gridLayout.addWidget(self.barrierlabel, 2, 0, 1, 1)
        self.linearresult = QtWidgets.QLabel(self.centralwidget)
        self.linearresult.setObjectName("linearresult")
        self.gridLayout.addWidget(self.linearresult, 1, 2, 1, 1)
        self.barrieredit = QtWidgets.QLineEdit(self.centralwidget)
        self.barrieredit.setObjectName("barriereditt")
        self.gridLayout.addWidget(self.barrieredit, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 508, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Алгоритмы поиска"))
        self.linearlabel.setText(_translate("MainWindow", "Линейный поиск"))
        self.barrierresult.setText(_translate("MainWindow", ""))
        self.barrierlabel.setText(_translate("MainWindow", "Линейный поиск с барьером"))
        self.linearresult.setText(_translate("MainWindow", ""))

        self.linearedit.textChanged.connect(self.linear)
        self.linearsearchedit.textChanged.connect(self.linear)

        self.barrieredit.textChanged.connect(self.barrier)
        self.barrierserchedit.textChanged.connect(self.barrier)

    def linear(self):
        li = []
        text = self.linearedit.text()
        text = text.split(",")
        for item in text:
                li.append(item)

        x = self.linearsearchedit.text()

        result = linearSearch(li, x)
        if result is not None and x != '':
            result = "Искомый элемент под номером " + str(result + 1)
        else:
            result = "Искомый элемент не найден"
        self.linearresult.setText(result)

    def barrier(self):
        li = []
        text = self.barrieredit.text()
        text = text.split(",")
        for item in text:
                li.append(item)

        x = self.barrierserchedit.text()

        result = linearSearchBarrier(li, x)
        if result is not None and x != '':
            result = "Искомый элемент под номером"  + str(result + 1)
        else:
            result = "Искомый элемент не найден"
        self.barrierresult.setText(result)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

