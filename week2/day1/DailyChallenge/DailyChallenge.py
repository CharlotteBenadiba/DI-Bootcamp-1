
# class Farm:
#     def __init__(self,name):
#         self.name = name
#         self.animals = {}
#     def add_animal(self, new_animal, quantity = 1):
#         if new_animal in self.animals:
#             self.animals[new_animal] += quantity
#         else:
#             self.animals[new_animal] = quantity

#     def get_info(self) :
#         info = f"{self.name}'s farm\n\n"
#         for new_animal, quantity in sorted(self.animals.items()):
#             info += f"{new_animal} : {quantity}\n\n"    
#         return info 
    
#     def get_animal_types(self):
#         return sorted(list(self.animals.keys()))

#     def get_short_info(self):
#         animal_types = self.get_animal_types()
#         animal_string = ", ".join(animal_types)
#         return f"{self.name}'s farm has {animal_string}."

    
# macdonald = Farm("McDonald")        
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
# print('    E-I-E-I-O')   
# print(macdonald.get_animal_types())
# print(macdonald.get_short_info())