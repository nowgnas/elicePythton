import my_module
from utils import add


def main():

    num1 = 10
    num2 = 5

    # square 함수는 my_module.py 내에 있습니다.
    num1_squared = my_module.square(10)
    print(num1_squared)

    # add 합수는 utils.py 내에 있습니다.
    total_sum = add(num1, num2)
    print(total_sum)


if __name__ == "__main__":
    main()
