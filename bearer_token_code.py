import requests
from requests.utils import requote_uri
import base64

bearer_token_endpoint = "https://api.twitter.com/oauth2/token"
user_lookup_endpoint = "https://api.twitter.com/1.1/users/lookup.json"
user_status_endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json"
user_mentions_endpoint = "https://api.twitter.com/1.1/statuses/mentions_timeline.json"

def get_bearer_token(key, secret):
  token = key + ":" + secret
  token = requote_uri(token)
  b64_token = base64.b64encode(token.encode('utf-8'))

  headers = {
      "Authorization": "Basic " + b64_token.decode('utf-8') + "",
      "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
      # "Content-Length": "29"}

  response = requests.post(url = bearer_token_endpoint,
                           data = { 'grant_type':'client_credentials'},
                           headers=headers)
  return(response)

response = get_bearer_token('', # your key here
                            '') # your secret here

def lookup_users(bearer, screen_names):
  response = requests.get(url = user_lookup_endpoint,
                          headers = {'Authorization' : "Bearer " + bearer},
                          params = {'screen_name' : screen_names})
  return(response)

def lookup_tweets(bearer, screen_names):
  response = requests.get(url = user_status_endpoint, 
                          headers = {'Authorization' : "Bearer " + bearer},
                          params = {'screen_name' : screen_names})
  return(response)

bearer_token = response.json().get('access_token')
recent_tweets = lookup_tweets(bearer_token, ['realdonaldtrump']).json() # 25073877
