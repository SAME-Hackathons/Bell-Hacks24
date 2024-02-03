import os
import google.auth
from googleapiclient.discovery import build

# Set your API key or OAuth credentials
# For API key:
api_key = "YOUR_API_KEY"

# For OAuth credentials (replace 'path/to/credentials.json' and 'path/to/token.json' with your actual paths)
# credentials_path = 'path/to/credentials.json'
# token_path = 'path/to/token.json'
# credentials, _ = google.auth.transport.requests.Request().from_client_secrets_file(credentials_path)
# credentials.refresh(google.auth.transport.requests.Request())
# token = credentials.token
# credentials = google.auth.credentials.Credentials.from_authorized_user_file(token_path)

# Build the YouTube API service
youtube_service = build('youtube', 'v3', developerKey=api_key)

def find_comment(video_id, comment_text):
    # Search for comments on the video with the specified text
    comments_request = youtube_service.commentThreads().list(
        part='id,snippet',
        videoId=video_id,
        textFormat='plainText'
    )
    comments_response = comments_request.execute()

    # Check each comment for the specified text
    for comment_thread in comments_response['items']:
        comment = comment_thread['snippet']['topLevelComment']['snippet']['textDisplay']
        if comment_text in comment:
            return comment_thread['id']

    return None

def delete_comment(comment_id):
    # Delete a comment with the specified ID
    youtube_service.comments().delete(
        id=comment_id
    ).execute()
    print("Comment deleted successfully.")

if __name__ == "__main__":
    # Replace 'YOUR_VIDEO_ID' with the actual video ID and 'YOUR_COMMENT_TEXT' with the comment text you want to find
    video_id = 'YOUR_VIDEO_ID'
    comment_text = 'YOUR_COMMENT_TEXT'

    # Find the comment ID
    comment_id = find_comment(video_id, comment_text)

    if comment_id:
        # Delete the comment
        delete_comment(comment_id)
    else:
        print("Comment not found.")
