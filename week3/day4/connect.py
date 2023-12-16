#create the connection 
#commit ot rollback 
# close the connection 

import psycopg2
import os
from dotenv import load_dotenv

#est connection 
conn = psycopg2.connect(
    dbname  ='flyvcfjo',
    user ='flyvcfjo',
    password ='UJqLWdFnuIhVkmFlS-ULJl47E1ZbueAA',
    host = 'flora.db.elephantsql.com',
    port ='5432'
)

#create a cursur object to execute SQL queries
cur = conn.cursor()

# #execute a SELECT quary 
cur.execute('SELECT * FROM products')
rows = cur.fetchall()

for row in rows:
    print(row)

# #close
# cur.close()
# conn.close()

# #insert quary
insert_quary = 'INSERT INTO PRODUCTS (username, price) VALUES (%s,%s)' 
data_to_insert = ('iKey', 750)
cur.execute (insert_quary, data_to_insert)

# # commit the transaction
conn.commit()
# #or
# conn.rollback()
# conn.close()


#CRUD - Create (insert) Read (Select) Update (Update) Delete (Delete)

#update quary 
update_query = 'UPDATE products SET username=%s,price =%s WHERE user_id=%s'
new_value = ('iCar20',9999,6)
cur.execute(update_query, new_value)

conn.commit()

#delete quary
cur.execute('DELETE FROM products WHERE user_id BETWEEN %s AND %s', (10,29))
conn.commit()

conn.rollback()

load_dotenv()

#retrieve database crendetionals from env

db_name = os.getenv('db_name')
db_name = os.getenv('db_user')
db_name = os.getenv('db_pass')
db_name = os.getenv('db_host')
db_name = os.getenv('db_port')
#the same
#establish connection
conn = psycopg2.connect(
    db_name = os.getenv('db_name')
    db_name = os.getenv('db_user')
    db_name = os.getenv('db_pass')
    db_name = os.getenv('db_host')
    db_name = os.getenv('db_port')
)

cur = conn.cursor()

