# tasks = input('enter ur tasks by comma: ').split(', ')
# print(tasks)

# s_tasks = sorted(tasks)
# print(tasks, 'sorted', s_tasks)

# tasks.sort()
# print( 'after', tasks)

# holiday_tasks = ['order', 'buy', 'love']
# tasks.extend(holiday_tasks)
# print(tasks)

# print(tasks + holiday_tasks)

# all_tasks = [*tasks, *holiday_tasks]
# print(all_tasks)

# fruits = {'apple', 'banana', 'orange', 'lime','tomatos'}
# vegetables = {'carrot', 'tomatos', 'broccoli'}

# common = fruits.intersection(vegetables)
# print(common)

# grocery_list = fruits.union(vegetables)
# print('grocery-list', grocery_list)

# point =(3,5)
# point2 = tuple()

# x,y =(3,5)
# print(x)
# print(y)

# print(point[0])
# print(point[1])

# users ={'basic-info':{'name':'Alice',
#         'age':20,
#         'email' : "alice@gmail.com" },
#         'scores': [100,255,345]
#         }
# print(users['basic-info']['name'])
# print(users['scores'][-1])        
# print(users['scores'].remove(255))
# # print(users)

# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }

# wallet = "$300"

# can_buy = []
# for product, price in items_purchase.items():
#     #cleaning the data
#     price_clean = price.strip('$').replace(',','')
#     wallet_clean = wallet.strip('$')

#     #converting to int

#     price_clean = int(price_clean)
#     wallet_clean = int(wallet_clean)

#     #cheking
#     if price_clean > wallet_clean:
#         continue
        
#     else:
#         can_buy.append(product)
#         wallet_clean =- price_clean


# print(f' You can buy: {can_buy} and you have {wallet_clean} dollars')


#functions

# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }

# wallet = "$300"

# def can_afford(wallet:str, items_dict:dict) -> None:
#     can_buy = []
   
#     wallet_clean = wallet.strip('$')

#     for product, price in items_dict.items():
#         price_clean = price.strip('$').replace(',','')
        
#     #converting to int

#         price_clean = int(price_clean)
#         wallet_clean = int(wallet_clean)

#     #cheking if i can affort
#         if price_clean > wallet_clean:
#             continue
        
#         else:
#             can_buy.append(product)
#             wallet_clean =- price_clean
#     return print(f' You can buy: {can_buy} and you have {wallet_clean} dollars')

# def say_hello(username, language):
#     if language == "EN":
#         print("Hello "+username)
#     elif language == "FR":
#         print("Bonjour "+username)
#     else:
#         print("This language is not supported: " + language)

# username = "Rick"
# language = "FR"
# say_hello(username, language) #variable arguments
# say_hello("Rick","FR")
# say_hello(username="Rick", language="FR") # keyword arguments
# say_hello("Rick",language="EN") #mixed: 1st has to be positional (nor username = 'rick', 'en')


#DEFAULT VALUE
# def say_hello(username, language = 'EN'):
#     if language == "EN":
#         print("Hello "+username)
#     elif language == "FR":
#         print("Bonjour "+username)
#     else:
#         print("This language is not supported: " + language)

# say_hello('Anastasia')     

# def square(number: int) -> int:
#     num_squared = number **2
#     return num_squared
# print(square(2))

# def country_info(country):
    
#     if country == 'Israel':
#         population = 9364000
#         capital = 'Jerusalem'
#     if country == 'Ukraine':
#         population = 14340000
#         capital = 'Kuiv'
#     if country == 'Brazil':
#         population = 214300000
#         capital = 'brazilia'
#     return population, capital 
# a,b = country_info('Israel')       
# print(f'The population is {a} and the cap is {b}')

# def calculation (a:int,b:int) -> tuple:
#     sum = a+b
#     subtrac = a-b
#     return (sum, subtrac)
# print(calculation(10,3))


#ARGS AND KWARGS
# def print_names (*args):
#     for i in args:
#         print(i)
# # args = *        
# print_names ('David','Anna','Nastya')    


# KWARGS = *  KEY WORD ARGUEMENT (** key and value)
# def print_info(**kwargs):
#     print(kwargs) 
# print_info(address = (5,7), score = [25,47,899])

# def print_info(**kwargs):
#     print(kwargs['address'])
# print_info (namy = 'David',age = 25, address = 'Holon')   

# def gamer_info(*args,**kwargs):
#     print(max(args))
#     print(kwargs)
# gamer_info(150,123,544,534, name ='John', l_name = 'Doe', age = 23)    

#FUNCTION INSIDE FUNCTION

# def country_info(country):
    
#     if country == 'Israel':
#         population = 9364000
#         capital = 'Jerusalem'
#         squared_pop = square(population)
#     if country == 'Ukraine':
#         population = 14340000
#         capital = 'Kuiv'
#     if country == 'Brazil':
#         population = 214300000
#         capital = 'brazilia'
#     return population,squared_pop, capital 
# pop, squ = country_info('Israel')       
# print(f'The population is {a} and the cap is {b}')

#LAMBDA
def upper_s(strings_enter):
    after_upper = []
    for string in strins_enter:
        string = string.upper()
        after_upper.append(string)

my_function = lambda s: s.upper()
print()

fruit =['Apple','Banana','Pear','Appricot','Orange']

map_result = map(lambda s: s.upper(), fruit)
# print(list(map_result))
# print(tuple(map_result))


print(dict(zip(map_result, fruit )))

filter_object = filter(lambda s: s[0] == 'A', fruit)
print(list(filter_object))

from functools import reduce
nums = [1,2,5,8,7,9,10]
redused = reduce(lambda n1, n2 : n1+n2, nums)
print(redused)