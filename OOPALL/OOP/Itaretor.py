class Power:
    def __init__(self, max_number):
        self.max_number = max_number

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max_number:
            result = 2**self.n
            self.n += 1
            return result
        else:
            raise StopIteration


ob = Power(4)
i = iter(ob)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))