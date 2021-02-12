def fnc(f):
    def warp():
        print("satrt")
        f()
        print('end')
    return warp

@fnc
def fnc1():
    print('i am fnc1')

@fnc
def fnc2():
    print('i am fnc2')




fnc1()
fnc2()