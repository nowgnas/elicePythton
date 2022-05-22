'''
6 3 3 4
3 4 2 3
2 3 1 2
4 3 1 1
'''

n, k, p, l = map(int, input().split())
player = []
for item in range(k):
    single_player = list(map(int, input().split()))
    player.append(single_player)
print(player)

    