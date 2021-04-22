import os
from requests_oauthlib import OAuth1Session

# Add your API key here
consumer_key = ""
# Add your API secret key here
consumer_secret = ""

fields = "created_at,description,pinned_tweet_id"
params = {"usernames": "TwitterDev", "user.fields": fields}

# Get request token
request_token_url = "https://api.twitter.com/oauth/request_token"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)
fetch_response = oauth.fetch_request_token(request_token_url)
resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
print("Got OAuth token: %s" % resource_owner_key)

# Get authorization
base_authorization_url = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)
print("Please go here and authorize: %s" % authorization_url)
verifier = input("Paste the PIN here: ")

# Get the access token
access_token_url = "https://api.twitter.com/oauth/access_token"
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)

oauth_tokens = oauth.fetch_access_token(access_token_url)

access_token = oauth_tokens["oauth_token"]
access_token_secret = oauth_tokens["oauth_token_secret"]

# Make the request
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

response = oauth.get("https://api.twitter.com/labs/2/users/by?", params=params)
print(response)
print("Response status: %s" % response.status_code)
print("Body: %s" % response.text)

# If you want your OAUTH Token Data:
oauth.token

import tweepy

# Consumer keys and access tokens, used for OAuth
consumer_key = ''  # Add your API key here
consumer_secret = ''  # Add your API secret key here
access_token = '' # get from oauth.token
access_token_secret = '' # get from oauth.token

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

tweets = [x.full_text for  x in tweepy.Cursor(api.user_timeline, screen_name='realDonaldTrump', tweet_mode="extended").items()]

tweets[1]
