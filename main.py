from PyQt5 import QtWidgets
from PyQt5 import QtCore
import sys

from ReadCSV.reader import CSV_converter


class Main_Window(QtWidgets.QWidget):
    window_width = 640
    window_height = 480

    default_file_path = "C:\\"

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

        # Window drag and drops 활성화
        self.setAcceptDrops(True)

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

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        self.road_file(files[0])

    def road_file(self, path=""):
        if path == "":
            read_path, _ = \
                QtWidgets.QFileDialog.getOpenFileNames(
                    self,
                    "csv 파일 선택",
                    self.default_file_path
                )
            if read_path == "":
                return
        else:
            if not path.split("/")[-1].split(".")[-1] == "csv":
                self.show_error_message("csv 파일이 아닙니다.")
                return

            converter = CSV_converter(path)
            converter.convert()

            self.show_info_message("변환이 완료되었습니다.")

    def show_error_message(self, msg):
        QtWidgets.QMessageBox.warning(
            self,
            "경고",
            msg
        )

    def show_info_message(self, msg):
        QtWidgets.QMessageBox.information(
            self,
            "알림",
            msg
        )


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
