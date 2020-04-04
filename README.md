# Data Modeling with Postgres

Modeling and creating a Postgres database for collecting data about songs and user activities.

# INTRODUCTION
The goal of this project to create PostgresSQL database to Utilize songs and song plays logs for analytics team who they are particularly interested in understanding what songs users are listening to.they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app. 

# Files
In addition to the data files, the project workspace includes six files:

    * etl.ipynb: this notebook to develop the ETL process for each tables
    * test.ipynb: this notebook to test sql_queries.py and elt.ipynb (etl.py)
    * create_tables.py: create database and tables
    * elt.py: define the ETL process
    * sql_queries.py: define the SQL queries

# Data

song metadata
```json
{
    num_songs:1
    artist_id:"ARJIE2Y1187B994AB7"
    artist_latitude:null
    artist_longitude:null
    artist_location:""
    artist_name:"Line Renaud"
    song_id:"SOUPIRU12A6D4FA1E1"
    title:"Der Kleine Dompfaff"
    duration:152.92036
    year:0
}
```

Songs play log examples
```json
{
   "artist":null,
   "auth":"Logged Out",
   "firstName":null,
   "gender":null,
   "itemInSession":0,
   "lastName":null,
   "length":null,
   "level":"free",
   "location":null,
   "method":"PUT",
   "page":"Login",
   "registration":null,
   "sessionId":52,
   "song":null,
   "status":307,
   "ts":1541207073796,
   "userAgent":null,
   "userId":""
}
```

# Database modeling using star schema

Fact Table
    songplays - records in log data associated with song plays i.e. records with page NextSong
         songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

Dimension Tables
    users - users in the app
        user_id, first_name, last_name, gender, level
    songs - songs in music database
        song_id, title, artist_id, year, duration
    artists - artists in music database
        artist_id, name, location, latitude, longitude
    time - timestamps of records in songplays broken down into specific units
        start_time, hour, day, week, month, year, weekday

star schema is used because of the following reasons:
    * Denormalized tables.
    * Simplified queries.
    * Fast aggregation.
    
    ![Alt text](./tables/starSchemaModel.svg)
    <img src="./starSchemaModel.svg">

# ETL Processes
The summary of ETL processes is below. For more details, see etl.ipynb, etl.py and sql_queries.py.

## Songs metadata ETL Processing:

### #1: `songs` Table
#### Extract Data for Songs Table
    - Parse and read a song JSON file by using pandas.read_json function.
        -- Select columns for song ID, title, artist ID, year, and duration from dataframe.
    - Execute an insert query to songs table in PostgreSQL.
    - If the song ID confliction is occured, do nothing.
    - Repeat the process iterably for all songs data.

### #2: `artists` Table
#### Extract Data for Artists Table

    - Parse and read a song JSON file by using pandas.read_json function.
    - Select columns for artist ID, name, location, latitude, and longitude from dataframe.
    - Execute an insert query to artists table in PostgreSQL.
        -- If the artist ID confliction is occured, do nothing.
    - Repeat the process iterably for all songs data.

## Process ETL `log_data`
In this part, you'll perform ETL on the second dataset, `log_data`, to create the `time` and `users` dimensional tables, as well as the `songplays` fact table.

### #3: `time` Table
#### Extract Data for Time Table
    - Parse and read a JSON file of user activity log by using pandas.read_json function.
    - Filter records by NextSong action.
    - Convert the ts timestamp column to datetime.
    - Extract the timestamp, hour, day, week of year, month, year, and weekday from dataframe.
    - Execute an insert query to time table in PostgreSQL.
    - Repeat the process iterably for all log files.

### #4: `users` Table
#### Extract Data for Users Table
    - Parse and read a JSON file of user activity log by using pandas.read_json function.
    - Filter records by NextSong action.
    - Select columns for user ID, first name, last name, gender and level from dataframe.
    - Execute an insert query to songs table in PostgreSQL.
     -- If the user ID confliction is occured, Update value of level on the recored.
    - Repeat the process iterably for all log files.

### #5: `songplays` Table
#### Extract Data and Songplays Table
    - Parse and read a JSON file of user activity log by using pandas.read_json function.
    - Filter records by NextSong action.
    - Select the timestamp, user ID, level, song ID, artist ID, session ID, location, and user agent from dataframe.
    -- Log files don't include song ID and artist ID, so get these ID by executing select query to songs and artists tables.
    - Execute an insert query to songs table in PostgreSQL.
    - Repeat the process iterably for all log files.
    
# Usage
Create tables and execute ETL.

```
$ python create_tables.py
$ python etl.py
```

# Examples of Result Sets

Fact Table: 

```bash
%sql SELECT * FROM songplays LIMIT 5;
```
![Alt text](./tables/songplayTable.PNG "songplays table")

Dimension Tables:

```bash
%sql SELECT * FROM users LIMIT 5;
```
![Alt text](./tables/usersTable.PNG "users table")


```bash
%sql SELECT * FROM songs LIMIT 5;
```
![Alt text](./tables/songsTable.PNG "songs table")


```bash
%sql SELECT * FROM artists LIMIT 5;
```
![Alt text](./tables/artistTable.PNG "artists tables")


```bash
%sql SELECT * FROM time LIMIT 5;
```
![Alt text](./tables/timeTables.PNG "time tables")