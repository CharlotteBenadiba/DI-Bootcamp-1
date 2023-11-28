#1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# print(dict(zip(keys, values)))

#2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# total_cost = 0
# for x,y in family.items():
#     if y <3:
#         continue
#     elif 3 < y <12:
#         total_cost += 10
#     elif y >= 12:
#         total_cost += 15     

# print(f'Your total cost for the movie is $', total_cost)   

# family = {}
# users_name = input('Your name')
# users_age = input('Your age')
# family[users_name] = int(users_age)
# print(family)
# total_cost = 0
# for name,age in family.items():
#     if age <3:
#         continue
#     elif 3 < age <12:
#         total_cost += 10
#     elif age >= 12:
#         total_cost += 15     

# print(f'Your total cost for the movie is $', total_cost) 

#3
# brand = {'name': 'Zara',
#          'creation_date': 1975,
#          'creator_name': 'Amancio Ortega Gaona', 
#          'type_of_clothes' : ['men', 'women', 'children', 'home'],
#          'international_competitors': ['Gap, H&M, Benetton'],
#          'number_stores': 7000,
#          'major_color':
#          {'France': 'blue', 
#           'Spain': 'red', 
#           'US': 'pink, green'},
# }
# print(brand)

# brand['number_stores'] = 2
# print(brand)

# print(' '.join(list(brand['major_color'].keys())))
# print('Zara\'s clients are '  + ' '.join(brand['type_of_clothes'][0:2]) + ' from ' + ' '.join(list(brand['major_color'].keys())))


# brand['country_creation'] = 'Spain'
# print(brand)
 

# if 'international_competitors' in brand:
#     brand['international_competitors'].append('Desigual') 
#     print(brand)

# del brand['creation_date']   
# print(brand)

# last_competitor = brand['international_competitors'][-1]
# print(last_competitor)

# us_colors = brand['major_color']['US']
# print('Major color in the US is', us_colors)

# print(len(list(brand.keys())))

# x = brand.keys()
# print(x)

# more_on_zara = {
#     'creation_date': 1975,
#     'number_stores': 10000
# }
# brand['more_on_zara'] = more_on_zara
# print(brand)

# print(brand['number_stores'])

#4
# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# disney_users_A = {user: index for index, user in enumerate(users)}
# print(disney_users_A)

# disney_users_B = {index: user for index, user in enumerate(users)}
# print(disney_users_B)

# sort = users.sort()
# disney_users_C = {sort:index for index, sort in enumerate(users) }
# print(disney_users_C)

# filtered_users_1 = [user for user in users if 'i' in user]
# disney_users_A = {user: index for index, user in enumerate(filtered_users_1)}
# print(disney_users_A)

# filtered_users_2 = [user for user in users if user.startswith(('M', 'P'))]
# disney_users_A = {user: index for index, user in enumerate(filtered_users_2)}
# print(disney_users_A)


