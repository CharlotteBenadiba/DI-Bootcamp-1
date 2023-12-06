# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount
    
    # def __add__(self,other):
    #     if type(other) == int:
    #         return self.amount + other
    #     elif self.currency == other.currency:
    #         return self.amount + other.amount
    #     else:
    #         raise TypeError ('Different labels, Give me the same currencies:')
        
    # def __iadd__(self,other):
    #     if type(other) == int:
    #         self.amount += other

    #     elif self.currency == other.currency:
    #         self.amount += other.amount

    #     else:
    #         raise TypeError ('Different labels, Give me the same currencies:')    
        
    #     return self


# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)

# # print(c1+5)
# # print(c1 + c2)
# # print(c1 + c3)
# c1 += 5
# print(c1)

# import math 

# class Circle:
#     def __init__(self,radius, diameter) -> None:
#         self.radius = radius
#         self.diameter = diameter

#     @classmethod
#     def from_radius(cls,radius):
#         return cls(radius = radius, diameter = radius *2)
        
#     @classmethod
#     def from_diameter(cls,diameter):
#         return cls(radius = diameter /2, diameter = diameter)
    

#     def area(self):
#         area = math.pi * self.radius **2
#         return area
    
#     def __str__(self):
#         return f'Circle d: {self.diameter}\n Radius: {self.radius}\n Area: {self.area()}'

#     def __add__(self,other):
#         return self.diameter + other.diameter
    

#     def __gt__(self,other):
#         return self.diameter  > other.diameter
    
#     def __eg__(self,other):
#         return self.diameter  == other.diameter

#     def sort_circles(self,lst:list):
#         lst.append(self)
#         result = sorted(lst)
#         return result


# circle1 = Circle.from_radius(10)
# circle2 = Circle.from_diameter(50)
# circle3 = Circle(10,20)

# print(circle1.diameter)
# print(circle1.radius)
# print(circle1.area())
# print(circle1)
# print(circle1 + circle2)
# print(circle1 > circle2)
# print(circle1 == circle2)

# circles = [circle2,circle3]
# s_cicles = circle1.sort_circles(circles)
# for circle in s_cicles:
#     print(circle.diameter)


# python file i/o

#open a file

# with open('example.txt',encoding = 'utf-8', mode ='r' ) as f:
#     my_line = "hello testing"
#     print(f.read())

# with open('example.txt',encoding = 'utf-8', mode ='w+' ) as f:
#     original_text = f.read()
#     print(original_text)
#     my_line = original_text +'\nhello testing'
#     f.write(my_line)
# def read_file(file_name):
#     with open(file_name,encoding = 'utf-8', mode ='r') as f:
#         file_text = f.read()
#         return file_text


# def read_and_write (file_name, text_add):
#     with open('example.txt',encoding = 'utf-8', mode ='r+' ) as f:
#         f.read()
#         f.write(f'\n{text_add}')
#         final_f = f.readlines()
#         return final_f
# print(read_and_write('example.txt','adding for function'))
# print(read_file())

#exercise

import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file_location = __location__ + '/names.txt'

# with open(file_location,'r' ) as f:
#     text = f.readlines()
#     print(text)

# for i, line in enumerate(text):
#     print(line)  

# print(text[:5])   
# print('step 3', text[:5]) 

# for word in text:
#     splited = []
#     s =word.split()
#     print(s)

# Darth = 0
# Luke = 0 
# Lea = 0
# cleaned_names = list(map(lambda s:s.strip('\n'),text))
# print(cleaned_names)
# Darth = cleaned_names.count('Darth')
# Luke = cleaned_names.count('Luke')
# Lea = cleaned_names.count('Lea')
# print(Darth,Luke,Lea)

# my_name = 'Anastasia'
# with open(file_location,mode = 'a' ) as f:
#     f.write('\n my_name')


# for i, name in enumerate(cleaned_names):
#     if name == "Luke":
#         cleaned_names[i] = f'SkyWalker{name}' 

# print('modified names:\n', cleaned_names)      

#Json and Python 
#convert python dict into jsonfile
import json

my_family = {
    'parents' : ['Beth','James'],
    'children': ['Summer','Mark']
}

json_file = '/family.json'
file_location = __location__ + json_file
with open(file_location, 'w') as file_obj:
    json.dump(my_family, file_obj)

#retrieve json data
json_file = '/family.json'
file_location = __location__ + json_file
with open(file_location, 'r') as file_obj:
    my_family2 = json.load(file_obj)

print(my_family2)    
