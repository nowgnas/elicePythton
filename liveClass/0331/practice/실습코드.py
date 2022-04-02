'''
N by N 행렬

2는 학교, 1은 집, 0 은 빈칸

학교 거리 =  집과 가장 가까운 학교까지 거리

도시 학교 거리 = 모든 집의 학교 거리의 합

(2,1)에 있는 집과 (1,2) 에 있는 학교 사이 거리는 2, (5,5) 에 있는 학교집과 거리는 7

학생수가 갈수록 적어져서, 학교들 중 M 개만 고르고 나머지를 없앨 때, 어떻게 남겨야 도시의 치킨거리가 최소일지 코드

입력 변수

첫 째줄에 N, M

둘 째줄부터 집, 학교 위치 데이터

5 2
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

'''


import itertools


def main():

    def distance(v1, v2):
        x, y = abs(v2[0] - v1[0]), abs(v2[1] - v1[1])
        return x + y

    n, m = map(int, input().split())
    map_data = [list(map(int, input().split())) for i in range(n)]

    home = []
    school = []
    for i, row in enumerate(map_data):
        for j, col in enumerate(row):
            if col == 1:
                home.append((i, j))
            elif col == 2:
                school.append((i, j))

    school_left = itertools.combinations(school, m)
    result_all = []  # 각 경우에 해당하는 도시 학교 거리
    each_home_each_school = []  # 각 집의 좌표에서 최소 학교 거리들이 포함된 리스트

    for left_temp in school_left:
        # 각 집별로 최소 학교 거리 구하기
        school_dist = []
        for i in home:  # 각 집의 좌표
            for school_pos in left_temp:
                school_dist.append(distance(school_pos, i))
            each_home_each_school.append(sorted(school_dist)[0])
        result_all.append(sum(each_home_each_school))
    print(sorted(result_all)[0])


if __name__ == '__main__':
    main()
