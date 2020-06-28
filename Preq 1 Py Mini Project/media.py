import webbrowser
import fresh_tomatoes


class Movie():
    def __init__(self, title, story_line, movie_review, poster_url):
        self.title = title
        self.story_line = story_line
        self.poster_image_url = movie_review
        self.trailer_youtube_url = poster_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
