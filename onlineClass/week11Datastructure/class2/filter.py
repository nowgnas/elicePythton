# CSV 모듈을 임포트합니다.
import csv


def get_titles_of_long_books(books_csv):
    with open(books_csv) as books:
        reader = csv.reader(books, delimiter=',')
        # 함수를 완성하세요.

        def is_long(row):
            if int(row[3]) > 250:
                return row

        def get_title(row): return row[0]

        long_books = filter(is_long, reader)
        long_book_titles = map(get_title, long_books)

        return list(long_book_titles)


# 작성한 함수를 테스트합니다. 주석을 해제하고 실행하세요.
books = '/mnt/f/elicepy/onlineClass/week11Datastructure/class2/TED/books.csv'
titles = get_titles_of_long_books(books)
for title in titles:
    print(title)
