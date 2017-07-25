import webbrowser

#the class keyword allows us to create classes
class Movie():
    #this is the so called constructor
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        #create some "instance variables"
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #this is a so called instance method
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)