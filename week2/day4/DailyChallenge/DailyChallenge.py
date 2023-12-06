#1
# import string
# import re

# import os

# __location__ = os.path.realpath(
#     os.path.join(os.getcwd(), os.path.dirname(__file__)))

# file_location = __location__ + '/the_stranger.txt'

# class Text:
#     def __init__(self,string) -> None:
#         self.string = string

#     def frequency_of_word(self, word):
#         words = self.string.lower().split()
#         word = word.lower()
#         word_count = words.count(word)
#         if word_count == 0:
#             return f"The word '{word}' does not appear in the text."
#         else:
#             return f"The word '{word}' appears {word_count} time(s) in the text."  

#     def most_common_word(self):
#         words = self.string.lower().split()
#         word_count = {word: words.count(word) for word in set(words)}

#         max_frequency = max(word_count.values())
#         most_common = [word for word, frequency in word_count.items() if frequency == max_frequency]

#         return f"The most common word(s) are {', '.join(most_common)} with a frequency of {max_frequency}."  

#     def unique_words(self):
#         words = self.string.lower().split()
#         unique = list(set(words))
#         return unique
    
#     @classmethod
#     def from_file(cls,file_location):
#         try:
#             with open(file_location,'r' ) as f:
#                 text = f.read()
#             return cls(text)
#         except FileNotFoundError:
#             print(f"File not found.")
#             return None
        
# class TextModification(Text):
#     def __init__(self, text):
#         super().__init__(text)
#         self.punctuation = string.punctuation
#         self.stop_words = ["a", "an", "the", "this", "that", "is", "it", "to", "and"]

#     def remove_punctuation(self):
#         without_punct = ''.join([char for char in self.string if char not in self.punctuation])
#         return without_punct

#     def remove_stop_words(self):
        
#         words = self.string.split()
#         without_stop_words = ' '.join([word for word in words if word.lower() not in self.stop_words])
#         return without_stop_words

#     def remove_special_characters(self):
#         without_special_chars = re.sub(r'[^a-zA-Z0-9\s]', '', self.string)
#         return without_special_chars


# text_string = "A good book would sometimes cost as much as a good house."
# text_object = Text(text_string)
# print(text_object.frequency_of_word("good"))

# print(text_object.most_common_word())
# print(text_object.unique_words())

#2
# stranger_text = Text.from_file(file_location)
# print(stranger_text.frequency_of_word("fine"))
# print(stranger_text.most_common_word())
# print(stranger_text.unique_words())

#bonus part
# stranger_text_modified = TextModification.from_file(file_location)

# print(stranger_text_modified.remove_punctuation())

# print(stranger_text_modified.remove_stop_words())

# print(stranger_text_modified.remove_special_characters())

