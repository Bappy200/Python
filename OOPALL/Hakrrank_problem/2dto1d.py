matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
new=[j for i in matrix for j in i]
print(new)

planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]
new_planets= [j for i in planets for j in i if len(j)<6]
print(new_planets)