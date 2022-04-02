# 단어 모음을 선언합니다. 수정하지 마세요.
words = [
    'apple',
    'banana',
    'alpha',
    'bravo',
    'cherry',
    'charlie',
]


def filter_by_prefix(words, prefix):
    # 아래 코드를 작성하세요.

    return [a for a in words if a.startswith(prefix)]


# 아래 주석을 해제하고 결과를 확인해보세요.
a_words = filter_by_prefix(words, 'a')
print(a_words)
