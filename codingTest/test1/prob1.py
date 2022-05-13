'''
5 8 5
2 2
3 3
4 4
5 3
6 2

'''


def main():
    n, m, k = map(int, input().split())
    carrot = []
    for item in range(k):
        x, y = map(int, input().split())
        carrot.append([x, y])

    sort_x = sorted(carrot, key=lambda x: x[0])
    min_x = sort_x[0][0]
    max_x = sort_x[-1][0]
    sor_y = sorted(carrot, key=lambda x: x[1])
    min_y = sor_y[0][1]
    max_y = sor_y[-1][1]

    width = abs((min_x-1) - (max_x+1))
    height = abs((min_y-1) - (max_y+1))
    lengh = (width+height)*2
    print(lengh)


if __name__ == "__main__":
    main()
