#1
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
    
# class Siamese(Cat):
#     pass

# bengal_cat = Bengal('Bella',3)
# charteux_cat = Chartreux('Vassa',5)
# siamese_cat = Siamese('Sandra',7)
# all_cats = [bengal_cat,charteux_cat,siamese_cat]

# sara_pets = Pets(all_cats)
# sara_pets.walk()

#2
# class Dog:
#     def __init__(self,name,age,weight):
#         self.name = name
#         self.age = age
#         self.weight = weight

#     def bark(self):
#         print(f'{self.name} is barking')   

#     def run_speed(self):
#         run_speed = self.weight/self.age*10     
#         if self.age != 0:
#             return self.weight/self.age*10    
#         else:
#             return 0

#     def fight(self,other_dog):
#         self_result = self.run_speed() * self.weight
#         other_result = other_dog.run_speed() * other_dog.weight
#         if self_result > other_result:
#             return f'{self.name} won the fight'   
#         elif other_result > self_result:
#             return f'{other_dog.name} won the fight'   
#         else:
#             return 'It\'s a tie!'
# dog1 = Dog('Rex', 1, 10)
# dog2 = Dog('Backs', 3, 15)
# dog3 = Dog('Rocks', 6, 20)

# dog1.bark()
# dog2.bark()
# dog3.bark()

# print(f'{dog1.name}\'s running speed:{dog1.run_speed()}')
# print(f'{dog2.name}\'s running speed:{dog2.run_speed()}')
# print(f'{dog3.name}\'s running speed:{dog3.run_speed()}')

# print(dog1.fight(dog2))
# print(dog2.fight(dog3))
# print(dog3.fight(dog1))

#3 in Dogs_domesticated

#4
# class Family:
#     def __init__(self,last_name, members):
#         self.last_name = last_name
#         self.members = members
    
#     def born(self, **kwargs):
#         self.members.append(kwargs)
#         print(f"Congratulations on the birth of a child! {kwargs['name']} was born into the {self.last_name} family.")

#     def is_18(self, name):
#         for member in self.members:
#             if member['name'] == name:
#                 return member['age'] > 18
#         return False   

#     def family_presentation(self):
#         print(f"Family Name: {self.last_name}")
#         print("Members:")
#         for member in self.members:
#             print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Is Child: {member['is_child']}")
# members = [
#     {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
#     {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
# ]

# family = Family('Adams', members) 

# family.born(name='Mia', age=1, gender='Female', is_child=True)
# print(family.is_18('Sarah')) #true
# print(family.is_18('Mia')) #false
# family.family_presentation()

#5
# class TheIncredibles(Family):
#     def __init__(self, last_name, members):
#         super().__init__(last_name, members)

#     def use_power(self, name):
#         for member in self.members:
#             if member['name'] == name:
#                 if member['age'] > 18:
#                     print(f"{member['name']} has the power of {member['power']}")
#                 else:
#                     raise ValueError(f"{member['name']} is under 18 years old and has no power.")

#     def incredible_presentation(self):
#         print("*Here is our powerful family**")
#         super().family_presentation()

# members = [
#     {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
#     {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
# ]

# incredibles_family = TheIncredibles('Incredibles', members)
# incredibles_family.use_power('Sarah')
# incredibles_family.use_power('Michael')

# incredibles_family.incredible_presentation()

# incredibles_family.born(name='Baby Jack', age=1, gender='Male', is_child=True, power='Unknown Power', incredible_name='JackUnknown')

# incredibles_family.incredible_presentation()