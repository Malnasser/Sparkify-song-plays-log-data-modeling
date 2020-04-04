# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"

user_table_drop = "DROP TABLE IF EXISTS users;"

song_table_drop = "DROP TABLE IF EXISTS songs;"

artist_table_drop = "DROP TABLE IF EXISTS artists;"

time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = (""" 
CREATE TABLE IF NOT EXISTS songplays (songplay_id serial,
start_time timestamp, user_id varchar(20), level varchar, song_id varchar(30),
artist_id varchar(40), session_id int, location varchar, user_agent varchar,
FOREIGN KEY (user_id) REFERENCES users(user_id), FOREIGN KEY (song_id) REFERENCES songs(song_id), \
FOREIGN KEY (artist_id) REFERENCES artists(artist_id) \
)""")

user_table_create = (""" 
CREATE TABLE IF NOT EXISTS users ( \
user_id varchar(20), first_name varchar(20), \
last_name varchar(20), gender char(6), \
level varchar(10), PRIMARY KEY(user_id) \
)""")

song_table_create = (""" 
CREATE TABLE IF NOT EXISTS songs ( 
song_id varchar(30), title varchar(100), artist_id varchar(30), \
year int, duration decimal, PRIMARY KEY(song_id) \
)""")

artist_table_create = (""" 
CREATE TABLE IF NOT EXISTS artists ( \
artist_id varchar(40), name varchar(100), location varchar(100), \
latitude decimal, longtitude decimal,  PRIMARY KEY(artist_id) \
)""")

time_table_create = (""" 
CREATE TABLE IF NOT EXISTS time ( \
start_time timestamp, hour int, day int, week int, month int, \
year int, weekday varchar, PRIMARY KEY(start_time) \
)""")

# INSERT RECORDS

songplay_table_insert = (""" 
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING""")

artist_table_insert = (""" 
INSERT INTO artists (artist_id, name, location, latitude, longtitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING""")

# FIND SONGS

song_select = ("""
SELECT songs.song_id, artists.artist_id
FROM songs
JOIN artists ON artists.artist_id = songs.artist_id
WHERE   songs.title = %s
AND     songs.artist_id = %s
AND     songs.duration = %s
""")
# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]