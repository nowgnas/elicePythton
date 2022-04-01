import csv
import json
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

from operator import itemgetter

from elice_utils import EliceUtils
elice_utils = EliceUtils()


def jsonify(data):
    return json.loads(data.replace("'", '"'))


def preprocess_talks(csv_file):
    # 강연 데이터를 저장할 빈 리스트를 선언합니다.
    talks = []

    # CSV 파일을 열고, 데이터를 읽어 와서 talks에 저장합니다.
    with None as None:
        reader = None

        for None in reader:
            try:
                talk = {
                    'title': None,     # 강연의 제목
                    'speaker': None,   # 강연자의 이름
                    'views': None,     # 조회수
                    'comments': None,  # 댓글의 개수
                    'duration': None,  # 강연 길이
                    'languages': None,  # 지원하는 언어의 수
                    'tags': None,      # 관련 태그 (키워드)
                    'ratings': None,   # 강의에 대한 평가
                }
            except:
                pass
            talks.append(talk)

    return talks


def get_popular_tags(talks, n):
    # 태그 별 인기도를 저장할 딕셔너리
    tag_to_views = {}

    # 태그 별 인기도를 구해 tag_to_views에 저장합니다.
    pass

    # (태그, 인기도)의 리스트 형식으로 변환합니다.
    tag_view_pairs = list(tag_to_views.items())

    # 인기도가 높은 순서로 정렬해 앞의 n개를 취합니다.
    # n개를 취한 후에는 태그만 남깁니다.
    # 힌트: itemgetter()를 사용하세요!
    top_tag_and_views = sorted(tag_view_pairs, key=None, reverse=None)[:n]
    top_tags = map(None, None)

    return list(top_tags)


def completion_rate_by_duration(talks):
    durations = None
    completion_rates = None
    scatter_plot(durations, completion_rates, '강의 길이', '완수도')

    return completion_rates, durations


def views_by_languages(talks):
    languages = None
    views = None
    scatter_plot(languages, views, '언어의 수', '조회수')

    # 채점을 위해 결과를 리턴합니다.
    return views, languages


def show_ratings(talk):
    pass
    keywords = None
    counts = None

    bar_plot(keywords, counts, '키워드', 'rating의 수')

    # 채점을 위해 결과를 리턴합니다.
    return keywords, counts


def scatter_plot(x, y, x_label, y_label):
    font = fm.FontProperties(fname='./NanumBarunGothic.ttf')

    plt.scatter(x, y)
    plt.xlabel(x_label, fontproperties=font)
    plt.ylabel(y_label, fontproperties=font)

    plt.xlim((min(x), max(x)))
    plt.ylim((min(y), max(y)))
    plt.tight_layout()

    plot_filename = 'plot.png'
    plt.savefig(plot_filename)
    elice_utils.send_image(plot_filename)


def bar_plot(x_ticks, y, x_label, y_label):
    assert(len(x_ticks) == len(y))

    font = fm.FontProperties(fname='./NanumBarunGothic.ttf')

    pos = range(len(y))
    plt.bar(pos, y, align='center')
    plt.xticks(pos, x_ticks, rotation='vertical', fontproperties=font)

    plt.xlabel(x_label, fontproperties=font)
    plt.ylabel(y_label, fontproperties=font)
    plt.tight_layout()

    plot_filename = 'plot.png'
    plt.savefig(plot_filename)
    elice_utils.send_image(plot_filename)


def main():
    src = 'ted.csv'
    talks = preprocess_talks(src)
    print(get_popular_tags(talks, 10))
    # completion_rate_by_duration(talks)
    # views_by_languages(talks)
    # show_ratings(talks[0])


if __name__ == "__main__":
    main()
