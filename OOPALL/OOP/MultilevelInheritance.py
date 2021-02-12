class A:
    def p(self):
        print('A')
    pass
class B:
    def p(self):
        print('B')
    pass
class multiDrived(A, B):
    pass
ob = multiDrived()
ob.p()
print(multiDrived.__mro__)