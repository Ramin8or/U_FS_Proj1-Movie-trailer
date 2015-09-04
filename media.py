import webbrowser

class Video():
  """ This class provides a base class to store basic information on videos such as title, release year, duration, and image URL."""

  def __init__(self, video_title, year, duration, poster_image):
    self.title = video_title
    self.release_year = year
    self.duration_minutes = duration
    self.poster_image_url = poster_image
  
class Movie(Video):
  """ This class stores movie related information. It inherits from Video class, and adds movie rating, trailer URL, and storyline."""
  
  VALID_RATINGS = ["G", "PG", "PG-13", "R", "NR"]

  def __init__(self, movie_title, year, duration, movie_rating, poster_image, trailer_youtube, movie_storyline):
    Video.__init__(self, movie_title, year, duration, poster_image)
    if movie_rating in Movie.VALID_RATINGS:
      self.rating = movie_rating
    else:
      self.rating = ""
    self.trailer_youtube_url = trailer_youtube
    self.storyline = movie_storyline
  
  def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)
