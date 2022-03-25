# 트럼프 대통령 트윗을 공백 기준으로 분리한 리스트입니다. 수정하지 마세요.
trump_tweets = ['thank', 'you', 'to', 'president', 'moon', 'of', 'south', 'korea', 'for',
                'the', 'beautiful', 'welcoming', 'ceremony', 'it', 'will', 'always', 'be', 'remembered']


def print_korea(text):
    for item in text:
        if item[0] == 'k':
            print(item)


print_korea(trump_tweets)
