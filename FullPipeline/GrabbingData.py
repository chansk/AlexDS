# %%
import json
import requests
import pandas as pd
from datetime import datetime
import mysql.connector as sql
import psycopg2
# from sqlalchemy import create_engine

# %% Retrieve data using API call

url = "https://api.tomorrow.io/v4/timelines?location=42.3478%2C%20-71.0466&fields=temperature&fields=&units=metric&timesteps=1h&startTime=now&endTime=nowPlus6h&apikey=WgX3pBOikmlLo5MDTzfdHPaYuSqyhuMZ"
headers = {
    "accept": "application/json",
    "Accept-Encoding": "gzip"
}
response = requests.get(url, headers=headers)
print(response.text)

# Parse the JSON data into a Python object
parsed_data = json.loads(response.text)

# %% turn to Df
timelines = parsed_data['data']['timelines']
intervals = []
for timeline in timelines:
    intervals.extend(timeline['intervals'])

# Create a DataFrame from the extracted data
data = pd.DataFrame(intervals)
data


# %% Turn Datetimes into columns
df = pd.DataFrame(data['startTime'])

# Split datetime into separate columns
df[['date', 'time']] = df['startTime'].str.split('T', expand=True)
df[['year', 'month', 'day']] = df['date'].str.split('-', expand=True)
df[['hour', 'minute', 'second']] = df['time'].str[:-1].str.split(':', expand=True)

# Remove unnecessary columns
df = df.drop(['startTime', 'date', 'time'], axis=1)

# %% Pull the column of temperature values
df['temp'] = data['values'].apply(lambda x: x['temperature'])
    # access values in 'values' column
    # lambda fxn: extracts value, temp, from each key, x

df


# %% testing connection
conn = psycopg2.connect(database ="postgres", user = "postgres",
                        password = "Brazilll", host = "localhost", 
                        port = "5432")
# cursor
cur = conn.cursor()

query = """SELECT boot_val,reset_val
FROM pg_settings
WHERE name='listen_addresses';;"""
cur.execute(query)
rows = cur.fetchall()

conn.close()
print('Connection closed')
# %% Create table with false info
conn = psycopg2.connect(database ="postgres", user = "postgres",
                        password = "Brazilll", host = "localhost", 
                        port = "5432")
cur = conn.cursor()

# Create a table and insert data into it
query = """CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(100)
);
INSERT INTO users (id, name, email) VALUES
  ('1', 'John Doe', 'john@example.com'),
  ('2', 'Jane Smith', 'jane@example.com');
"""

query = """SELECT * FROM users;"""

# Check which tables exist in current DB
query = """SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog' AND 
    schemaname != 'information_schema';"""

cur.execute(query)
rows = cur.fetchall()

conn.close()
print('Connection closed')



# %% Create table and store API call

# Connect to DB
# conn_string = 'postgres://user:password@host/data1'
# conn_string = 'psycopg2.connect://postgres:Brazilll@localhost/data1' 
# db = create_engine(conn_string)
# conn = db.connect()

conn_string = psycopg2.connect(database ="postgres", user = "postgres",
                        password = "Brazilll", host = "localhost", 
                        port = "5432")
cur = conn.cursor()


  
# Change Df to SQL
df.to_sql('data', con=cur, if_exists='replace',
          index=False)
conn = psycopg2.connect(conn_string
                        )
conn.autocommit = True
cursor = conn.cursor()
  
# Testing if can retrieve data easily
    # Attention: this now working
sql1 = '''select * from data;'''
cursor.execute(sql1)
for i in cursor.fetchall():
    print(i)
  
# conn.commit()
conn.close()

# %% Retrieve data from table
