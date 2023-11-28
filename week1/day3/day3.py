# pizza_top_list = []
# pizza_top =''
# price = 10
# while True: 
#     pizza_top = input("Please enter a series of pizza toppings (enter 'q'  when you are finished): ").lower()  
#     if pizza_top == 'q':
#         print(f'You added {"".join(pizza_top_list)} to ur order')
#         print(pizza_top_list)
#         print(price)
#         break
#     else:
#         pizza_top_list.append(pizza_top)
#         price += 2.5

# # #     print(f'{pizza_top} was added to your pizza')

# users = {'name': 'Harry',
#          'age': 33,
#          'height' : 1.7,
#          'wizard': True,
#          'house': 'Gryfildor',
#          'hobbies' : ['flying cars', 'eating all favors beens'],
#          'best friends': {'Hermione','Ron'},
#          'family':(
#          {'name': 'Gina Weasley',
#           'age': 31,
#           'height': 1.65}),
#           }
# # print(users[1])
# print(users['height'])
# # print(users['best friends'])
# wife = users['family']['name']
# print('wife:', wife)
# users['house'] = 'Slytherin'
# print(users['house'])

#add new key value

# users ['pet'] = 'Hedwig'
# print(users)

#delete 

# del users['height']
# print(users)

# #set 
# print('wizard' in users )
# print('height' in users )

# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }

# print(sample_dict['class']['student']['marks']['history'])


#BUILT IN METHODS

# print(users.keys()) # all the keys that is in dictionary
# print(users.values()) # only values
# print(users.items()) # everithing key and value

# member = {'name' : 'Alvo Sirius Potter',
#           'age' : 5,
#           'height' :1.45}


# # users.update({'family': member})
# users['family'].appent(member)
# print(users)

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"

# }
# keys_to_remove = ["name", "salary"]
# for key in keys_to_remove:
#     del sample_dict[key]
# print(sample_dict)

# for loops in dict 

# my_books = {
#     'title': 'harry potter',
#     'author' : 'JK',
# }

# for key, value in my_books.items():
# print

# students = ['lior','david','sveta','nastya']
# for i,j in enumerate(students):
#     print (i,j)
# for name in enumerate(students):
#     print(name)

#zip

# hobbies = ['dance','paint', 'cars','soccer']
# for item in zip(students, hobbies):
#     print(item)
# for item in zip(hobbies, students):
#     print(item)
# print(dict(zip(students,hobbies)))

# for i in range(1,6):
#     print(i)
# else: 
#     print('finished')

# count = 0 
# while count <= 5:
#     print(count)
#     count += 1
# else:
#     print('count is more than 5')

# some_nums = []
# for num in range(11):
#     some_nums.append(num)
# print(some_nums)

# some_nums = [num for num in range(11)]
# print(some_nums)
