class Playlist(object):
    def __init__(self):
        self.playlist = []

    def add(self, play_list_item):
        if isinstance(play_list_item, PlaylistItem ):
            self.playlist.append(play_list_item)

    def as_dict(self):
        # serialize stuff
        return {"this":"is just a sample"}


class PlaylistItem(object):
    def __init__(self, slug ):
        pass

