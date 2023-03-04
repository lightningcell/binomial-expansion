from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QIcon


class MessageBox(QDialog):
    def __init__(self, message: str):
        super(MessageBox, self).__init__()
        self.setWindowTitle("Message")

        self.setFixedSize(300, 120)
        self.setWindowIcon(QIcon("./media/message.png"))

        v_box = QVBoxLayout(self)
        label = QLabel()
        label.setText(message)
        label.setWordWrap(True)
        button = QPushButton()
        button.setText("OK")

        v_box.addWidget(label)
        v_box.addWidget(button)

        button.clicked.connect(self.close)
