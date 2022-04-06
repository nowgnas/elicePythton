import time
import random


def isAnagram(str1, str2):
    if len(str1) != len(str2):  # 길이가 다르면 false

        return False

    dict1 = {}  # 첫번째 문자열에서 각 알파벳이 몇번 쓰였는지 딕셔너리 생성
    # dict1 = {'i':0, 's':0}  'sisisi'

    for ch in str1:
        dict1[ch] = dict1.get(ch, 0) + 1

        # 지난 번에 배운 코드 # dict.get

    for ch in str2:  # 두번째 문자열 한글자씩 돌면서 사전과 대조
        if ch in dict1:  # ch 가 dict1 에 있나?
            if dict1[ch] == 0:
                return False
            else:
                dict1[ch] -= 1
                # dict[ch] == 0 이면 False
                # 있다면 dict1[ch] -=1
                # 없으면 False
        else:
            return False

    return True


def main():

    print(isAnagram('iamlordvoldemort', 'tommarvoloriddle'))  # should return True
    print(isAnagram('cat', 'cap'))  # should return False


if __name__ == "__main__":
    main()
