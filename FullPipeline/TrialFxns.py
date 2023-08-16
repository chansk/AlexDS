## Retrieving that same data from DB into workspace

def db_to_workspace_string(table_name, sql_arg="SELECT data FROM ", DB="postgres"):
  
  # Attention: this works with NOAA string, but not Tomorrow's
  # Establish connection to PostgreSQL database
  conn = psycopg2.connect(database =DB, user = "postgres",
                          password = "Brazilll", host = "localhost", 
                          port = "5432")
  
  # Create a cursor object to execute SQL queries
  cur = conn.cursor()
  
  # Select the JSON data from the table
  # cur.execute("SELECT data FROM noaacast1")
  cur.execute(sql_arg + table_name)
  
  # Fetch the retrieved data, which should already be stored as a python object
  # json_data = cur.fetchone()[0]
  for row in cur.fetchall():
    string = row[0]
  # Do something with the individual string, such as printing it
  # fxn here to save each string as 
  # print(string) # prob not necessary
  
  # Close the cursor and the connection
  cur.close()
  conn.close()
  
  return(string)

#jj = db_to_workspace_string("noaacast1")


def db_to_workspace_string_meteo(table_name, sql_arg="SELECT data FROM ", DB="postgres"):

  # Attention: this works with NOAA string, but not Tomorrow's
  # Establish connection to PostgreSQL database
  conn = psycopg2.connect(database =DB, user = "postgres",
                          password = "Brazilll", host = "localhost", 
                          port = "5432")
  
  # Create a cursor object to execute SQL queries
  cur = conn.cursor()
  
  # Select the JSON data from the table
  # cur.execute("SELECT data FROM noaacast1")
  cur.execute(sql_arg + table_name)
  
  # Fetch the retrieved data, which should already be stored as a python object
  # json_data = cur.fetchone()[0]
  for row in cur.fetchall():
      string = row[0]
      # Do something with the individual string, such as printing it
      # fxn here to save each string as 
      # print(string) # prob not necessary
  
  # Close the cursor and the connection
  cur.close()
  conn.close()
  
  return(string)

#jj = db_to_workspace_string_meteo("meteo")


def jsonstring_to_df_Tomorrow(json_data_arg):

  # %% turn to Df
  # timelines = parsed_data['data']['timelines']
  timelines = json_data_arg['data']['timelines']
  intervals = []
  for timeline in timelines:
      intervals.extend(timeline['intervals'])
  
  # Create a DataFrame from the extracted data
  data = pd.DataFrame(intervals)
  
  
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
      
  return(df)

# df2 = jsonstring_to_df(json_data)
#df2 = jsonstring_to_df_Tomorrow(string) # Attention: this works
