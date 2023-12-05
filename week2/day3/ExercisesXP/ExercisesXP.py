#1
# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     def __str__(self):
#         return f'{self.amount} {self.currency}s'  
#     def __int__(self):
#         return self.amount
#     def __repr__(self):
#         return f"{self.amount} {self.currency}s"
#     def __add__(self, other):
#         if isinstance(other, Currency):
#             if self.currency != other.currency:
#                 raise TypeError(f"Cannot add between Currency type {self.currency} and {other.currency}")
#             return Currency(self.currency, self.amount + other.amount)
#         else:
#             return Currency(self.currency, self.amount + other)
#     def __iadd__(self, other):
#         if isinstance(other, Currency):
#             if self.currency != other.currency:
#                 raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#             self.amount += other.amount
#         else:
#             self.amount += other
#         return self

#     def __radd__(self, other):
#         return self.__add__(other)    




# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)      

# print(str(c1))
# print(int(c1))
# print(repr(c1))
# print(c1+5)
# print(c1 + c2)
# print(c1) 
# c1 += 5
# print(c1)
# c1 += c2
# print(c1)
# print(c1 + c3) #TypeError

#2
#in func and exercise_one

#3
# import string
# import random

# def random_str(length=5):
#     letters = string.ascii_letters
#     return ''.join(random.choice(letters) for _ in range(length))

# print(random_str())

#4
# from datetime import datetime

# def current_date():
#     current_date = datetime.now().date()
#     print(f"The current date is: {current_date}")

# current_date()

#5
# from datetime import datetime

# def time_left():
#     current_date = datetime.now()
#     january_1st = datetime(current_date.year + 1, 1, 1)
#     time_dif = january_1st - current_date
#     days = time_dif.days
#     hours, remainder = divmod(time_dif.seconds, 3600)
#     minutes, seconds = divmod(remainder, 60)
#     print(f"The 1st of January is in {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")

# time_left()

#6
# from datetime import datetime

# def minutes_lived(birthdate):
#     birth_datetime = datetime.strptime(birthdate, '%Y-%m-%d')
#     current_datetime = datetime.now()

#     difference = current_datetime - birth_datetime
#     minutes = difference.total_seconds() / 60

#     print(f"You have lived approximately {minutes} minutes.")

# birthdate = input("Enter your burthdate in 'YYYY-MM-DD' format")
# minutes_lived(birthdate)

#7
pip install Faker

from faker import Faker

fake = Faker()
users = []

def add_fake_user():
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code()
    }
    users.append(user)

for _ in range(3):
    add_fake_user()
for user in users:
    print(user)
    