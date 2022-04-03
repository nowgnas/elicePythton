# 아래 코드는 문제 해결을 위해 기본적으로 제공되는 코드입니다. 수정하지 마세요!
import json

fileame = '/Volumes/nowgnas/elicepy/onlineTest/week11/items.json'
item = 'items.json'

name = input()
answer = []
# 지시사항 1번을 참고하여 코드를 작성하세요.
with open(fileame) as file:
    items = json.load(file)

    jsons = items['product_doll']
    for item in jsons:
        dicts = {}
        if name in item['name']:
            dicts['name'] = item['name']
            dicts['price'] = item['price']
            answer.append(dicts)

print(answer)
