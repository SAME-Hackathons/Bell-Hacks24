import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import pandas as pd
import joblib
from class_data import *
from hateful import is_hateful

# OAuth2 credentials file (replace 'path/to/credentials.json' with your actual path)
credentials_path = 'credentials.json'

# Scope required for YouTube Data API
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def authenticate():
    credentials = None

    # The file token.json stores the user's access and refresh tokens, and is created automatically when the
    # authorization flow completes for the first time.
    if os.path.exists('token.json'):
        credentials = Credentials.from_authorized_user_file('token.json')

    # If there are no (valid) credentials available, let the user log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            credentials = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(credentials.to_json())

    return credentials

# Get OAuth2 credentials
creds = authenticate()

# Build the YouTube API service using OAuth2 credentials
youtube_service = build('youtube', 'v3', credentials=creds)

def filter_comment(video_id):
    # Search for comments on the video with the specified text
    #print("ran")
    comments_request = youtube_service.commentThreads().list(
        part='id,snippet',
        videoId=video_id,
        textFormat='plainText'
    )
    comments_response = comments_request.execute()

    # Check each comment for the specified text
    for comment_thread in comments_response['items']:
        #print("went through comments")
        comment = comment_thread['snippet']['topLevelComment']['snippet']['textDisplay']
        #print(comment)
        if is_hateful(comment):
            comment_id = comment_thread['id']
            delete_comment(comment_id)
            print("Deleted Comment: " + comment)
        else:
            print("Not Deleted: " + comment)


    return None

def delete_comment(comment_id):
    # Delete a comment with the specified ID
    youtube_service.comments().delete(
        id=comment_id
    ).execute()
    print("Comment deleted successfully.")

if __name__ == "__main__":
    # Replace 'YOUR_VIDEO_ID' with the actual video ID and 'YOUR_COMMENT_TEXT' with the comment text you want to find
    video_id = '-vIC9kZwvq8'
    comment_text = 'poop32'

    # Find the comment ID
    filter_comment(video_id)

