#1
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# cat1 = Cat('Murka',3)
# cat2 = Cat('Sandra',10)
# cat3 = Cat('Richy',5)

# def oldest_cat(*cats):
#     max_value = max(cats, key =lambda cat: cat.age)
#     return max_value
# oldest_cat = oldest_cat(cat1,cat2,cat3)
# print(f'The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.')

#2
# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
    
#     def bark(self):
#         print(f"{(self.name)} goes woof!")  

#     def jump(self):
#         x = self.height *2
#         print(f"{(self.name)} jumps {x} cm high!")   

# davids_dog = Dog('Rex',50)          
# print(davids_dog.name, davids_dog.height)
# davids_dog.bark()
# davids_dog.jump()


# sarahs_dog = Dog('Teacup', 20)
# print(sarahs_dog.name, sarahs_dog.height)
# sarahs_dog.bark()
# sarahs_dog.jump()


# if davids_dog.height > sarahs_dog.height:
#     print (f"The name of the bigger dog is:{davids_dog.name}")
# elif sarahs_dog.height > davids_dog.height:
#     print (f"The name of the bigger dog is:{sarahs_dog.name}")  
# else:
#     print ('All dogs have the same height')     

#3
# class Song:
#     def __init__(self,lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()

#4
# class Zoo:
#     def __init__(self,name):
#         self.name = name
#         self.animals = []
#         self.grouped_animals = {}
#     def add_animal(self, new_animal):
#         if new_animal in self.animals:
#             pass
#         else:
#             self.animals.append(new_animal)
#         return self.animals    
#     def get_animals(self):
#         print(f'All the animals in the Zoo are : {self.animals}.')
#     def sell_animal(self, animal_sold):
#         if animal_sold in self.animals:
#             self.animals.remove(animal_sold)
#         return print(f'An updated list of all the animals in the Zoo is : {self.animals}.')
  
#     def sort_animals(self):
#         sorted_animals = {}
#         self.animals.sort()
        
#         groups = set()
#         for animal in self.animals:
#             groups.add(animal[0])

#         for animal in self.animals:
#             key = animal[0] 
#             if key not in sorted_animals:
#                 sorted_animals[key] = [animal]
#                 continue
#             sorted_animals[key].append(animal)


#         index = 1
#         temp = {}
#         for key in sorted_animals.keys():
#             temp[index] = sorted_animals[key]
#             index = index +1
#         self.grouped_animals = temp
#         print(self.grouped_animals)    

#     def get_groups(self):
#         for key in self.grouped_animals:
#             print(f' Group {key} containce: {','.join(self.grouped_animals[key])}')
               
# ramat_gan_safari = Zoo("Ramat Gan Safari")

# ramat_gan_safari.add_animal("Ape")
# ramat_gan_safari.add_animal("Baboon")
# ramat_gan_safari.add_animal("Bear")
# ramat_gan_safari.add_animal("Cat")
# ramat_gan_safari.add_animal("Cougar")
# ramat_gan_safari.add_animal("Eel")
# ramat_gan_safari.add_animal("Emu")

# ramat_gan_safari.get_animals()

# ramat_gan_safari.sell_animal("Cat")

# ramat_gan_safari.sort_animals()

# ramat_gan_safari.get_groups()
