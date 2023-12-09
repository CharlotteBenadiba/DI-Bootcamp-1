# from anagram_checker import AnagramChecker

# def get_user_input():
#     while True:
#         user_input = input("Enter a word (or 'exit' to quit): ").strip()
#         if user_input.lower() == 'exit':
#             return None
#         if ' ' in user_input:
#             print("Error: Only a single word is allowed.")
#             continue
#         if not user_input.isalpha():
#             print("Error: Only alphabetic characters are allowed.")
#             continue
#         return user_input

# def display_anagrams(word, anagrams):
#     print(f"\nYOUR WORD: \"{word}\"")
#     if anagrams:
#         print("This is a valid English word.")
#         print(f"Anagrams for your word: {', '.join(anagrams)}.")
#     else:
#         print("This word has no anagrams.")

# def main():
#     anagram_checker = AnagramChecker()

#     while True:
#         user_word = get_user_input()
#         if user_word is None:
#             print("Exiting...")
#             break

#         anagrams = anagram_checker.get_anagrams(user_word)
#         display_anagrams(user_word, anagrams)

# main()

