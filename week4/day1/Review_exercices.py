#Conditions
#1
# word1 = input('Enter the first word:')
# word2 = input('Enter the second word:')
# word3 = input('Enter the third word:')
# sentence = f'The words you entered are: {word1}, {word2} and {word3}'
# print(sentence)
#2
# list = ['hello', 'world']
# str1 = list[1].upper()
# print(str1)
# str2 = list[0][::-1]
# print(str2)
#3
# names = ['Alice','Max','David','Anastasia']
# print(names[::2])
#4  
##########Almost correct. The insert method is used correctly, but it should use -2 instead of -1 to insert the number second from the end, not at the end.
# my_numbers = [1,2,3,4,5]
# user_numbers = int(input('Enter your number:'))
# my_numbers.insert(-1,user_numbers)
# print(my_numbers)
#5
# my_data = {
#     'first_name' : 'Anastasia',
#     'last_name' :'Skaliy',
#     'age' : 26,
#     'gender' : 'female',
#     'fav_food' : 'sushi'
# }
# print(my_data)
#6
########## Almost correct. The condition checks if the alcohol level is greater than 0.5%, but the text says "less than 0.5%". It should be if alc_level >= 0.5: to match the instruction.
# alc_level = float(input('Please enter your blood alcohol level'))
# if alc_level >0.5 :
#     print(' A user is allowed to drive home if their blood alcohol is less than 0.5 %. Please take a cab')
# else:
#     print('You are allowed to drive.')   
#7
# user_gender = input('Please chooce your gender (Male/Female)')
# user_age = int(input('Please enter your age'))
# if (user_gender.lower() =='male' and user_age >65) or (user_gender.lower() == 'female' and user_age >60):
#     print('It\'s time to retire!')
# else:
#     print('It\'s not time to retire yet')  
