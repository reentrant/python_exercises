class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        """
        A playlist is considered a repeating playlist if any of the songs contain a reference to a
        previous song in the playlist.
        Otherwise, the playlist will end with the last song which points to None.
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        previous_songs = {self.name: None}
        repeating_flag = False

        next_song = self.next
        while next_song is not None:
            if next_song.name in previous_songs.keys():
                repeating_flag = True
                break
            else:
                previous_songs[next_song.name] = None
            print(previous_songs)
            next_song = next_song.next
        return repeating_flag


if __name__ == '__main__':
    first = Song("Hello")
    second = Song("Eye of the tiger")
    third = Song("Let it be")

    first.next_song(second);
    second.next_song(third);
    third.next_song(first)

    print(first.is_repeating_playlist())
