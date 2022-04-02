class Champion:

    team_color = None

    def __init__(self):
        self.champion_color = 'yellow'

    def change_team_color(self):
        Champion.team_color = 'red'

    def change_champion_color(self):
        self.team_color = 'blue'


def main():

    # 인스턴스를 생성하는 코드를 추가하세요.
    warrior = Champion()
    archer = Champion()

    # 이후 속성값들을 확인해보세요.
    warrior.change_team_color()
    print(warrior.team_color, archer.team_color)

    warrior.change_champion_color()
    print(warrior.team_color, archer.team_color)

    print(warrior.__dict__)
    print(archer.__dict__)


if __name__ == "__main__":
    main()
