from PyQt5 import QtWidgets
import sys


class Main_Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.show()


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


if __name__ == "__main__":
    # Back up the reference to the exceptionhook
    sys._excepthook = sys.excepthook

    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook

    qt_start = QtWidgets.QApplication(sys.argv)
    main_qt = Main_Window()

    sys.exit(qt_start.exec_())
