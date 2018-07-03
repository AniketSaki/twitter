from nltk.corpus import wordnet as wn
import random
from bot_config import *
import twitter

verbs = list(wn.all_synsets('v'))
nouns = list(wn.all_synsets('n'))

api = twitter.Api(consumerKey, consumerSecret, accessToken, accessTokenSecret)
tweet = random.choice(nouns).name().split('.')[0] + " " + random.choice(verbs).name().split('.')[0]
status = api.PostUpdate(tweet)
del api
