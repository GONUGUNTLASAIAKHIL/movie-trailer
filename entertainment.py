import hollywood_thrills
import media

the_raid=media.Movie("the raid",
                      "a story of building",
                     "https://upload.wikimedia.org/wikipedia/en/9/9a/The_Raid_2011_poster.jpg",
                     "https://www.youtube.com/watch?v=m6Q7KnXpNOg")
avengers=media.Movie("avengers",
                     "a story of persons having super powers",
                     "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
                     "https://www.youtube.com/watch?v=6ZfuNTqbHE8")
fate_of_the_furious=media.Movie("Fate Of The Furious ",
                               "a story of cars",
                               "https://upload.wikimedia.org/wikipedia/en/2/2d/The_Fate_of_The_Furious_Theatrical_Poster.jpg",
                               "https://www.youtube.com/watch?v=JwMKRevYa_M")
dead_pool_2=media.Movie("Dead pool2",
                        "a humourus movie",
                        "https://upload.wikimedia.org/wikipedia/en/c/cf/Deadpool_2_poster.jpg",
                        "https://www.youtube.com/watch?v=D86RtevtfrA")
sky_scrapper=media.Movie("sky scrapper",
                         "a  story of a father protecting his family",
                         "https://upload.wikimedia.org/wikipedia/en/6/6e/Skyscraper_%282018%29_film_poster.png",
                         "https://www.youtube.com/watch?v=t9QePUT-Yt8")
battle_ships=media.Movie("battle ships",
                         "a story of batlles in water",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/6/6e/Battleship_Poster.jpg/220px-Battleship_Poster.jpg",
                         "https://www.youtube.com/watch?v=cp3646Zf8rg")
movies=[the_raid,avengers,fate_of_the_furious,dead_pool_2,sky_scrapper,battle_ships]
hollywood_thrills.open_movies_page(movies)



