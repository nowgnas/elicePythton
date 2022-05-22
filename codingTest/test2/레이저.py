'''
7 2
1 4 1
5 4 1
3 2 3
6 1 2
7 5 3
4 3 2
8 4 1

'''
n, h = map(int, input().split())

razer = []
stop = 0
hole = 0
for item in range(n):
    left_bottom, height, attr = map(int, input().split())
    razer.append([left_bottom, height, attr])

sort_razer = sorted(razer, key=lambda x: x[0])

for x, hei, att in sort_razer:
    if x == sort_razer[-1][0]:
        stop = -1
    if h < hei:
        if att == 1:
            hole += 1
        elif att == 3:
            stop = x
            break
print(f'{stop} {hole}')
