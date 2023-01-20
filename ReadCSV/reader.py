import csv
import os
from datetime import datetime


class CSV_converter:
    default_header = [
        "구분", "Site", "level1", "level2", "level3", "intent",
        "sample_question", "response", "action", "표정코드", "연결 페이지"
    ]

    keyword_max_num = 29

    finish_name_list = []

    def __init__(self, file_path):
        self.file_path = file_path
        for x in range(1, 30):
            self.default_header.append(
                f"keyword{x}"
            )
            self.default_header.append(
                f"score{x}"
            )

    def convert(self):
        if not self.check_path():
            return False

        csv_data = self.__read_csv_file()

        self.__replace_csv_data(csv_data)

    # 받은 파일 경로가 유효한 파일 경로인지 확인
    def check_path(self):
        if not os.path.isfile(self.file_path):
            # 유효한 파일 경로가 아니라면 None return
            return False
        else:
            return True

    # csv 파일을 읽어서 추출한 데이터 반환
    def __read_csv_file(self):
        csv_data = []
        # with 문으로 csv 파일 읽기
        with open(self.file_path, "r", encoding='UTF8') as csv_file:
            reader = csv.reader(csv_file)
            for line in reader:
                csv_data.append(line)

        return csv_data[1:]

    def __replace_csv_data(self, csv_data):
        result_data = []

        ori_file_nm = self.file_path.split("/")[-1].split(".")[0]
        new_file_nm = ori_file_nm + "_" + datetime.now().strftime("%y%m%d_%H%M%S")

        new_file_path = self.file_path.replace(ori_file_nm, new_file_nm)

        with open(new_file_path, 'w', newline='', encoding='cp949') as w_file:
            wr = csv.writer(w_file)
            wr.writerow(
                self.default_header
            )

            for data in csv_data:
                name = data[1]

                if name in self.finish_name_list:
                    continue

                find_data = self.__find_text_in_csv_data(csv_data, name, 1)


                self.finish_name_list.append(name)
                wr.writerow(
                    [
                        # 구분
                        "직원",
                        # site
                        "직원",
                        # level1
                        name,
                        # level2
                        find_data["num"],
                        # level3
                        "",
                        # intent
                        f"{name}_{find_data['num']}",
                        # sample question
                        name,
                        # response
                        "",
                        # action
                        find_data["action"],
                        # 표정코드
                        "",
                        # 연결 페이지
                        "",
                        # keyword1
                        name,
                        # score1
                        50,
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                    ]
                )

    def __find_text_in_csv_data(self, csv_data, text, index):
        result_data = {
            "num": 0,
            "action": "n_"
        }
        for data in csv_data:
            if data[index] == text:
                result_data["num"] += 1
                if result_data["num"] == 1:
                    result_data["action"] += text + "_" + data[0] + ".jpg"
                else:
                    result_data["action"] += "_" + data[0] + ".jpg"

        return result_data
