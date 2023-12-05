# class Pagination:
#     def __init__(self, items, pageSize):
#         self.items = items
#         self.pageSize = int(pageSize)
#         self.current_page = 1
#         self.total_pages = len(self.items) // self.pageSize +1

#     def getVisibleItems(self):
#         end_index = self.pageSize * self.current_page
#         start_index = end_index - self.pageSize
#         currentpg = self.items[start_index:end_index]
#         print(currentpg)
    
#     def nextPage(self):
#         if self.current_page == self.total_pages:
#             self.current_page = 1
#         else:
#             self.current_page += 1
#         return self

#     def prevPage(self):
#         self.current_page -= 1
#         return self

#     def firstPage(self):
#         self.current_page =1
#         return self
    
#     def lastPage(self):
#         self.current_page = len(self.items) // self.pageSize +1
#         return self

#     def goToPage(self,pageNum):
#         self.current_page = pageNum
#         return self



# alphabetList = list("abcdefghijklmnopqrstuvwxyz")
# print(alphabetList)

# p = Pagination(alphabetList, 4)   
# p.getVisibleItems()
# p.getVisibleItems()
# p.nextPage().nextPage()
# p.getVisibleItems()
# p.nextPage()
# p.getVisibleItems()
# p.nextPage()
# p.getVisibleItems()
# p.lastPage()
# p.getVisibleItems()
# p.goToPage(4)
# p.getVisibleItems()

#   exceptions
# def divide(x,y):
#     try:
#         result = x/y
#     except TypeError:
#         print('one of the arg is not int') 
#     except:
#         raise ZeroDivisionError ("can't divide by zero")       
#     else:
#         print(result)
# print(divide(5,0))    
# print(divide('e',4)) 
# print(divide(20,4))     

# my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]
# def sum_list(some_list):
#     try:
#         result = sum(some_list)

#     except TypeError:
#         print('mixed values')
#         raise
#     else:
#         print(result)
# sum_list(my_list)

# from googletrans import Translator

# def translate():
#     french_words = ['bonjour','mercy']
#     translator = Translator()
#     translated_en = {}

#     for word in french_words:
#         try:
#             translation = translator.translate(word)
#             translated_en.update({word : translation})
#         except Exception:
#             translated_en.update({word : 'unvailable translation'})    

#     print(translated_en)    
# translate()    

#CLASS ATTRIBUTE

# class Circle:
#     color = "red"

#     def __init__(self, diameter):
#         self.diameter = diameter

#     def grow(self, factor=2):
#         self.diameter = self.diameter * factor

#     def get_color(self):
#        return Circle.color
    
#     def change_color(self,color):
#         self.color = color

# circle1 = Circle(2)
# print(circle1.color)
# circle1.change_color('blue')
# print(circle1.color)
# print(Circle.color)
# print(circle1.get_color())
# circle1.grow(3)
# print(circle1.diameter)

#DECORATORS

# class MyClass:
#     def __init__(self,val) -> None:
#         self.val = self.filterint(val)

#     @staticmethod    
#     def filterint(val):
#         if not isinstance(val, int):  
#             raise TypeError
#         else:
#             return val
# a = MyClass(5)   
# print(a.val)

# b = MyClass('100')
# print(b.val)


class AtmAccount:
    available_acc_num = 2000
    def __init__(self, holder) -> None:
        self.__holder = holder #private 
        self.__account_num = AtmAccount.available_acc_num
        self.__balance = 0
        AtmAccount.available_acc_num += 1

    @property   
    def balance(self):
        return self.__balance #i'm giving an access 
    
    @balance.setter
    def balance(self, amount): #i'm giving permition to change smth inside
        self.__balance = amount

    def deposit(self,amount):
        AtmAccount.validate_amount(amount)
        self.__balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Insufficient balance')
        else:
            self.balance -= amount  
    @staticmethod #function just inside the class, usuaaly to do some math in attribute, to check values
    def validate_amount(amount):
        if amount <= 0:
            raise ValueError("Can't be negative or 0 ")      
        else:
            return amount
        
    @classmethod    # is related to the class and can be called directly  
    def get_next_acc_num(cls):
        if cls.available_acc_num > 2000:
            cls.available_acc_num += 1000
        return cls.available_acc_num
    
    def __str__(self):
        output = f'''Account_Number: {self.__account_num}\nHolder: {self.__holder}\nBalance: {self.balance}'''
        return output
    
    # def __add__(self,amount):
    #     self.deposit(amount)
    #     return self.balance
    
    def __iadd__(self,amount):
        self.deposit(amount)
        return self.balance


account1 = AtmAccount('Anastasia S.')
account2 = AtmAccount('John P.')
account3 = AtmAccount('Leo DiCaprio.')

# print(account1._AtmAccount__account_num)
# print(account2._AtmAccount__account_num)
# print(account3._AtmAccount__account_num)

account1.deposit(500) #gives a ValueError if <0
account1.withdraw(100)
account2.deposit(500)

# print(account1)
account1 += 500

print(dir(account1))


# all_account = [account1,account2,account3]
# print(len(all_account))

# print(AtmAccount.available_acc_num)
# print(AtmAccount.get_next_acc_num())

# some_num = 5
# print(type(some_num))
# print(type(account1))

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.used_names.add(name)

#     def __call__(self):
#         print ('Person: {}, Age: {}'.format(self.name, self.age))

#     @classmethod
#     def fromYear(sld,name, birth_year):
#         THIS_YEAR = 2023
#         return cls(name, THIS_YEAR - birth_year)
    
#     @property
#     def prof_name(self):
#         return "Mr" +self.name

# joe = Person('John',45)
# print(joe.used_names)
# an_age =Person.fromYear("Ana",1997)
# print(an_age.age)
