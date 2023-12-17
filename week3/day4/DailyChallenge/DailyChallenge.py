import requests
import psycopg2
import random

# Function to fetch random countries
def fetch_random_countries():
    response = requests.get('https://restcountries.com/v3.1/all')
    if response.status_code == 200:
        countries_data = response.json()
        return random.sample(countries_data, 10)  # Choose 10 random countries
    else:
        print("Failed to fetch data")
        return []

#Establish connection
conn = psycopg2.connect(
    dbname  ='Managemen_system',
    user ='postgres',
    host = 'localhost',
    port ='5432'
)
cur = conn.cursor()
# Function to insert data into PostgreSQL
def insert_into_postgres(cursor, countries):
    cursor = conn.cursor()
    for country in countries:
        try:
            name = country['name']['official']
            capital = country['capital'][0]
            flag = country.get('flags', {}).get('png', '')
            subregion = country.get('subregion', '')
            population = country.get('population', 0)
            
            cursor.execute('''INSERT INTO countries VALUES (%s, %s, %s, %s, %s)''', (name, capital, flag, subregion, population))
        except Exception:
            continue
    conn.commit()
    cursor.close()
# Main function to execute the process
def main():
    try:
        conn = psycopg2.connect(
            dbname="Managemen_system", 
            user="postgres", 
            host="localhost", 
            port="5432"
        )

        random_countries = fetch_random_countries()
        insert_into_postgres(conn, random_countries)
        
        conn.close()
        print("Data inserted successfully.")
        
    except psycopg2.Error as e:
        print("Error:", e)

if __name__ == "__main__":
    main()