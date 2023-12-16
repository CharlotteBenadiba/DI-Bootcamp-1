# #Part 1

# import psycopg2

# class MenuItem:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price 
#     def save(self):
#         conn = psycopg2.connect(
#             dbname="Managemen_system",
#             user="postgres",
#             host="localhost",
#             port="5432"
#         )
#         cur = conn.cursor() 
#         cur.execute('INSERT INTO menu_items (item_name, item_price) VALUES (%s,%s)',
#                     (self.name, self.price))
#         conn.commit()
#         print('Item saved successfully!')
#         cur.close()
#         conn.close()

#     def delete(self, item_id):
#         conn = psycopg2.connect(
#             dbname="Managemen_system",
#             user="postgres",
#             host="localhost",
#             port="5432"
#         )
#         cur = conn.cursor()
#         cur.execute("DELETE FROM menu_items WHERE item_id = %s", (item_id,))
#         conn.commit()
#         print("Item deleted successfully!")
#         cur.close()
#         conn.close()

#     def update(self, item_id, new_name=None, new_price=None):
#         conn = psycopg2.connect(
#             dbname="Managemen_system",
#             user="postgres",
#             host="localhost",
#             port="5432"
#         )
#         cur = conn.cursor()
#         if new_name is not None:
#             cur.execute('UPDATE menu_items SET item_name=%s WHERE item_id =%s', (new_name, item_id))
#         if new_price is not None:
#             cur.execute('UPDATE menu_items SET item_price=%s WHERE item_id =%s', (new_price, item_id))    
#         conn.commit()
#         print("Item updated successfully!")
#         cur.close()
#         conn.close()

# item = MenuItem('Burger', 35)
# item.save()
# item.delete(item_id=12)
# item.update(item_id=9, new_name='Veggie Burger',new_price= 37)

# from menu_manager import MenuManager

# item = MenuManager.get_by_name("Beef Stew")
# if item:
#     print("Item found:", item)
# else:
#     print("Item not found")

# item = MenuManager.get_by_name("Burger")
# if item:
#     print("Item found:", item)
# else:
#     print("Item not found")

# all_items = MenuManager.all_items()
# if all_items:
#     print("All items:", all_items)
# else:
#     print("No items found")


