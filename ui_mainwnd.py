# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwnd.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(820, 166)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWidget.setFont(font)
        self.gridLayout_2 = QtWidgets.QGridLayout(MainWidget)
        self.gridLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listeningChk = QtWidgets.QCheckBox(MainWidget)
        self.listeningChk.setObjectName("listeningChk")
        self.horizontalLayout_2.addWidget(self.listeningChk)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.ok = QtWidgets.QPushButton(MainWidget)
        self.ok.setMinimumSize(QtCore.QSize(130, 0))
        self.ok.setObjectName("ok")
        self.horizontalLayout_2.addWidget(self.ok)
        self.cancel = QtWidgets.QPushButton(MainWidget)
        self.cancel.setMinimumSize(QtCore.QSize(130, 0))
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_2.addWidget(self.cancel)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(MainWidget)
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.profileCbx = QtWidgets.QComboBox(MainWidget)
        self.profileCbx.setMinimumSize(QtCore.QSize(250, 0))
        self.profileCbx.setObjectName("profileCbx")
        self.horizontalLayout.addWidget(self.profileCbx)
        self.addBut = QtWidgets.QPushButton(MainWidget)
        self.addBut.setMinimumSize(QtCore.QSize(130, 0))
        self.addBut.setObjectName("addBut")
        self.horizontalLayout.addWidget(self.addBut)
        self.editBut = QtWidgets.QPushButton(MainWidget)
        self.editBut.setMinimumSize(QtCore.QSize(130, 0))
        self.editBut.setObjectName("editBut")
        self.horizontalLayout.addWidget(self.editBut)
        self.removeBut = QtWidgets.QPushButton(MainWidget)
        self.removeBut.setMinimumSize(QtCore.QSize(130, 0))
        self.removeBut.setObjectName("removeBut")
        self.horizontalLayout.addWidget(self.removeBut)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(MainWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "LinVAM"))
        self.listeningChk.setText(_translate("MainWidget", "Enable Listening"))
        self.ok.setText(_translate("MainWidget", "OK"))
        self.cancel.setText(_translate("MainWidget", "Cancel"))
        self.label.setText(_translate("MainWidget", "Profile:"))
        self.addBut.setText(_translate("MainWidget", "Add"))
        self.editBut.setText(_translate("MainWidget", "Edit"))
        self.removeBut.setText(_translate("MainWidget", "Remove"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWidget = QtWidgets.QWidget()
    ui = Ui_MainWidget()
    ui.setupUi(MainWidget)
    MainWidget.show()
    sys.exit(app.exec_())