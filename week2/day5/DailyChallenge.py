#1 

#1 
#Class is a blueprint or a template for creating objects. 
#It defines the attributes (variables) and methods (functions) that the objects will have.
#Think of a class as a way to encapsulate data and behavior into a single unit.
#2
#Instance refers to a specific realization or individual occurrence of a class.
#When you create an object from a class, you're creating an instance of that class.
#It's a concrete occurrence of the class, with its own unique attributes and methods.
#3
# Encapsulation is a fundamental concept in object-oriented programming (OOP) that refers to the bundling of data (attributes) and the methods (functions) that operate on that data within a single unit(a class).memoryview
# The main idea behind encapsulation is to hide the internal state and functionality of an object from the outside world while providing controlled access to that object. This is often achieved by setting access levels to the attributes and methods within a class.
# Could be: public, private and protected.
#4
# Abstraction is a fundamental principle that involves emphasizing essential details and hiding unnecessary information, providing users with a simplified and more manageable interface. 
#In OOP, abstraction is achieved by creating abstract classes and interfaces that define a blueprint for other classes. These abstract classes contain abstract methods that must be implemented by their concrete subclasses.
#5
#Inheritance is a core concept in object-oriented programming (OOP) that allows a new class (called a subclass or derived class) to inherit properties and behaviors (attributes and methods) from an existing class (called a superclass or base class).
#This enables code reusability and promotes the creation of a hierarchy of classes.
#6
#Multiple inheritance refers to the capability of a Python to create a new class by inheriting attributes and methods from more than one base class or superclass. This means a subclass can inherit from multiple parent classes.
#7
# Polymorphism refers to the ability of different objects to be treated as objects of a common superclass. It allows different classes to be used through a common interface, providing a way to perform a single action in different ways based on the object's type.
#8
#Method Resolution Order in Python refers to the order in which Python searches for methods and attributes in a class hierarchy. It's crucial for determining which method or attribute is accessed when dealing with inheritance, especially in scenarios involving multiple inheritance.

#2
# import random

# class Card:
#     def __init__(self, suit, value):
#         self.suit = suit
#         self.value = value

#     def __repr__(self):
#         return f"{self.value} of {self.suit}"

# class Deck:
#     def __init__(self):
#         self.cards = []
#         self.generate_deck()
#         self.shuffle()

#     def generate_deck(self):
#         suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
#         values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
#         for suit in suits:
#             for value in values:
#                 self.cards.append(Card(suit, value))

#     def shuffle(self):
#         random.shuffle(self.cards)

#     def deal(self):
#         if not self.cards:
#             return "No cards left in the deck"
#         return self.cards.pop()

# my_deck = Deck()

# print("Initial deck:")
# print(my_deck.cards)

# print("\nShuffling the deck...")
# my_deck.shuffle()
# print("Shuffled deck:")
# print(my_deck.cards) 

# print("\nDealing cards:")
# for i in range(5):  # Dealing 5 cards
#     dealt_card = my_deck.deal()
#     print(f"Dealt card: {dealt_card}")

# print("\nRemaining deck:")
# print(my_deck.cards) 