# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# cat1 = Cat('Murka',3)
# cat2 = Cat('Sandra',10)
# cat3 = Cat('Richy',5)

# cats_l = [cat1,cat2,cat3]

# def oldest(cats_l:list):
#     temp = [cats_l[0]]
#     for cat in cats_l:
#         if cat.age > temp[0].age:
#             temp[0] = cat
#     return temp

# oldest_cat = oldest(cats_l)
# print (f'The oldest cat is: {oldest_cat[0].name} and it is {oldest_cat[0].age} years old')     

# def oldest_max(cats:list):
#     for cat in cats:
#         old_cat = max(cats, key = lambda cat: cat.age)
#     return old_cat
# old_cat = oldest_max(cats_l)

# print (f'The oldest cat is: {old_cat.name} and it is {old_cat.age} years old')  

#INHERITANCE
# class Animal:
#     def __init__(self, name, family,legs):
#         self.name = name
#         self.family = family
#         self.legs = legs
    
#     def make_sound(self):
#         print(f'{self.name} is making a sound.')

# class Dog(Animal):
#     def __init__(self, name, family, legs, trained ='False'): # i add smth only to child
#         super().__init__( name, family, legs)
#         self.trained = trained

#     def make_sound(self):
#         print(f'{self.name} is barking.')

#     def fetch_ball(self):
#         print(f'{self.name} fetched the ball')

#     def give_paw(self):
#         if self.trained:
#             print(f'{self.name} gives the paw')
#         else:
#             print(f'{salf.name} is not trained')        

        

# animal1 = Animal('Bobo','Felidae',4)
# print(animal1.family)

# dog1 =Dog('Rex','Canidae',4)
# print(dog1.trained)
# dog1.make_sound()
# animal1.make_sound()
# # animal1.fetch_ball() #dosn't work because in child class
# dog2 = Dog('Lassy','Canidae', 4, True)
# dog2.give_paw()

# class Door:
#     def __init__(self, is_opened):
#         self.is_opened = is_opened
#         print('the door is close')

# class BlockedDoor:
#     def open_door(self) :
#         raise Exception ('Blocked door cant be open')
    
#     def close_door(self):
#         raise Exception ('Blocked door cant be open')

# new_door = Door(True)
# new_door.open_door
# new_door.close_door

# print(new_door.is_opened)

# blocked_Door = BlockedDoor(False)
# blocked_Door.open_door()
# blocked_Door.open_door()


# class AtmAccount:
#     available_acc_num = 2000
#     def __init__(self, holder) -> None:
#         self.__holder = holder #private 
#         self.__account_num = AtmAccount.available_acc_num
#         self.__balance = 0
#         AtmAccount.available_acc_num += 1

#     @property   
#     def balance(self):
#         return self.__balance #i'm giving an access 
    
#     @balance.setter
#     def balance(self, amount): #i'm giving permition to change smth inside
#         self.__balance = amount

#     def deposit(self,amount):
#         self.__balance += amount
#         return self.balance

#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise ValueError('Insufficient balance')
#         else:
#             self.balance -= amount  

# account1 = AtmAccount('Anastasia S.')
# account2 = AtmAccount('John P.')
# account3 = AtmAccount('Leo DiCaprio.')

# print(account1._AtmAccount__account_num)
# print(account2._AtmAccount__account_num)
# print(account3._AtmAccount__account_num)

# account1.deposit(200)
# account1.withdraw(500)
# print(account1.balance)