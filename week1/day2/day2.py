#list
# list1 = [5, 10, 15, 20, 25, 50, 20]
# print(list1.index(20))
# if 20 in list1:
#     index20 = list1.index(20)
#     list1.remove(20)
#     list1.insert(index20,200)
# print(list1)
# index20 = list1.index(20)
# list1.remove(20)
# list1.insert(index20,200)
# print(list1)

#for loop
# students = ('Lior','Sveta','Estee','David')
# for each_students in students:
#     if each_students is 'Sveta':
#         print('Happy birthday,Sveta')
#     else:
#         print(f'hello,{each_students}')

# for i in range(1,11):
#     print(i)

# for i in range(11): #the last number
#     print(i)  

# l = list(range(1,11))
# print(l)

# print(sum(l))

# result = 0
# for i in sum(l):
#     result +=i
# print(result)

# #exercise
# num = int(input('Print your number'))
# for i in range(1,11):
#     print(num,'x',i,'=',num*i)

# c = 1
# while c <= 5:
#     print('python')
#     c += 1

# user_str = str(input('give me a word 10 chars'))
# while len(user_str) != 10:
#     user_str = str(input('give me a word'))
# else:
#     print('perfect word')

# user_str = str(input('give me a word 10 chars'))
# while len(user_str) != 10:
#     user_str = str(input('give me a word'))
#     if user_str =='quit':
#         print('thanks for playing')
#         break
#     else:
#         print ('bye')

# num = 1
# while num <= 10:
#     print(num)
#     num += 1 

# students = ('Lior','Sveta','Estee','David')
# for i,j in enumerate(students):
#     if i ==2:
#         print(j)

current_number = 0
while current_number <= 10:
    current_number += 1
    if 3 < current_number < 7: 
        continue                # Go back to the beginning of the loop
    print(current_number)