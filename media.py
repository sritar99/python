import webbrowser
"""to open URLs in interactive browser applications"""

class Movie():

    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
    	""" it is the constructor method for a class."""

	    self.title=movie_title
	    self.storyline=movie_storyline
	    self.poster_image_url=poster_image
	    self.trailer_youtube_url=trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        """opens the url to display the videos"""
