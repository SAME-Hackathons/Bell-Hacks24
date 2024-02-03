from instagrapi import Client
from instagrapi.exceptions import LoginRequired
import joblib
from class_data import *
import logging

logging.basicConfig(encoding='utf-8', level=logging.WARNING)
logging.info("Starting Instagram bot")


cl = Client()
cl.delay_range = [1, 3]

model = joblib.load("model/better.joblib")
def is_hatefull(comment):
     df = pd.DataFrame([comment], columns=['text'])
     if(model.predict(df) == 1):
          return True
     else:
          return False

def login():
    global user_id

    with open("credentials.op", "r") as file:
        lines = file.readlines()

    username = lines[1].strip()
    password = lines[2].strip()



    try:
        session = cl.load_settings("igsession.json")
    except FileNotFoundError:
        session = None

    login_via_session = False
    login_via_pw = False
     
    if session:
        try:
            cl.set_settings(session)
            cl.login(username, password)

            # check if session is valid
            try:
                cl.get_timeline_feed()
                logging.info("Session is valid")
            except LoginRequired:
                logging.info("Session is invalid, need to login via username and password")

                old_session = cl.get_settings()

                # use the same device uuids across logins
                cl.set_settings({})
                cl.set_uuids(old_session["uuids"])

                cl.login(username, password)
            login_via_session = True
        except Exception as e:
            logging.info("Couldn't login user using session information: %s" % e)

    if not login_via_session:
        try:
            logging.info("Attempting to login via username and password. username: %s" % username)
            if cl.login(username, password):
                login_via_pw = True
        except Exception as e:
            logging.info("Couldn't login user using username and password: %s" % e)

    if not login_via_pw and not login_via_session:
        raise Exception("Couldn't login user with either password or session")

    cl.dump_settings("igsession.json")
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
                #cl.direct_message_delete(thread.pk, msg.id)
                cl.user_block(user.pk)



if __name__ == "__main__":
    login()
    try:
        remove_comments()
        remove_direct_messages()
    except LoginRequired as e:
        logging.error(e)
        cl.relogin()
        cl.dump_settings("igsession.json")
        remove_comments()
        remove_direct_messages()
