# 아래 코드는 문제 해결을 위해 기본적으로 제공되는 코드입니다. 수정하지 마세요!
import json
from movies import titles

file = 'netflix.json'


def get_top_movies(n):
    # 지시사항을 참고하여 코드를 작성하세요.
    watcher = {}
    with open(file) as files:
        loaded = files.read()
        for movie, users in json.loads(loaded).items():
            watcher[movie] = len(users)

    top_movie = {}
    for code, user in watcher.items():
        if user > n:
            top_movie[titles[code]] = user

    return top_movie


# 값을 확인하기 위한 코드입니다. 값을 변경해가며 테스트해 보세요!
print(get_top_movies(23500))
