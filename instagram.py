from instagrapi import Client
import joblib

cl = Client()

model = joblib.load("model/logistic_regression_model.joblib")

def is_hatefull(comment):
     if(model.predict([comment]) == 1):
          return False
     else:
          return True

def login():
     global user_id

     with open("credentials.op", "r") as file:
          lines = file.readlines()


     username = lines[1].strip()
     password = lines[2].strip()

     cl.login(username, password)

     user_id = cl.user_id_from_username(username)

login()



medias = cl.user_medias(user_id, 20)



# for post in medias:
#      comments = cl.media_comments(medias[0].id)
#      for comment in comments:
#           if comment.text == "bad comment":
#                print(comment.text)
#                #cl.comment_bulk_delete(medias[0].id, [comment.pk])

threads = cl.direct_threads() + cl.direct_pending_inbox()

for thread in threads:
     msgs = cl.direct_messages(thread.pk)
     user = thread.users[0]
     print(user.username)
     for msg in msgs:

          if is_hatefull(msg.text):
               print(msg.text)



print()