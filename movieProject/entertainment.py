import media
import fresh_tomatoes

robot = media.Movie("Endhiran",
                    "Endhiran is a story of Andro-Humanoid Robot which fell in love with the heroine, Aishwarya Rai and how the scientist struggled to dismantle itself at later stage"
                    , "https://upload.wikimedia.org/wikipedia/en/0/0f/Enthiran_poster.jpg",
                     "https://www.youtube.com/watch?v=Ghh1Y7lsWwk")

i = media.Movie("I",
                "I is a story of body builder named Lingesan who gets into modelling by the heroine, Amy Jackson and backstabbed by culprits. The story deals with the hero who struggled to punish the villains",
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1mjzx63JdUa9phJuKzhy9Eh3_rz9P5gmThG8u-PxM9YoSUlyJ",
                "https://www.youtube.com/watch?v=pzTHmcXfeug")

friends = media.Movie("Nanban",
                      "Nanban is a story of three students who succeeds in life because of his friend named Panchavan Parivendhan who motivated the other two to get into success in their lives.",
                      "http://photos.filmibeat.com/ph-big/2011/11/nanban_13226425247.jpg",
                      "https://www.youtube.com/watch?v=z1YaqEIIQL8")

movies = [robot, i, friends]

fresh_tomatoes.open_movies_page(movies)