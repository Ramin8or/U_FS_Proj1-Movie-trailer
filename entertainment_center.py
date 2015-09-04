import fresh_tomatoes
import media

# Name of input file which holds the list of favorite movies and their info
FAV_MOVIES_FILE = r"favorite_movies.txt"

# Number of columns in FAV_MOVIES_FILE
NUM_OF_COLUMNS = 7

# List of Movie instances which will contain movie information after FAV_MOVIES_FILE is read
movies_list = []

with open(FAV_MOVIES_FILE) as file:
  for line in file:
    # After reading a line from the input file, split each line into columns in this order:
    # 1. Title, 2. Year, 3. Duration, 4. Rating, 5. Image URL, 6. Trailer URL, 7. Story_Line
    # Lines are delimited by TAB and stripped of their ending return character.
    columns = line.rstrip('\n').split('\t', NUM_OF_COLUMNS)

    # Last field in columns denotes story_line, constrain it to 200 characters
    story_line = (columns[6][:200] + '...') if len(columns[6]) > 200 else columns[6]

    # Create a Movie object and append the instance into movie_list
    movies_list.append( media.Movie( columns[0].upper(), columns[1], columns[2], columns[3], columns[4], columns[5], story_line ) )

# Pass the movies_list to fresh_tomotoes method to write out the HTML page for favorite movies
fresh_tomatoes.open_movies_page(movies_list)

