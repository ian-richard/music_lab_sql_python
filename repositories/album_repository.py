from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album
from repositories import artist_repository

def save(album):
    sql = "INSERT INTO albums (album_name, artist_id, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [album.album_name, album.artist.id, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE FROM albums" 
    run_sql(sql)

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"  
    values = [id] 
    result = run_sql(sql, values)[0]
    
    if result is not None:
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['album_name'], artist, ['artist'], genre['genre'], result['id'] )
    return album