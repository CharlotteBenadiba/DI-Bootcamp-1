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

# item = MenuItem("New Item1", 100)
# item = MenuItem("New Item2", 150)
# item.save()

# item.delete(item_id=8)

# item.update(item_id=8, new_price=200,new_name='Updated item')

# item = MenuItem('Burger', 35)
# item.save()
# item.delete()
# item.update('Veggie Burger', 37)
# item2 = MenuManager.get_by_name('Beef Stew')
# items = MenuManager.all()