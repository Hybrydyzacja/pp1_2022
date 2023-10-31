class Music():
    def __init__(self, artist, song, album, year):
        self.artist = artist
        self.song = song
        self.album = album
        self.year = year

    def __str__(self):
        return(f'Performer: {self.artist}\nSong: {self.song}\nAlbum: {self.album}\nYear: {self.year}')


song1 = Music("Ed Sheeran", "Hearts Dont Break Around Here", "Divide", 2017)

print(song1)
