from instagrapi import Client

cl = Client()
cl.login("jason_c.2007", "SAMEHACKS")

user_id = cl.user_id_from_username("jason_c.2007")
medias = cl.user_medias(user_id, 20)

threads = cl.direct_threads()

for post in medias:
     comments = cl.media_comments(medias[0].id)
     for comment in comments:
          print(comment.text)
          print(comment.user.username)
          if comment.text == "bad comment":
               cl.comment_bulk_delete(medias[0].id, [comment.pk])


for thread in threads:
     cl.direct_answer(thread.id, "")



print()