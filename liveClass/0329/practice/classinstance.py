class Champion:

    def __init__(self, HP=300, MP=200):
        self.HP = HP
        self.MP = MP


def main():
    # 아래의 코드를 완성하세요.
    warrior = Champion(HP=500, MP=0)
    archer = Champion(HP=300, MP=200)
    wizard = Champion(HP=200, MP=500)

    print(warrior.HP, warrior.MP)
    print(archer.HP, archer.MP)
    print(wizard.HP, wizard.MP)


if __name__ == "__main__":
    main()
