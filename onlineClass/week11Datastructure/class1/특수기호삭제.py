# 트럼프 대통령의 트윗 세개로 구성된 리스트입니다. 수정하지 마세요.
trump_tweets = [
    "i hope everyone is having a great christmas, then tomorrow it’s back to work in order to make america great again.",
    "7 of 10 americans prefer 'merry christmas' over 'happy holidays'.",
    "merry christmas!!!",
]


def remove_special_characters(text):
    processed_text = []
    rep1 = ','
    rep2 = "'"
    rep3 = '!'
    # 아래 코드를 작성하세요.
    for item in text:
        newString = item.replace(rep1, '').replace(rep2, '').replace(rep3, '')

        processed_text.append(newString)

    return processed_text


# 아래 주석을 해제하고 결과를 확인해보세요.
print('\n'.join(remove_special_characters(trump_tweets)))
