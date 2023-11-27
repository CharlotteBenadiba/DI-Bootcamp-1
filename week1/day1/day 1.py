print('hello world in python')
print(dir(42))
print(5%10)
print('hello'.replace('hello','hi'))
print(10-5.5)
# my_age = 26
cars = 100 #amount of cars, int
space_in_a_car = 4.0 #amount of space in car
drivers = 30 #amount of drivers, int
passengers = 90 #amount of passengers, int
cars_not_driven = cars - drivers #amount of cars without drivers 
cars_driven = drivers #amount of cars which are driven, with driwers
carpool_capacity = cars_driven * space_in_a_car #capacity in all driven cars
average_passengers_per_car = passengers / cars_driven #average amount of passengers in all driven cars


print("There are", "{ }".format(cars), "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")

