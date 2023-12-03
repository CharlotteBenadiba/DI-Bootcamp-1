#exc from the last week 

# mag_names = ['Harry Potter', 'David Bleine','Griss Angel']

# def show_magicians():
#         print(','.join(mag_names))

# show_magicians()    

# def make_great():
#     for i, name in enumerate(mag_names):
#           mag_names[i] = 'The Great ' + name
               
# make_great()
# show_magicians()        

#CLASSES

# class Dog():
    
#     def __init__(self, name, color, height, weight,fav_toys):
#         print('An object was created')
#         self.name = name
#         self.color = color
#         self.height = height
#         self.weight = weight
#         self.fav_toys = fav_toys
    
#     def bark(self):
#         print(f"{(self.name)} barks ! WAF")  

#     def walk(self,distance:int):
#         print(f'{self.name} walks {distance} km')    

#     def rename(self, new_name):
#         self.name = new_name     
#         return self.name

 #dianas dog before we had __init   
# dianas_dog = Dog() #when we had no __init__ before, so it printed the name. 
# dianas_dog.name = "Leto"
# print(dianas_dog.name)

  #alex and john dogs with __init__

# Alex_dog = Dog('Rex','beige','30','10', ['ball','mouse','shoe'])
# print(Alex_dog.name, Alex_dog.color, Alex_dog.height, Alex_dog.weight)
# print(Alex_dog.__dict__)
# Alex_dog.fav_toys.append('rope')
# print(Alex_dog.fav_toys)

# john_dog = Dog('Flufy','white','50','20')
# john_dog.bark()
# Alex_dog.walk(5)
# Alex_dog.rename('Korn')
# print(Alex_dog.name)

# dianas_dog = Dog('Leto','brown and white','40','5')

# all_dogs = [Alex_dog, john_dog, dianas_dog]

# for dog in all_dogs:
#     print(dog.name)

# for dog in all_dogs:
#     dog.bark()  

#     #or(listo of names)
# all_dogs = [Alex_dog.name, john_dog.name, dianas_dog.name]    
# print(all_dogs)
# class Person():
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def show_details(self):
#     print("Hello my name is " + self.name)

# first_person = Person("John", 36)
# first_person.show_details()

from datetime import date 
import random

class BankAccount:
    def __init__(self, account_num, balance = 0) -> None:
        self.account_num = account_num
        self.balance = balance
        self.transaction = []

    def view_balance(self):
        print(f'The balance for {self.account_num} is {self.balance}') 
        self.transaction.append(f' {date.today()}:view_balance')   

    def deposit(self, dep_amount):
        if dep_amount <= 0:
            print('Invalid amount')
        elif dep_amount < 50:
            print('Minimum deposit is 100')
        else:      
            self.balance += dep_amount  
            self.view_balance()  
            self.transaction.append(f' {date.today()}:view_balance')
    def withdraw(self, w_amount):
        if w_amount > self.balance:
            print('Insufficient amount')
        else:
            self.balance -= w_amount
            self.view_balance()
            self.transaction.append('withdraw')


    def view_transactions(self):
        print('\n'.join(self.transaction))        
        

account1 = BankAccount(1234567, 500)

account1.deposit(300)
account1.view_balance()

account1.withdraw(100)
account1.view_balance()

account1.view_transactions()



        
                