from instagrapi import Client

cl = Client()
cl.login("jason_c.2007", "SAMEHACKS")

user_id = cl.user_id_from_username("jason_c.2007")
medias = cl.user_medias(user_id, 20)



print()