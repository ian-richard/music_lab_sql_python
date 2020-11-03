import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist("Nirvana")
artist_repository.save(artist1)

album1 = Album("Come as you are", artist1, "Grunge")

album_repository.save(album1)

res = artist_repository.select_all()

pdb.set_trace()