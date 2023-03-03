from PyQt5.QtWidgets import QWidget
from converted_ui_files.termwidget import Ui_Form
from unknown_terms.printer import TermPrinter
from unknown_terms.alpha_term import AlphaTerm


class TermWidget(QWidget):
    def __init__(self, term: AlphaTerm):
        super(TermWidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.lbl_term.setText(TermPrinter.print(term))
        self.ui.lbl_base.setText(str(term.get_coefficient()))
        self.ui.lbl_unknown.setText(term.get_alpha())
        self.ui.lbl_exponent.setText(str(term.get_exponent()))
