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

def remove_comments():
     medias = cl.user_medias(user_id, 20)
     for post in medias:
          comments = cl.media_comments(post.id)
          for comment in comments:
               if is_hatefull(comment.text):
                    print(f"User: {comment.user.username} - Comment: {comment.text}")
                    #cl.comment_bulk_delete(post.id, [comment.pk])

def remove_direct_messages():
     threads = cl.direct_threads() + cl.direct_pending_inbox()

     for thread in threads:
          msgs = cl.direct_messages(thread.pk)
          user = thread.users[0]
          for msg in msgs:
               if is_hatefull(msg.text):
                    print(f"User: {user.username} - Message: {msg.text}")
                    #cl.direct_message_delete(thread.pk, msg.pk)
                    #cl.user_block(user.pk)



if __name__ == "__main__":
     login()
     remove_comments()
     remove_direct_messages()





