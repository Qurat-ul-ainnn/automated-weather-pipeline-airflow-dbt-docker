from api_request import fetch_data
import psycopg2
import time
import sys

# Connect to database
def connect_to_db():
    try:
        conn = psycopg2.connect(
            host='db',
            port='5432',
            dbname='db',
            user='db_user',
            password='db_password'
        )
        print('Connected to database')
        return conn
    except psycopg2.Error as e:
        print(f'Error connecting to database: {e}')
        return None

# Create Table
def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE SCHEMA IF NOT EXISTS dev;
        CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
            id SERIAL PRIMARY KEY,
            city TEXT,
            temperature FLOAT,
            weather_description TEXT,
            wind_speed FLOAT,
            time TIMESTAMP,
            inserted_at TIMESTAMP DEFAULT NOW(),
            utc_offset TEXT
        );
        """)
        conn.commit()
        print('Table created successfully')
    except psycopg2.Error as e:
        print(f'Error creating table: {e}')

# Insert Data
def insert_data(conn, data):
    # CRITICAL FIX: If data is None (API failed), stop immediately
    if not data or 'current' not in data:
        print("Skipping insertion: No valid data received.")
        return

    try:
        location = data['location']
        weather = data['current']
        
        conn.cursor().execute("""
        INSERT INTO dev.raw_weather_data (city, temperature, weather_description,
         wind_speed, time, inserted_at, utc_offset)
         VALUES(%s, %s, %s, %s, %s, NOW(), %s)
        """,
        (
            location['name'],
            weather['temperature'],
            weather['weather_descriptions'][0],
            weather['wind_speed'],
            location['localtime'],
            location['utc_offset']
        ))
        conn.commit()
        print(f"Data inserted successfully for {location['name']}")
    except psycopg2.Error as e:
        print(f'Error inserting data: {e}')

# Main Orchestrator
def main():
    cities = ['New York', 'London', 'Paris', 'Tokyo', 'Sydney']
    conn = None
    
    try:
        conn = connect_to_db()
        if not conn:
            return

        create_table(conn)
        
        for city in cities:
            print(f"--- Processing {city} ---")
            
            # 1. Fetch Data
            data = fetch_data(city)
            
            # 2. Insert Data (Safely)
            insert_data(conn, data)
            
            # 3. Sleep to prevent 429 Rate Limit Error
            time.sleep(2)
            
    except Exception as e:
        print(f'Unexpected Error: {e}')
    finally:
        if conn:
            conn.close()
            print('Connection closed')

if __name__ == "__main__":
    main()