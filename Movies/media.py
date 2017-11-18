# webbrowser will allow film trailers to be played with the show_trailer function.
import webbrowser

class Movie():
    """This class stores movie-related information"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# show_trailer allows movie trailers to play in an inset window.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
