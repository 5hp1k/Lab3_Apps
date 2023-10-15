import sys

from task5 import *
from task3 import *

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('task6.ui', self)
        self.setFixedSize(700, 325)
        self.enterButton.clicked.connect(self.addRecord)

    def addRecord(self):
        login = self.loginField.text()
        number = self.numberField.text()
        password = self.passwordField.text()

        try:
            check_password(password)
            formatted_number = format_phone_number(number)
            self.listWidget.addItem(f"{login}: {formatted_number}")
            self.errorLabel.setText("")
        except PasswordError as e:
            self.errorLabel.setText(f"Password Error: {e}")
        except (CountryCodeError, DigitCountError, OperatorError, FormatError) as e:
            self.errorLabel.setText(f"Number Error: {e}")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
