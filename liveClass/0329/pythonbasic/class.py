class cal():
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result = self.result+num
        return self.result


call = cal()
print(call.add(3))
