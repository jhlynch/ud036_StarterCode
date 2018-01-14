# Movie Trailer Website Code
Source code for a Movie Trailer website of some of my favorite movies. This code relies on a utility module, fresh_tomatoes, that given a list of movies (title, poster image, trailer URL) will invoke a web page that displays a list of the movie’s poster images and plays the movie trailer in response to users clicking the poster images. I added the module media that implements a class that stores the movie information required by fresh_tomatoes. The basic program is contained in my_entertainment_center.py which when invoked instantiates some of my favorite movies using the class media.Movie, creates a list from these movies then invokes fresh_tomatoes.open_movies_page with the list to display said movies.

I have only run my_entertainment_center from the Python 2.x IDLE shell.

You can download my project from [github](https://github.com/jhlynch/ud036_StarterCode).

