from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import Qt
from converted_ui_files.mainwindow import Ui_Window
from unknown_terms.alpha_term import AlphaTerm, TermPrinter
from widgets.term_widget import TermWidget
from widgets.ted_widget import TermExistsDialogWidget
from widgets.message_widget import MessageBox
from binomial_expansion import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_Window()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon("media/icon.png"))

        # Legends say it's still in development
        self.ui.line_edit_term.setEnabled(False)
        tab_bar: QTabBar = self.ui.tab_widget.tabBar()
        tab_bar.setCursor(QCursor(Qt.PointingHandCursor))

        self.temp_term = AlphaTerm()
        self.terms = list()
        self.terms_dict = dict()

        self.ui.btn_create.clicked.connect(self.create_term)
        self.ui.btn_calculate.clicked.connect(self.calculate_binom)

    def calculate_binom(self):
        self.ui.label_4.setText(
            binomial_expansion(
                self.terms_dict[self.ui.term1_combo_box.currentText()],
                self.terms_dict[self.ui.term2_combo_box.currentText()],
                self.ui.spin_box_exponent_binom.value()
            )
        )

    def update_combo_box(self):
        self.ui.term1_combo_box.clear()
        self.ui.term1_combo_box.addItems(self.terms)
        self.ui.term2_combo_box.clear()
        self.ui.term2_combo_box.addItems(self.terms)

    def create_term(self) -> QDialog:
        unknown = self.ui.line_edit_unknown.text()

        if len(unknown) != 1:
            return MessageBox("Please enter a valid value for unknown.").exec_()

        term = AlphaTerm(
            self.ui.spin_box_base.value(),
            unknown,
            self.ui.spin_box_exponent.value()
        )

        str_term = TermPrinter.print(term)
        self.temp_term = term

        if str_term in self.terms_dict.keys():
            dialog = TermExistsDialogWidget()
            dialog.setWindowTitle("Dikkat !")
            dialog.setWindowIcon(QIcon("media/message.png"))
            dialog.ui.buttonBox.clicked.connect(lambda button: self.term_exists_dialog(button))
            return dialog.exec_()

        self.terms.append(str_term)
        widget = TermWidget(term)
        self.ui.scroll_vbox.insertWidget(0, widget)
        self.update_combo_box()
        self.terms_dict[str_term] = term
        return MessageBox(f"'{str_term}' created.").exec_()

    def term_exists_dialog(self, button: QPushButton):
        if button.text() == "OK":
            str_term = TermPrinter.print(self.temp_term)
            widget = TermWidget(self.temp_term)
            self.ui.scroll_vbox.insertWidget(0, widget)
            self.update_combo_box()
            self.terms_dict[str_term] = self.temp_term
            MessageBox(f"'{str_term}' created.").exec_()


app = QApplication(sys.argv)
app.setStyle("Fusion")
win = Window()
win.show()
app.exec_()
