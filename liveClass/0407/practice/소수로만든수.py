import heapq


k, n = map(int, input().split())
prime = list(map(int, input().split()))

heap_prime = []

for p in prime:
    heapq.heappush(heap_prime, p)

for i in range(n):
    p1 = heapq.heappop(heap_prime)
    for j in range(k):
        heapq.heappush(heap_prime, p1*prime[j])

        if p1 % prime[j] == 0:
            break
print(p1)
