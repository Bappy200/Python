my_list = [1,2,3,3]
my_set = {2,4,5,67}
r = [*my_set,*my_list]
print(r)


def display(a,b,*args):
    print(a)
    print(b)
    print(args)

display(*r)