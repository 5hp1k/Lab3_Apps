import sys

from dict_password_check import *

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('task7.ui', self)
        self.setFixedSize(600, 325)

        self.passwords = []
        self.english_words = []

        self.init()
        self.execButton.clicked.connect(self.on_exec_button_click)

    def init(self):
        with open('data/top 10000 passwd.txt', 'r') as file:
            self.passwords = file.read().splitlines()

        with open('data/top-9999-words.txt', 'r') as file:
            self.english_words = set(file.read().splitlines())

    def on_exec_button_click(self):
        error_stats = {}

        for password in self.passwords:
            errors = dict_password_check(password, self.english_words)
            for error in errors:
                error_name = error.__class__.__name__
                if error_name in error_stats:
                    error_stats[error_name] += 1
                else:
                    error_stats[error_name] = 1

        for error, count in sorted(error_stats.items()):
            self.listWidget.addItem(f"{error}: {count}")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
