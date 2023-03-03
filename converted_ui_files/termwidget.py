# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'term_widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(540, 90)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(540, 90))
        Form.setMaximumSize(QtCore.QSize(540, 90))
        Form.setStyleSheet("background-color: rgb(38, 255, 0);\n"
"border: 1px solid black;")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_x1 = QtWidgets.QLabel(Form)
        self.lbl_x1.setStyleSheet("font: 12pt \"Britannic Bold\";")
        self.lbl_x1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_x1.setObjectName("lbl_x1")
        self.gridLayout.addWidget(self.lbl_x1, 0, 1, 1, 1)
        self.lbl_x2 = QtWidgets.QLabel(Form)
        self.lbl_x2.setStyleSheet("font: 12pt \"Britannic Bold\";")
        self.lbl_x2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_x2.setObjectName("lbl_x2")
        self.gridLayout.addWidget(self.lbl_x2, 0, 2, 1, 1)
        self.lbl_x3 = QtWidgets.QLabel(Form)
        self.lbl_x3.setStyleSheet("font: 12pt \"Britannic Bold\";")
        self.lbl_x3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_x3.setObjectName("lbl_x3")
        self.gridLayout.addWidget(self.lbl_x3, 0, 3, 1, 1)
        self.lbl_term = QtWidgets.QLabel(Form)
        self.lbl_term.setStyleSheet("font: 12pt \"Britannic Bold\";")
        self.lbl_term.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_term.setObjectName("lbl_term")
        self.gridLayout.addWidget(self.lbl_term, 1, 0, 1, 1)
        self.lbl_base = QtWidgets.QLabel(Form)
        self.lbl_base.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_base.setObjectName("lbl_base")
        self.gridLayout.addWidget(self.lbl_base, 1, 1, 1, 1)
        self.lbl_unknown = QtWidgets.QLabel(Form)
        self.lbl_unknown.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_unknown.setObjectName("lbl_unknown")
        self.gridLayout.addWidget(self.lbl_unknown, 1, 2, 1, 1)
        self.lbl_exponent = QtWidgets.QLabel(Form)
        self.lbl_exponent.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_exponent.setObjectName("lbl_exponent")
        self.gridLayout.addWidget(self.lbl_exponent, 1, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_x1.setText(_translate("Form", "BASE"))
        self.lbl_x2.setText(_translate("Form", "UNKNOWN"))
        self.lbl_x3.setText(_translate("Form", "EXPONENT"))
        self.lbl_term.setText(_translate("Form", "TERM"))
        self.lbl_base.setText(_translate("Form", "BASE"))
        self.lbl_unknown.setText(_translate("Form", "BASE"))
        self.lbl_exponent.setText(_translate("Form", "BASE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
