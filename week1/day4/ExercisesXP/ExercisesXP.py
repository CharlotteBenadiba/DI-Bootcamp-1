# 1
# def display_message():
#     themes = ['Python','SQL','Data base','Power BI']
#     message = f'We learn such themes in this course: {', '.join(themes)} .'
#     return message
# print(display_message())

# 2
# def favorite_book(title):
#     message = f'One of my favorite books is {title}.'
#     return message
# print(favorite_book('Alice in Wonderland'))

# 3
# def describe_city(city,country = 'Israel'):
#     message = f'{city} is in {country}.'
#     return message
# print(describe_city('Mykolaiv','Ukraine'))    
# print(describe_city('Mykolaiv'))    

#4
# import random
# def numbers (num):
#     if num < 1 or num >100:
#         return "Please enter a number between 1 and 100."
#     random_number = random.randint(1,100)
#     print(f'Random number is {random_number}.')

#     if num == random_number:
#         return 'Success! You guessed the right number'
#     else:
#         return f"Sorry, it's a miss! Your guess was {num} and the random number was {random_number}."
    
# user_guess = int(input('Guess the number between 1 to 100.'))
# result = numbers(user_guess)
# print(result)

#
# def make_shirt(size : str, text : str):
#     sentence = f'The size of the shirt is {size} and the text is {text}'
#     return sentence
# print(make_shirt('small','hi'))

# def make_shirt(size = 'large', text = 'I love Python'):
#     sentence = f'The size of the shirt is {size} and the text is {text}'
#     return sentence
# print(make_shirt())
# print(make_shirt('medium'))
# print(make_shirt('small', 'Hello World'))
# print(make_shirt(size = 'small', text = 'Hi!'))

#6
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# def show_magicians(magicians):
#     for magician in magicians:
#         return magician_names
# print(show_magicians(magician_names))    

# def make_great(magicians):
#     for i in range(len(magicians)):
#         magicians[i] += " the Great"

# make_great(magician_names)
# print(magician_names)

#7
# import random

# def get_random_temp(season = None):
#     low =-10
#     high = 40
#     if season == 'Winter' :
#         high = 16 
#     random_temp = random.uniform(low, high)
#     return random_temp
    

# random_temp = get_random_temp()
# print(f"The random temperature is: {random_temp} degrees Celsius")

# def main():
#     monthes = { 1: 'winter',
#                2: 'winter',
#                3: 'spring',
#                4: 'spring',
#                5: 'spring',
#                6: 'summer',
#                7: 'summer',
#                8: 'summer',
#                9: 'autumn',
#                10: 'autumn',
#                11: 'autumn',
#                12: 'winter',
#     }
#     # season = input('Write a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.')
#     month = int(input('Enter the number of the month (1 = January, 12 = December)'))
#     season = monthes[month]
#     random_temp = get_random_temp(season)
#     print(f"The temperature right now is {random_temp} degrees Celsius.")
#     if random_temp < 0:
#         print('Brrr, that’s freezing! Wear some extra layers today')
#     elif random_temp >0 and random_temp <16:
#         print('Quite chilly! Don’t forget your coat') 
#     elif random_temp >16 and random_temp <23:
#         print('Perfect weather!')           
#     elif random_temp >24 and random_temp <32:
#         print('It\'s hot. Remember drink water') 
#     else:
#         random_temp >32 and random_temp <40 
#         print('It\'s hot. Stay under conditioner') 

# main()


#8
# data = [
#     {
#         "question": "What is Baby Yoda's real name?",
#         "answer": "Grogu"
#     },
#     {
#         "question": "Where did Obi-Wan take Luke after his birth?",
#         "answer": "Tatooine"
#     },
#     {
#         "question": "What year did the first Star Wars movie come out?",
#         "answer": "1977"
#     },
#     {
#         "question": "Who built C-3PO?",
#         "answer": "Anakin Skywalker"
#     },
#     {
#         "question": "Anakin Skywalker grew up to be who?",
#         "answer": "Darth Vader"
#     },
#     {
#         "question": "What species is Chewbacca?",
#         "answer": "Wookiee"
#     }
# ]

# def ask_questions(questions):
#     while True:
#         correct_answers = 0
#         incorrect_answers = 0
#         wrong_answers = []

#         for question_set in questions:
#             question = question_set["question"]
#             answer = question_set["answer"]
            
#             user_answer = input(question + " ")

#             if user_answer.lower() == answer.lower():
#                 print("Correct!")
#                 correct_answers += 1
#             else:
#                 print(f"Incorrect! The correct answer is: {answer}")
#                 incorrect_answers += 1
#                 wrong_answers.append({
#                     'user_answer' : user_answer,
#                     'question' : question,
#                     'correct_answer' : answer
#                 })


#         print("\nQuiz Summary:")
#         print(f"Correct Answers: {correct_answers}")
#         print(f"Incorrect Answers: {incorrect_answers}")
#         print(f"List of Wrong Answers: {wrong_answers}")

#         if incorrect_answers > 3:
#             print("\nYou had more than 3 wrong answers. Would you like to play again?")
#             play_again = input("Type 'yes' to play again: ")
#             if play_again.lower() == 'yes':
#                 continue
#             else:
#                 print("Thank you for playing!")
#                 break
#         return

# ask_questions(data)

