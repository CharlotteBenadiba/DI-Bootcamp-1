# import psycopg2

# class MenuManager:
#     @classmethod
#     def get_by_name(cls, name):
#         conn = psycopg2.connect(
#             dbname="Managemen_system",
#             user="postgres",
#             host="localhost",
#             port="5432"
#         )
#         cur = conn.cursor() 
#         cur.execute("SELECT * FROM menu_items WHERE item_name = %s", (name,))
#         item = cur.fetchone()
#         if item:
#             return (f'Item found:{item}')
#         else:
#             return None
#         cur.close()
#         conn.close()
#     @classmethod
#     def all_items(cls):
#         conn = psycopg2.connect(
#             dbname="Managemen_system",
#             user="postgres",
#             host="localhost",
#             port="5432"
#         )
#         cur = conn.cursor() 
#         cur.execute("SELECT * FROM menu_items")
#         items = cur.fetchall()
#         return items  # Return a list of all items
#         cur.close()
#         conn.close()    
# item2 = MenuManager.get_by_name('Beef Stew')
# item2 = MenuManager.get_by_name('Burger')
# items = MenuManager.all_items()            