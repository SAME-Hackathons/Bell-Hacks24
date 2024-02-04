from instagrapi import Client
from instagrapi.exceptions import LoginRequired
from class_data import *
import logging

from hateful import *

logging.basicConfig(encoding='utf-8', level=logging.WARNING)
logging.info("Starting Instagram bot")

total_messages = 0
done_messages = 0

total_posts = 0
done_comments = 0

cl = Client()
cl.delay_range = [0, 1]


def login():
    global user_id

    with open("credentials/credentials.op", "r") as file:
        lines = file.readlines()

    username = lines[1].strip()
    password = lines[2].strip()

    try:
        session = cl.load_settings("credentials/igsession.json")
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
    global done_messages,done_comments
    medias = cl.user_medias(user_id, 20)
    for post in medias:
        comments = cl.media_comments(post.id)
        for comment in comments:
            if is_hateful(comment.text):
                print(f"User: {comment.user.username} - Comment: {comment.text}")
                #cl.comment_bulk_delete(post.id, [comment.pk])
                done_comments += 1


def remove_direct_messages():
    global done_messages,done_comments
    
    threads = cl.direct_threads() + cl.direct_pending_inbox()

    for thread in threads:
        msgs = cl.direct_messages(thread.pk)
        user = thread.users[0]
        for msg in msgs:
            if is_hateful(msg.text):
                print(f"User: {user.username} - Message: {msg.text}")
                done_messages += 1
                #cl.direct_message_delete(thread.pk, msg.id)
                #cl.user_block(user.pk)


def remove(comments, messages):
    global done_messages,done_comments
    done_messages = 0
    comments = True
    messages = True
    done_comments = 0
    login()
    try:
        if comments:
            remove_comments()
        if messages:
            remove_direct_messages()
    except LoginRequired as e:
        logging.error(e)
        cl.relogin()
        cl.dump_settings("credentials/igsession.json")
        if comments:
            remove_comments()
        if messages:
            remove_direct_messages()


if __name__ == "__main__":
    remove(True, True)
