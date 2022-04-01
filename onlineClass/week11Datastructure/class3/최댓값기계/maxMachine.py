'''
maxMachine 클래스를 완성하세요.
'''


class maxMachine:
    def __init__(self):
        self.nums = []

    def addNumber(self, n):
        self.nums.append(n)

    def removeNumber(self, n):
        self.nums.remove(n)

    def getMax(self):
        return max(self.nums)
