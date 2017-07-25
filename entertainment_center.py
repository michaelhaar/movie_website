import media
import fresh_tomatos

#create an instance of a class Movie
toy_story = media.Movie("Toy Story",
                        "A Stroy of a Boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Toy_Story_logo.svg/1200px-Toy_Story_logo.svg.png",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)  #access the instance variables

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()

moana = media.Movie("Moana",
                    "The film tells the story of Moana, the strong-willed daughter of a chief of a Polynesian tribe",
                    "https://lumiere-a.akamaihd.net/v1/images/r_moana_header_poststreet_mobile_bd574a31.jpeg",
                    "https://www.youtube.com/watch?v=cPAbx5kgCJo")
#moana.show_trailer()

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "http://is1.mzstatic.com/image/thumb/Video69/v4/22/50/c3/2250c3e7-6b24-a0df-dd8f-dea7321b3ee4/source/1200x630bb.jpg",
                          "https://www.youtube.com/watch?v=niD-jahFURU")


movies = [toy_story, avatar, moana, school_of_rock, ratatouille]
fresh_tomatos.open_movies_page(movies)