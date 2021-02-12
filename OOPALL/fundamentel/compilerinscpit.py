import inspect
import queue


def num(n):
    if n == 2:
        def et():
            print('n is 2')
    else:
        def et():
            print('n is not 2')
    return et


ob = num(3)

print(inspect.getsource(ob))
print(inspect.getmodule(ob))
print(inspect.getmembers(ob))
print(inspect.getsource(queue))
