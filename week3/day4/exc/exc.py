import psycopg2

conn = psycopg2.connect(
    dbname  ='user_management',
    user ='postgres',
    host = 'localhost',
    port ='5432'
)

cur = conn.cursor()

cur.execute('SELECT * FROM users')
rows = cur.fetchall()
for row in rows:
    print(row)

# insert_quary = 'INSERT INTO users (username, email, age) VALUES (%s,%s,%s)' 
# data_to_insert = ('Ana', 'skaliy@gmail.com', 26)
# cur.execute (insert_quary, data_to_insert)    

# conn.commit()
# cur.execute('SELECT * FROM users')
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute('DELETE FROM users WHERE id=2')
# conn.commit()    
# cur.execute('DELETE FROM users WHERE id=3')
# conn.commit()    

update_query = 'UPDATE users SET username=%s,age =%s WHERE user_id=%s'
new_value = ('Michelle',1)
cur.execute(update_query, new_value)

conn.commit()