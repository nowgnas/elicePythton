# a = list(range(100))
# b = list(range(101))
# c = a[99]+b[100]
# print(c)

# random_string = 'abcd'
# random_string = random_string + 'e'
# print(random_string)


class Cal():
    def __init__(self):
        self.result = 10

    def add(self, num):
        self.result += num
        return self.result


c = Cal()
print(c.add(7))
