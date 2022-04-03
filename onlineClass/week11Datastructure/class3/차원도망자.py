# 리스트와 튜플을 이용해 문제를 해결할 수 있습니다.
def compress(S):
    S = sorted(L)
    M = {}
    for i in range(len(S)):
        M[S[i]] = i
    return M


n = int(input())
m = int(input())
L = list(map(int, input().split()))
MAP = compress(L)
sign = input()

dim = [0] * m
trace = {tuple(dim)}
for i in range(m):
    # 방문 위치를 계산합니다.
    dim[MAP[L[i]]] += 1 if sign[i] == "+" else -1
    T = tuple(dim)
    # 이미 방문한 곳이라면 0을 반환합니다.
    if T in trace:
        print(0)
        break
    trace.add(T)
else:
    print(1)
