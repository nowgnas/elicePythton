# 아래 코드는 문제 해결을 위해 기본적으로 제공되는 코드입니다. 수정하지 마세요!
hashtag, mention, plain = [], [], []


# 지시사항을 참고하여 코드를 작성하세요.
txt = 'Make America Great Again @Trump #Speech #White_HOuse'
txt = txt.split(' ')
for item in txt:
    if item.startswith('#'):
        hashtag.append(item[1:])
    elif item.startswith('@'):
        mention.append(item[1:])
    else:
        plain.append(item)


# 아래의 코드는 값을 확인하기 위한 코드입니다.
print(hashtag)
print(mention)
print(plain)
