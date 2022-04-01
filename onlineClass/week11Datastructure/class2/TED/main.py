# csv 모듈을 임포트합니다.
import csv
import json


def print_book_info(filename):
    with open(filename) as file:
        # ',' 기호로 분리된 CSV 파일을 처리하세요..
        reader = csv.reader(file, delimiter=',')

        # 처리된 파일의 각 줄을 불러옵니다.
        for row in reader:

            # 함수를 완성하세요.
            title = row[0]
            author = row[1]
            pages = row[3]
            print("{} ({}): {}p".format(title, author, pages))


def books_to_json(src_file, dst_file):
    # 아래 함수를 완성하세요.
    books = []
    with open(src_file) as src:
        reader = csv.reader(src, delimiter=',')

        # 각 줄 별로 대응되는 book 딕셔너리를 만듭니다.
        for title, author, genre, pages, publisher in reader:
            # 책 정보를 저장하는 딕셔너리를 생성합니다.
            book = {
                "title": title,
                "author": author,
                "genre": genre,
                "pages": int(pages),
                "publisher": publisher
            }
            books.append(book)

    with open(dst_file, 'w') as dst:
        # JSON 형식으로 dst_file에 저장합니다.
        json_string = json.dumps(books)
        dst.write(json_string)


# 아래 주석을 해제하고 실행 결과를 확인해보세요.
file_path = '/mnt/f/elicepy/onlineClass/week11Datastructure/class2/TED/books.csv'
filename = 'books.csv'
# print_book_info(file_path)

src_file = 'books.csv'
dst_file = 'books.json'
books_to_json(file_path, dst_file)
# elice_utils.send_file(dst_file)
