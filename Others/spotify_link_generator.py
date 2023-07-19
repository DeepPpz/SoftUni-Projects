import os
import psycopg2
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def insert_data_into_db(connection, cursor, artist, title, spotify_link):
    sql_query = f"UPDATE generator_test SET spotify_link = %s WHERE main_artist = %s AND song_title = %s"  # check this query
    cursor.execute(sql_query, (spotify_link, artist, title))
    connection.commit()


def generate_spotify_links(artist, title):
    client_id = "0e410b530f464cb3b43f58e52db162a6"
    client_secret = "65d8c261fcec49d393b47e7e712d8b99"
    
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    
    query = f"artist:{artist} track:{title}"
    results = sp.search(q=query, type="track", limit=1)
    
    if results["tracks"]["items"]:
        track_url = results["tracks"]["items"][0]["external_urls"]["spotify"]
        return track_url


db_host = "localhost"
db_name = "spotify_generator_test"
db_user = "postgres"
db_password = "******"
connection = None

try:
    connection = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )
    cursor = connection.cursor()

    sql_query = "SELECT main_artist, song_title FROM generator_test"
    cursor.execute(sql_query)
    
    for row in cursor.fetchall():
        artist, title = row
        song_link = generate_spotify_links(artist, title)
        if song_link:
            insert_data_into_db(connection, cursor, artist, title, song_link)
        else:
            print("Spotify Link: Not found!")
    
except psycopg2.Error as e:
    print("Error connecting database")

finally:
    if connection is not None:
        connection.close()
