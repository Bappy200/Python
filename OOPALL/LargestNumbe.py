class Numbers:
    def largest(self,lists):
        max = lists[0]
        for item in lists:
            if max < item:
                max = item
        return max


number1 = Numbers()
result = number1.largest([1,2,21,21,23,43,23,54])
print(result)

