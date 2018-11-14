from bot_config import *
import twitter
import markovify

with open('brown.txt', 'r') as f:
    text = f.read()
text_model = markovify.NewlineText(text)
api = twitter.Api(consumerKey, consumerSecret, accessToken, accessTokenSecret)

tweet = text_model.make_short_sentence(140)
status = api.PostUpdate(tweet)
del api
