from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import Qt
from converted_ui_files.mainwindow import Ui_Window
from unknown_terms.alpha_term import AlphaTerm, TermPrinter
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
        t1 = self.ui.term1_combo_box.currentText()
        t2 = self.ui.term2_combo_box.currentText()
        term_list = list()

        for term in [t1, t2]:
            if term.isnumeric():
                t = int(term) if float(term).is_integer() else float(term)
            elif term in self.terms:
                t = self.terms_dict[term]
            else:
                return MessageBox(f"{term} is not a valid value.").exec_()

            term_list.append(t)

        self.ui.result_text.setPlainText(
            binomial_expansion(
                term_list[0],
                term_list[1],
                self.ui.spin_box_exponent_binom.value()
            )
        )

    def update_combo_box(self):
        self.ui.term1_combo_box.clear()
        self.ui.term1_combo_box.addItems(self.terms)
        self.ui.term2_combo_box.clear()
        self.ui.term2_combo_box.addItems(self.terms)

    def create_term(self) -> int:
        unknown = self.ui.line_edit_unknown.text()

        if len(unknown) > 1:
            return MessageBox("Please enter a valid value for unknown.").exec_()

        if len(unknown) == 0:
            return MessageBox("It looks like you want to create a known term. "
                              "You can do this conveniently on the binomial expansion page. "
                              "You don't need to create a term for this!").exec_()

        term = AlphaTerm(
            self.ui.spin_box_base.value(),
            unknown,
            self.ui.spin_box_exponent.value()
        )

        str_term = TermPrinter.print(term, True, 0).strip()
        self.temp_term = term

        if str_term in self.terms_dict.keys():
            dialog = TermExistsDialogWidget()
            dialog.setWindowTitle("Dikkat !")
            dialog.setWindowIcon(QIcon("media/message.png"))
            dialog.ui.buttonBox.clicked.connect(lambda button: self.term_exists_dialog(button))
            return dialog.exec_()

        self.terms.append(str_term)
        self.ui.terms_table.insertRow(0)
        items = [str_term, term.get_coefficient(), term.get_alpha(), term.get_exponent()]
        for i in range(0, 4):
            self.ui.terms_table.setItem(0, i, QTableWidgetItem(str(items[i])))

        self.update_combo_box()
        self.terms_dict[str_term] = term
        return MessageBox(f"'{str_term}' created.").exec_()

    def term_exists_dialog(self, button: QPushButton):
        if button.text() == "OK":
            str_term = TermPrinter.print(self.temp_term, True).strip()
            items = [str_term,
                     self.temp_term.get_coefficient(),
                     self.temp_term.get_alpha(),
                     self.temp_term.get_exponent()]
            for i in range(0, 4):
                self.ui.terms_table.setItem(0, i, QTableWidgetItem(str(items[i])))

            self.update_combo_box()
            self.terms_dict[str_term] = self.temp_term
            MessageBox(f"'{str_term}' created.").exec_()


app = QApplication(sys.argv)
app.setStyle("Fusion")
win = Window()
win.show()
app.exec_()
