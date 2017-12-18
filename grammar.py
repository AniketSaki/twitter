from nltk import PCFG
import random
from bot_config import *
import twitter
import string
import time


def weighted_choice(choices):
    total = sum(w for c, w in choices)
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices:
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"


def generate_sent(grammar, items):
    frag = []
    while len(items) > 0:
        prods = grammar.productions(items[0])
        choices = []
        for prod in prods:
            choices.append((prod, prod.prob()))
        prod = weighted_choice(choices)
        print(prod.unicode_repr())
        rhs = prod.rhs()
        items.pop(0)
        if prod.is_lexical():
            frag.append(rhs)
        if prod.is_nonlexical():
            for i in rhs[::-1]:
                items.insert(0, i)
    return frag


def send_tweet():
    text = str(generate_sent(toy_pcfg, [toy_pcfg.start()]))
    tweet = ''
    for character in text:
        if character in string.ascii_letters or character in string.whitespace:
            tweet = tweet + character
    status = api.PostUpdate(tweet)
    print(status.text)
    time.sleep(1800)
    send_tweet()


toy_pcfg = PCFG.fromstring(pcfg)
api = twitter.Api(consumerKey, consumerSecret, accessToken, accessTokenSecret)
send_tweet()
