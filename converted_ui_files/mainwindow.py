# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(640, 388)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Window.sizePolicy().hasHeightForWidth())
        Window.setSizePolicy(sizePolicy)
        Window.setMaximumSize(QtCore.QSize(640, 480))
        Window.setWindowFilePath("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Window)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tab_widget = QtWidgets.QTabWidget(Window)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tab_widget.setFont(font)
        self.tab_widget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tab_widget.setStyleSheet("QTabBar::tab {\n"
"            border: 1px solid white;\n"
"            background-color: gray;\n"
"            color: #fff;\n"
"            padding: 6px;\n"
"            border-top-left-radius: 10px;\n"
"            border-top-right-radius: 10px;\n"
"            cursor: pointing-hand;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"    color: black;\n"
"    border: 1px solid gray;\n"
"}")
        self.tab_widget.setMovable(True)
        self.tab_widget.setObjectName("tab_widget")
        self.tab_term_creator = QtWidgets.QWidget()
        self.tab_term_creator.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tab_term_creator.setObjectName("tab_term_creator")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_term_creator)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.form_box1 = QtWidgets.QFormLayout()
        self.form_box1.setObjectName("form_box1")
        self.spin_box_base = QtWidgets.QDoubleSpinBox(self.tab_term_creator)
        self.spin_box_base.setMinimum(-1e+20)
        self.spin_box_base.setMaximum(1e+16)
        self.spin_box_base.setObjectName("spin_box_base")
        self.form_box1.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spin_box_base)
        self.lbl_x2 = QtWidgets.QLabel(self.tab_term_creator)
        self.lbl_x2.setObjectName("lbl_x2")
        self.form_box1.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_x2)
        self.line_edit_unknown = QtWidgets.QLineEdit(self.tab_term_creator)
        self.line_edit_unknown.setObjectName("line_edit_unknown")
        self.form_box1.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_edit_unknown)
        self.lbl_x3 = QtWidgets.QLabel(self.tab_term_creator)
        self.lbl_x3.setObjectName("lbl_x3")
        self.form_box1.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_x3)
        self.btn_create = QtWidgets.QPushButton(self.tab_term_creator)
        self.btn_create.setObjectName("btn_create")
        self.form_box1.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.btn_create)
        self.lbl_x1 = QtWidgets.QLabel(self.tab_term_creator)
        self.lbl_x1.setObjectName("lbl_x1")
        self.form_box1.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_x1)
        self.spin_box_exponent = QtWidgets.QSpinBox(self.tab_term_creator)
        self.spin_box_exponent.setMinimum(-999999999)
        self.spin_box_exponent.setMaximum(999999999)
        self.spin_box_exponent.setObjectName("spin_box_exponent")
        self.form_box1.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spin_box_exponent)
        self.verticalLayout_2.addLayout(self.form_box1)
        self.hbox2 = QtWidgets.QHBoxLayout()
        self.hbox2.setObjectName("hbox2")
        self.line_edit_term = QtWidgets.QLineEdit(self.tab_term_creator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_edit_term.sizePolicy().hasHeightForWidth())
        self.line_edit_term.setSizePolicy(sizePolicy)
        self.line_edit_term.setMinimumSize(QtCore.QSize(400, 120))
        self.line_edit_term.setSizeIncrement(QtCore.QSize(60, 0))
        self.line_edit_term.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_edit_term.setFont(font)
        self.line_edit_term.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.line_edit_term.setObjectName("line_edit_term")
        self.hbox2.addWidget(self.line_edit_term)
        self.btn_generate = QtWidgets.QPushButton(self.tab_term_creator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_generate.sizePolicy().hasHeightForWidth())
        self.btn_generate.setSizePolicy(sizePolicy)
        self.btn_generate.setMinimumSize(QtCore.QSize(160, 120))
        self.btn_generate.setObjectName("btn_generate")
        self.hbox2.addWidget(self.btn_generate)
        self.verticalLayout_2.addLayout(self.hbox2)
        self.lbl_x7 = QtWidgets.QLabel(self.tab_term_creator)
        self.lbl_x7.setObjectName("lbl_x7")
        self.verticalLayout_2.addWidget(self.lbl_x7)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.setStretch(0, 40)
        self.verticalLayout_2.setStretch(1, 40)
        self.verticalLayout_2.setStretch(3, 20)
        self.tab_widget.addTab(self.tab_term_creator, "")
        self.tab_binomial_expansion = QtWidgets.QWidget()
        self.tab_binomial_expansion.setObjectName("tab_binomial_expansion")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_binomial_expansion)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.grid_box1 = QtWidgets.QGridLayout()
        self.grid_box1.setObjectName("grid_box1")
        self.lbl_x4 = QtWidgets.QLabel(self.tab_binomial_expansion)
        self.lbl_x4.setObjectName("lbl_x4")
        self.grid_box1.addWidget(self.lbl_x4, 0, 0, 1, 1)
        self.term1_combo_box = QtWidgets.QComboBox(self.tab_binomial_expansion)
        self.term1_combo_box.setObjectName("term1_combo_box")
        self.grid_box1.addWidget(self.term1_combo_box, 0, 1, 1, 1)
        self.lbl_x5 = QtWidgets.QLabel(self.tab_binomial_expansion)
        self.lbl_x5.setObjectName("lbl_x5")
        self.grid_box1.addWidget(self.lbl_x5, 1, 0, 1, 1)
        self.term2_combo_box = QtWidgets.QComboBox(self.tab_binomial_expansion)
        self.term2_combo_box.setObjectName("term2_combo_box")
        self.grid_box1.addWidget(self.term2_combo_box, 1, 1, 1, 1)
        self.lbl_x6 = QtWidgets.QLabel(self.tab_binomial_expansion)
        self.lbl_x6.setObjectName("lbl_x6")
        self.grid_box1.addWidget(self.lbl_x6, 2, 0, 1, 1)
        self.spin_box_exponent_binom = QtWidgets.QSpinBox(self.tab_binomial_expansion)
        self.spin_box_exponent_binom.setObjectName("spin_box_exponent_binom")
        self.grid_box1.addWidget(self.spin_box_exponent_binom, 2, 1, 1, 1)
        self.btn_calculate = QtWidgets.QPushButton(self.tab_binomial_expansion)
        self.btn_calculate.setObjectName("btn_calculate")
        self.grid_box1.addWidget(self.btn_calculate, 3, 0, 1, 2)
        self.horizontalLayout_3.addLayout(self.grid_box1)
        self.label_4 = QtWidgets.QLabel(self.tab_binomial_expansion)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.tab_widget.addTab(self.tab_binomial_expansion, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 581, 303))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scroll_vbox = QtWidgets.QVBoxLayout()
        self.scroll_vbox.setContentsMargins(-1, 0, -1, 250)
        self.scroll_vbox.setObjectName("scroll_vbox")
        self.verticalLayout_3.addLayout(self.scroll_vbox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.tab_widget.addTab(self.tab, "")
        self.horizontalLayout.addWidget(self.tab_widget)
        self.label = QtWidgets.QLabel(Window)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.retranslateUi(Window)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Binomial Expansion"))
        self.spin_box_base.setToolTip(_translate("Window", "Base"))
        self.lbl_x2.setText(_translate("Window", "Unknown"))
        self.line_edit_unknown.setToolTip(_translate("Window", "Unknown"))
        self.lbl_x3.setText(_translate("Window", "Exponent"))
        self.btn_create.setToolTip(_translate("Window", "Create"))
        self.btn_create.setText(_translate("Window", "Create"))
        self.lbl_x1.setText(_translate("Window", "Base"))
        self.spin_box_exponent.setToolTip(_translate("Window", "Exponent"))
        self.line_edit_term.setToolTip(_translate("Window", "<html><head/><body><p><span style=\" font-family:\'Courier New\'; font-weight:600; font-style:italic; color:#645e75;\">Legends say it\'s still in development</span></p><p><span style=\" font-weight:600; font-style:italic; text-decoration: underline; color:#2a00fe;\">You can create AlphaTerm like this:</span></p><p>* 2x <span style=\" font-weight:600; color:#31ff31;\">-&gt;</span><span style=\" font-weight:600;\">2.0x</span><span style=\" font-weight:600; vertical-align:super;\">1</span></p><p>* 3(y^2)<span style=\" font-weight:600; color:#31ff31;\">-&gt;</span><span style=\" font-weight:600;\">3.0y</span><span style=\" font-weight:600; vertical-align:super;\">2</span></p><p>* 5z^2 <span style=\" font-weight:600; color:#31ff31;\">-&gt;</span><span style=\" font-weight:600;\">5.0z</span><span style=\" font-weight:600; vertical-align:super;\">2</span></p><p>* (4f)^4 <span style=\" font-weight:600; color:#31ff31;\">-&gt; </span><span style=\" font-weight:600; color:#000000;\">256</span><span style=\" font-weight:600;\">.0f</span><span style=\" font-weight:600; vertical-align:super;\">4</span></p><p><span style=\" font-weight:600; font-style:italic; text-decoration: underline; color:#2a00fe;\">Also you can create MultipleAlphaTerm:</span></p><p>* 2x3(y^2)(4f)^4 <span style=\" font-weight:600; color:#31ff31;\">-&gt; </span><span style=\" font-weight:600; color:#000000;\">1536</span><span style=\" font-weight:600;\">.0x</span><span style=\" font-weight:600; vertical-align:super;\">1</span><span style=\" font-weight:600;\">y</span><span style=\" font-weight:600; vertical-align:super;\">2</span><span style=\" font-weight:600;\">f</span><span style=\" font-weight:600; vertical-align:super;\">4</span></p><p><br/></p></body></html>"))
        self.line_edit_term.setPlaceholderText(_translate("Window", "You can write the term in a regular way."))
        self.btn_generate.setToolTip(_translate("Window", "Generate"))
        self.btn_generate.setText(_translate("Window", "Generate"))
        self.lbl_x7.setToolTip(_translate("Window", "<html><head/><body><p><span style=\" font-weight:600;\">Whattttt</span><span style=\" font-size:12pt; color:#2a00fe;\">😂😂😂😂</span></p></body></html>"))
        self.lbl_x7.setText(_translate("Window", "Hover your mouse over objects and see interesting clues ! Maybe there are some hidden treasures."))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_term_creator), _translate("Window", "Term Creator"))
        self.lbl_x4.setText(_translate("Window", "Term 1:"))
        self.lbl_x5.setText(_translate("Window", "Term 2:"))
        self.lbl_x6.setText(_translate("Window", "Exponent"))
        self.btn_calculate.setText(_translate("Window", "Calculate"))
        self.label_4.setText(_translate("Window", "You will see the result in here"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_binomial_expansion), _translate("Window", "Binomial Expansion"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab), _translate("Window", "Created Terms"))
        self.label.setToolTip(_translate("Window", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffbd52;\">You got me! It is not easy to find this hidden text.</span></p><p><span style=\" font-size:12pt; color:#0cff00;\">Take screenshot and contact me:</span></p><p><span style=\" font-size:12pt; color:#ff0004;\">Gmail:</span></p><p><span style=\" font-size:12pt; color:#2a00fe;\">hamidsimsek4457@gmail.com</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QWidget()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())