import fresh_tomatoes
import media

# This program shows my favorite movies on a web page.  When the movie is selected it plays the trailer.
# This program uses a Python module fresh_tomatoes that when given a movie list launches a web page that displays
# the poster images of each movie and responds to user clicks on an image by playing the trailer for the movie.
# A separate module media implements a class that stores the relevant instance variables needed by fresh_tomatoes.

joe_vs_volcano = media.Movie ("Joe Versus the Volcano",
                              "An existential adventure",
                              "https://images-na.ssl-images-amazon.com/images/I/41zfspgSM7L._SY300_.jpg",
                              "https://www.youtube.com/watch?v=cmQDIne3CLo")
blade_runner = media.Movie ("Blade Runner",
                            "To be a replicant or not a replicant",
                            "https://i.pinimg.com/originals/12/3b/85/123b8504866c67df71539f1e0d38c5a8.jpg",
                            "https://www.youtube.com/watch?v=iYhJ7Mf2Oxs")
wizards = media.Movie ("Wizards",
                       "Everlasting struggle for world supremacy fought between the powers of tchnology and magic",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BOGVmZDIwZjItNTY4Mi00NDE2LTg3NTYtMTNjNThlOThiMWFlL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                       "https://www.youtube.com/watch?v=eMSOouOkCic")
little_big_man = media.Movie ("Little Big Man",
                              "Western odyssey",
                              "https://images-na.ssl-images-amazon.com/images/I/91opQoCA8mL._SL1500_.jpg",
                              "https://www.youtube.com/watch?v=lnRaU39mI5E")
the_revenant = media.Movie ("The Revenant",
                            "Another western odyssey",
                            "https://images-na.ssl-images-amazon.com/images/I/51isa53LFIL._SL500_AC_SS350_.jpg",
                            "https://www.youtube.com/watch?v=QRfj1VCg16Y")

print (media.Movie.__doc__)
movies = [joe_vs_volcano, blade_runner, wizards, little_big_man, the_revenant]
fresh_tomatoes.open_movies_page (movies)
