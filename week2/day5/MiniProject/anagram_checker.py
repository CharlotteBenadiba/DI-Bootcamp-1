# import os

# __location__ = os.path.realpath(
#     os.path.join(os.getcwd(), os.path.dirname(__file__)))

# class AnagramChecker:
#     def __init__(self):
#         with open(__location__ + '/sowpods.txt', mode ='r') as file:
#             self.word_list = set(word.strip().lower() for word in file.readlines())

#     def is_valid_word(self, word):
#         return word.lower() in self.word_list

#     def is_anagram(self, word1, word2):
#         return sorted(word1.lower()) == sorted(word2.lower())

#     def get_anagrams(self, word):
#         word = word.lower()
#         return [w for w in self.word_list if self.is_anagram(word, w) and word != w]  

