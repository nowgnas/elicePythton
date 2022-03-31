from builtins import next, print


def finite_generator():
    yield 1
    print('22')
    yield 2


gen = finite_generator()
print(gen)
print(next(gen))
print(gen)
print(next(gen))
