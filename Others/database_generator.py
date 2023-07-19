import os
import psycopg2

def get_artist_and_title(file_name):
    try:
        data = file_name.split(" - ", 1)
        return data[0], data[1].rstrip(".mp3")
    except IndexError:
        return None, None


def insert_data_into_db(connection, cursor, artist, title, file_path):
    sql_query = f"INSERT INTO generator_test (main_artist, song_title, file_path) VALUES (%s, %s, %s);"
    cursor.execute(sql_query, (artist, title, file_path))
    connection.commit()


def extract_info_from_files(main_folder, connection, cursor):
    for root, _, all_files in os.walk(main_folder):
        for file_name in all_files:
            artist, title = get_artist_and_title(file_name)
            if artist and title:
                file_path = os.path.join(root, file_name).replace(main_folder, "")
                insert_data_into_db(connection, cursor, artist, title, file_path)


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
    
    root_path = "C:/Dessy/Music"
    files_dir = os.path.join(root_path, 'Pop')

    extract_info_from_files(files_dir, connection, cursor)
    print("Data inserted successfully!")
    
except psycopg2.Error as e:
    print("Error connecting database")

finally:
    if connection is not None:
        connection.close()
