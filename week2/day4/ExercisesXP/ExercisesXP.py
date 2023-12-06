import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

 #2
# import json
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""
# jsn = json.loads(sampleJson)
# print(jsn['company']['employee']['payable']['salary'])
# jsn['company']['employee']['birth_date'] = '1.1.23'
# print(jsn)



# json_file = '/sampleJson.json'
# file_location = __location__ + json_file
# with open(file_location, 'w') as file_obj:
#     json.dump(jsn, file_obj)


#1
# import random

# file_location = __location__ + '/words_list.txt'

# def get_words_from_file(file_location):
#     with open(file_location,'r' ) as f:
#         words = f.read().split()
#     return words

# def get_random_sentence(lenght, lst):
#     random_words = random.choices(lst, k=lenght)
#     random_sentence = ' '.join(random_words).lower()
#     return random_sentence

# def main():
#     print("This program generates random sentences. The program asks the user how long the sentence should be and then generate sentence.")

#     while True:
#         try:
#             sentence_length = int(input("Enter a number between 2 and 20 to determine the sentence length: "))
#             if sentence_length < 2 or sentence_length > 20:
#                 raise ValueError("Length should be between 2 and 20")
#             break
#         except ValueError as e:
#             print("Invalid input. Please enter a valid number between 2 and 20.")
#             print(e)

#     words = get_words_from_file(file_location)
#     sentence = get_random_sentence(sentence_length, words)
#     print('Random Sentence:',sentence)
# if __name__ == '__main__':
#     main()


 