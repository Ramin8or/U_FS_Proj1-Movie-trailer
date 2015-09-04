# U_FS_Proj1-Movie-trailer
Udacity Full-Stack Project 1 - Movie Trailer
This is the assignment for Project 1 of Full-stack Udacity Nanodegree. The course is Programming with Python.

To run the Movie-trailer Project Python 2.7 must be installed on your machine already.

Once Python 2.7 is installed, run entertainment_center.py. Make sure all *.py files and the favorite_movies.txt file are present in the directory where you run entertainment_center.py.

This will generate an HTML file called fresh_tomatoes.html. Then the default web browser will be launched to open the generated HTML file. The browser will display some of my favorite movies. Hovering over each movie will change the background for the movie tile. Clicking on a movie will bring up a small youtube window which plays the trailer clip for the selected movie.
The list of favorite movies is stored in favorite_movies.txt file. 
Each line in this file has the following information for a movie in 7 columns that are delimited by TAB characters.
Each column represents the information shown below in the specified order for each movie:
    1. Title, 2. Year, 3. Duration, 4. Rating, 5. Image URL, 6. Trailer URL, 7. Story_Line
"entertainment_center.py" Python script reads each line and creates an instance of the Movie class, and appends it to a list called movies_list. This list is then passed to "fresh_tomatoes.py" file to generate an HTML file, and drive the browser to display the generated HTML. 

