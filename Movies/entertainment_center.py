# "media" and "fresh_tomatoes" are two Python files
# which entertainment_center.py depends upon.
import media
import fresh_tomatoes

# Six movie objects are initialized from the Movie class defined in media.py
# Each movie is defined by its title, storyline, film poster, and trailer.
# media.py established this template, which all films must have.
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "http://1.bp.blogspot.com/-4CEJ24flM5U/T-ePLTwLdyI/AAAAAAAAHcQ/GGYVN8SVxG0/s1600/Toy+Story+%281995%29+1.jpg",  # noqa
    "https://www.youtube.com/watch?v=vwyZH85NQC4")

back_to_the_future = media.Movie(
    "Back to the Future",
    "A teenager in a time-traveling DeLorean is \
    trapped in the 1950's and must find his way \
    home",
    "https://www.movieposter.com/posters/archive/main/50/MPW-25074",  # noqa
    "https://www.youtube.com/watch?v=qvsgGtivCgs")

zootopia = media.Movie(
    "Zootopia",
    "In a city where predators and prey live in harmony, \
    a rabbit and a fox must solve the mystery of why some \
    predators are going feral",
    "https://lumiere-a.akamaihd.net/v1/images/movie_poster_zootopia_866a1bf2.jpeg?region=0%2C0%2C300%2C450",# noqa
    "https://www.youtube.com/watch?v=jWM0ct-OLsM")

avatar = media.Movie(
    "Avatar",
    "A paraplegic marine dispatched to the moon Pandora on a \
    unique mission becomes torn between following his orders \
    and protecting the world he feels is his home.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",  # noqa
    "https://www.youtube.com/watch?v=aVdO-cx-McA")

rain_man = media.Movie(
    "Rain Man",
    "Selfish yuppie Charlie Babbitt's father left a \
    fortune to his savant brother Raymond and a pittance \
    to Charlie; they travel cross-country.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMzVjNzI4NzYtMjE4NS00M2IzLWFkOWMtOTYwMWUzN2ZlNGVjL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",  # noqa
    "https://www.youtube.com/watch?v=mlNwXuHUA8I")

enchanted = media.Movie(
    "Enchanted",
    "A princess, who is prepared to be wed, is sent away \
    to New York by an evil queen, where she falls in love \
    with a lawyer.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjE4NDQ2Mjc0OF5BMl5BanBnXkFtZTcwNzQ2NDE1MQ@@._V1_.jpg",  # noqa
    "https://youtu.be/uW6dNiOIOhA")


# Each of the movies above is consolidated into one list...
movies = [toy_story, back_to_the_future, zootopia, avatar, rain_man, enchanted]
# ... which is then displayed using the HTML formatting in fresh_tomatoes.py!
fresh_tomatoes.open_movies_page(movies)
