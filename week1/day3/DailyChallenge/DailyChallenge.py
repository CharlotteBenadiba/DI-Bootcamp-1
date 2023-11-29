# 1
# word = input("Enter a word: ")
# letter_indexes = {}
# for index, letter in enumerate(word):
#     if letter not in letter_indexes:
#         letter_indexes[letter] = [index]
#     else:
#         letter_indexes[letter].append(index)

# print("Dictionary storing indexes of each letter:")
# print(letter_indexes)

# 2
# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }

# wallet = "$300"

# def items_you_can_afford(items_purchase, wallet):
#     wallet_amount = int(wallet.replace('$', '').replace(',', ''))
    
#     affordable_items = [item for item, price in items_purchase.items() if int(price.replace('$', '').replace(',', '')) <= wallet_amount]

#     affordable_items.sort()
    
#     return affordable_items
# result = items_you_can_afford(items_purchase, wallet)
# print(result)

# items_purchase = {
#   "Apple": "$4",
#   "Honey": "$3",
#   "Fan": "$14",
#   "Bananas": "$4",
#   "Pan": "$100",
#   "Spoon": "$2"
# }

# wallet = "$100" 
# def items_you_can_afford(items_purchase, wallet):
#     wallet_amount = int(wallet.replace('$', '').replace(',', ''))  

#     affordable_items = [item for item, price in items_purchase.items() if int(price.replace('$', '').replace(',', '')) <= wallet_amount]
    
#     affordable_items.sort()
    
#     return affordable_items
# result = items_you_can_afford(items_purchase, wallet)
# print(result)

# items_purchase = {
#   "Phone": "$999",
#   "Speakers": "$300",
#   "Laptop": "$5,000",
#   "PC": "$1200"
# }

# wallet = "$1" 
# def items_you_can_afford(items_purchase, wallet):
#     wallet_amount = int(wallet.replace('$', '').replace(',', '')) 

#     affordable_items = [item for item, price in items_purchase.items() if int(price.replace('$', '').replace(',', '')) <= wallet_amount]

#     affordable_items.sort()
    
#     return affordable_items if affordable_items else "Nothing"
# result = items_you_can_afford(items_purchase, wallet)
# print(result)