'''
6
권도안 100 50
배예린 40 30
김덕배 80 80
소윤주 70 90
이숙호 90 10
김미희 60 70
'''


def make_team(players):
    # 반환값은 두 개의 리스트가 들어있는 튜플이어야 합니다.
    # 첫 번째 리스트는 엘리스 팀, 두 번째 리스트는 체셔 팀의 선수 명단입니다.
    elice = []
    cheshur = []
    step = len(players) if len(players) % 2 == 0 else len(players)-1
    for i in range(step):
        if i % 2 == 0:
            # elice
            shoot = max(players, key=lambda x: int(x[1]))
            print(shoot)
            elice.append(shoot[0])
            players.remove(shoot)
        else:
            # cheshur
            dribble = max(players, key=lambda x: int(x[2]))
            cheshur.append(dribble[0])
            players.remove(dribble)

    return (elice, cheshur)


def main():
    n = int(input())
    players = []
    for i in range(n):
        name, shoot, dribble = input().strip().split()
        players.append([name, shoot, dribble])

    elice, cheshur = make_team(players)
    elice_string = ' '.join(elice)
    cheshur_string = ' '.join(cheshur)
    print(elice_string)
    print(cheshur_string)


if __name__ == '__main__':
    main()
