import helper_final_project
import fresh_tomatoes


Sonakshi_sinha1 = helper_final_project.Movie("AKIRA", "The Story of a Girl.",
                                             "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRhPGalyXO4ffKmoemaTXb_ijpNzv-M6qll2Q&usqp=CAU",
                                             "https://www.youtube.com/watch?v=QsCkty3mpg0")

Sonakshi_sinha2 = helper_final_project.Movie("Once upon a time in Mumbai", "The Story of Mumbai",
                                             "https://www.gstatic.com/tv/thumb/v22vodart/10123432/p10123432_v_v8_ab.jpg",
                                             "https://www.youtube.com/watch?v=w9Qo6p4XsXE")

Sonakshi_sinha3 = helper_final_project.Movie("Happy Phirr Bhag Jayegi", "The Story of a girl",
                                             "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Sonakshi_Sinha_-_IIFA_2017_Green_Carpet_%2835586491213%29_%28cropped%29.jpg/220px-Sonakshi_Sinha_-_IIFA_2017_Green_Carpet_%2835586491213%29_%28cropped%29.jpg",
                                             "https://www.youtube.com/watch?v=-HlzmWaFcG8")


movies = [Sonakshi_sinha1, Sonakshi_sinha2, Sonakshi_sinha3]

fresh_tomatoes.open_movies_page(movies)
