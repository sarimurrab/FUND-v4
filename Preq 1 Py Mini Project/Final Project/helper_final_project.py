import webbrowser
import fresh_tomatoes


class Movie():
    def __init__(self, title, storyline, poster_url, trailer_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
