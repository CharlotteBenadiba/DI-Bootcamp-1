#1
# my_fav_numbers = {1,3,7,8}
# print(my_fav_numbers)
# my_fav_numbers.add(11)
# my_fav_numbers.add(21)
# print(my_fav_numbers)
# my_fav_numbers.remove(21)
# print(my_fav_numbers)
# friend_fav_numbers = {2,5,9}
# our_fav_numbers = ()
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

#2
#No, because tuples are immutable lists, which means items can’t be changed.

#3
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# print(basket)
# basket.remove("Blueberries")
# print(basket)
# basket.append("Kiwi")
# print(basket)
# basket.insert(0,"Apples")
# print(basket)
# print(basket.count("Apples"))
# basket.clear()
# print(basket)

#4
# (1)
# # An integer (more commonly called an int) is a number without a decimal point.
# # A float is a floating-point number, which means it is a number that has a decimal place.
# # (2)
# x = 1.5
# l = [x]
# for i in range (0,7):
#     x = x+0.5
#     l.append(x)
# print(l)        
# # (3) for i in range(0, 1, 0.1): #start,stop, step

#5

# for i in range(1,21):
#     print(i)

# for i in range(1,21):
#     if i % 2 :
#         print(i)

#6
# my_name = 'Anastasia'
# users_name = ""
# while users_name != my_name:
#     users_name = str(input('What\'s your name?'))
#     if users_name == my_name:
#         print('We have the same name')        


#7
# users_fav_fruit = str(input('What\'s your favorite fruit(s)? Please separate the fruits with a single space'))
# list_fruits = users_fav_fruit.split()
# print(list_fruits)
# any_fruit = str(input('Input a name of any fruit'))
# if any_fruit in list_fruits:
#     print('You chose one of your favorite fruits! Enjoy!')
# else:
#     print('You chose a new fruit. I hope you enjoy')

#8
# pizza_top_list = []
# pizza_top =''
# while pizza_top!= 'quit': 
#     pizza_top = input("Please enter a series of pizza toppings (enter 'quit'  when you are finished): ")
#     if pizza_top != 'quit':
#         print('We will add that topping to your pizza')
#         pizza_top_list.append(pizza_top)
# print('All the toppings on the pizza pie are', [pizza_top_list])
# price = 10 + 2.5 * len(pizza_top_list)
# print('The total price is ', price)

#9
# age = (input('Write the age of each person who wants a ticket'))
# total_cost = int 
# if age < 3 :
#     total_cost = 0
# elif age < 12:
#     total_cost = 10
# else:
#     total_cost = 15
# print('The total cost is', total_cost)




#10
# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
# while "Pastrami sandwich" in sandwich_orders:
#     sandwich_orders.remove('Pastrami sandwich')
# print(sandwich_orders)
# finished_sandwiches = []


