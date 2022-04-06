import functools
# from functools import reduce


lst = [1, 2, 3, 4, 5]
n = 5
result = functools.reduce(lambda x, y: x*y, list(range(1, n+1)))
print(result)
