list_number = [1, 2, 3, 4, 5, 6]
new_list = list(filter(lambda x: x % 2 == 0 and x % 5 == 0, [i for i in range(20)]))
print(new_list)

new_list_two = list(filter(lambda x: x % 2 and x % 5 == 0, list_number))
print(new_list_two)

second_list = list(map(lambda x: x*2, list_number))
print(second_list)