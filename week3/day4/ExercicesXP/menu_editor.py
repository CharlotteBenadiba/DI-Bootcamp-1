# from menu_item import MenuItem
# from menu_manager import MenuManager

# class MenuEditor:
#     def __init__(self):
#         pass

#     def show_user_menu(self):
#         print("Program Menu:")
#         print("View an Item (V)")
#         print("Add an Item (A)")
#         print("Delete an Item (D)")
#         print("Update an Item (U)")
#         print("Show the Menu (S)")

#         user_choice = input("Enter your choice (V/A/D/U/S): ").upper()

#         if user_choice == "V":
#             self.view_item()
#         elif user_choice == "A":
#             self.add_item()
#         elif user_choice == "D":
#             self.delete_item()
#         elif user_choice == "U":
#             self.update_item()
#         elif user_choice == "S":
#             self.show_menu()
#         else:
#             print("Invalid choice. Please enter V, A, D, U, or S.")

#     def view_item(self):
#         print("Viewing an item...")

#     def add_item(self):
#         print("Adding an item...")

#     def delete_item(self):
#         print("Deleting an item...")

#     def update_item(self):
#         print("Updating an item...")

#     def show_menu(self):
#         print("Showing the menu...")
#     def add_item_to_menu(self):
#         item_name = input("Enter the item's name: ")
#         item_price = float(input("Enter the item's price: "))

#         new_item = MenuItem(item_name, item_price)

#         new_item.save() 

#         print("Item was added successfully.")
#     def remove_item_from_menu(self):
#         item_name = input("Enter the name of the item to remove: ")
#         item_price = float(input("Enter the price of the item: "))
#         item_to_delete = MenuItem(item_name, item_price) 
#         item_id = 1

#         if item_to_delete.delete(item_id): 
#             print("Item was deleted successfully.")
#         else:
#             print("Error: Item deletion failed.")

#     def update_item_from_menu(self):
#         old_item_name = input("Enter the name of the item to update: ")
#         old_item_price = float(input("Enter the price of the item to update: ")) 
        
#         new_item_name = input("Enter the new name for the item: ")
#         new_item_price = float(input("Enter the new price for the item: ")) 

#         old_item = MenuItem(old_item_name, old_item_price)
#         new_item = MenuItem(new_item_name, new_item_price)

#         item_id = 1

#         if old_item.update(item_id, new_item_name, new_item_price):
#             print("Item was updated successfully.")
#         else:
#             print("Error: Item update failed.")  
#     def show_restaurant_menu(self):
#         while True:
#             print("1. Show restaurant menu")
#             print("2. Exit")

#             choice = input("Enter your choice (1/2): ")

#             if choice == "1":
#                 all_items = MenuManager.all_items()
#                 print("Menu:", all_items)
#             elif choice == "2":
#                 print("Menu:", all_items)
#                 break
#             else:
#                 print("Invalid choice. Please enter 1, 2, or 3.")    

# if __name__ == "__main__":
#     menu_editor = MenuEditor()
#     menu_editor.show_user_menu()
#     menu_editor.add_item_to_menu()  
#     menu_editor.remove_item_from_menu() 
#     menu_editor.update_item_from_menu()
#     menu_editor.show_restaurant_menu() 

