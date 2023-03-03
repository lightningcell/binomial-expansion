from PyQt5.QtWidgets import QDialog
from converted_ui_files.tedwidget import Ui_Dialog


class TermExistsDialogWidget(QDialog):
    def __init__(self):
        super(TermExistsDialogWidget, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
