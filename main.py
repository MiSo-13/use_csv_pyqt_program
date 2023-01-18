from PyQt5 import QtWidgets
from PyQt5 import QtCore
import sys


class Main_Window(QtWidgets.QWidget):
    window_width = 640
    window_height = 480

    def __init__(self):
        super().__init__()
        self.window_setting()

        # QLabel 사용하기
        self.main_lbl = QtWidgets.QLabel("업무 자동화 프로그램", self)
        # 라벨 중앙 정렬
        self.main_lbl.setAlignment(QtCore.Qt.AlignCenter)

        # QPushButton 사용하기
        self.upload_csv_btn = QtWidgets.QPushButton("csv 열기", self)
        self.make_csv_btn = QtWidgets.QPushButton("csv 만들기", self)

        # 레이아웃 정의
        vBox = QtWidgets.QVBoxLayout(self)
        hBox = QtWidgets.QHBoxLayout(self)

        # 라벨 위젯 넣기
        vBox.addWidget(self.main_lbl)

        # 버튼 위젯 넣기
        hBox.addWidget(self.upload_csv_btn)
        hBox.addWidget(self.make_csv_btn)

        # 레이아웃에 레이아웃 넣기
        vBox.addLayout(hBox)

        # 최종적으로 레이아웃 적용
        self.setLayout(vBox)

        self.show()

    def window_setting(self):
        # Window 크기 변경
        self.resize(self.window_width, self.window_height)

        # Window 크기 고정
        self.setFixedSize(self.window_width, self.window_height)

        # Window 가로 크기만 고정
        # self.setFixedWidth(self.window_width)

        # Window 세로 크기만 고정
        # self.setFixedHeight(self.window_height)

        # Window 제목 변경
        self.setWindowTitle("PyQt 업무 자동화 프로그램")


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
