def delete_duplect(items):
    return list(dict.fromkeys(items))
numbers=[1,1,2,2,3,3,4,4,5,5,5,6,6,6]
numbers=delete_duplect(numbers)
print(numbers)
x,y,z,a,b,c=numbers
print(x)
print(y)
print(z)