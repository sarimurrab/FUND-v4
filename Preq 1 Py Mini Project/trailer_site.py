import media
import fresh_tomatoes


sona = media.Movie("Sonakshi", "Sonakshi Sinha is my fav Actress", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Sonakshi_Sinha_-_IIFA_2017_Green_Carpet_%2835586491213%29_%28cropped%29.jpg/220px-Sonakshi_Sinha_-_IIFA_2017_Green_Carpet_%2835586491213%29_%28cropped%29.jpg",
                   "https://www.youtube.com/watch?v=Hkn1ufAvC70")

srk = media.Movie("Shahrukh", "Shahrukh is my fav Actor", "https://st1.bollywoodlife.com/data/topics/image/1/34471/c4995f9e9138ec4f766cf336190bd152_org_225X300_1.jpg",
                  "https://www.youtube.com/watch?v=J7_1MU3gDk0")


list1 = [sona, srk]

fresh_tomatoes.open_movies_page(list1)
