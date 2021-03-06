import fresh_tomatoes
import media

# Create six movie objects, passing the strings title, description, poster
# image, and trailer link.
movie_a = media.Movie("The Thing",
                      "A group of men in the Antarctic band together to "
                      "fight an otherworldy evil... but can they trust each "
                      "other?",
                      "https://upload.wikimedia.org/wikipedia/en/c/c1"
                      "/ThingPoster.jpg",
                      "https://www.youtube.com/watch?v=VnGBL-qrmvE")

movie_b = media.Movie("Assault on Precinct 13",
                      "A police officer and a convicted murderer are forced "
                      "to cooperate when local gangs attack.",
                      "https://upload.wikimedia.org/wikipedia/en/9/9d"
                      "/Assault_on_precinct_thirteen_movie_poster.jpg",
                      "https://www.youtube.com/watch?v=BaJR2zlnp7o")

movie_c = media.Movie("In the Mouth of Madness",
                      "An author uncovers a mystery and discovers his own "
                      "madness",
                      "https://upload.wikimedia.org/wikipedia/en/9/92"
                      "/Mouthmadnessposter.jpg",
                      "https://www.youtube.com/watch?v=mHJl2V1sMxc"
                      )

movie_d = media.Movie("Escape From New York",
                      "Snake Plisskin is tasked with rescuing the President "
                      "from post-apocalyptic New York... or lose his life.",
                      "https://upload.wikimedia.org/wikipedia/en/4/4b"
                      "/EscapefromNYposter.jpg",
                      "https://www.youtube.com/watch?v=8-LDW7tWwAI")

movie_f = media.Movie("Prince of Darkness",
                      "An ancient mystery draws in a research team and "
                      "forces them to confront their own dark pasts.",
                      "https://upload.wikimedia.org/wikipedia/en/e/e9"
                      "/Prince_of_darkness.jpg",
                      "https://www.youtube.com/watch?v=PKI2kI6Flw0")

movie_e = media.Movie("They Live",
                      "Work. Buy. Die.",
                      "https://upload.wikimedia.org/wikipedia/en/3/3d"
                      "/1988They_Live_poster300.jpg",
                      "https://www.youtube.com/watch?v=KLRafyWhzG4")

# Put movie objects into a list.
movies = [movie_a, movie_b, movie_c, movie_d, movie_e, movie_f]

# Past the list of movies to the fresh_tomatoes script.
fresh_tomatoes.open_movies_page(movies)
