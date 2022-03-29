class Champion:

    def __init__(self, HP, MP):
        self.level = 1
        self.power = 10
        self.HP = HP
        self.MP = MP

    def print_status(self):
        print("Level: {} | Power: {} | HP: {} | MP: {}".format(
            self.level, self.power, self.HP, self.MP))

    def level_up(self):
        # 여기에 코드를 입력하세요.
        self.level += 1
        self.power += 2

    def use_skill(self, MP_usage):
        # 여기에 코드를 입력하세요.
        self.MP -= MP_usage


def main():

    # 아래의 코드를 완성하세요.
    archer = Champion(HP=300, MP=200)
    archer.print_status()

    archer.level_up()
    archer.print_status()

    archer.use_skill(30)
    archer.print_status()


if __name__ == "__main__":
    main()
