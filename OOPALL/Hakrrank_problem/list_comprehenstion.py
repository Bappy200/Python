item = [1, 2, 3, 4, 5, 6]
new_item_filter = list(filter(lambda x: x % 2 == 0, item))
print(new_item_filter)

new_item_maps = list(map(lambda x: x*2, item))
print(new_item_maps)

new_list = [i if i > 9 else '' for i in range(20) if i % 2 == 0]

print(new_list)

new_list_boolen = ['even' if i % 2 == 0 else 'odd' for i in range(20)]
print(new_list_boolen)

matrix = [[1, 2], [3, 4], [4, 6]]

new_matrix = [[row[i] for row in matrix] for i in range(2)]
print(new_matrix)

new_matrix_two = [[row[i] for row in new_matrix] for i in range(3)]
print(new_matrix_two)





