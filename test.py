import argparse

from twitter.oauth import OAuth
from twitter.stream import TwitterStream, Timeout, HeartbeatTimeout, Hangup
from twitter.util import printNicely

from config import *


# connect to my twitter timeline and print out the tweets

def parse_arguments():
    parser = argparse.ArgumentParser(description=__doc__ or "")
    parser.add_argument('-us', '--user-stream', action='store_true', help='Connect to the user stream endpoint.')
    parser.add_argument('-ss', '--site-stream', action='store_true', help='Connect to the site stream endpoint.')
    parser.add_argument('-to', '--timeout', help='Timeout for the stream (in seconds).')
    parser.add_argument('-ht', '--heartbeat-timeout', help='Set heartbeat timeout.', default=90)
    parser.add_argument('-nb', '--no-block', action='store_true', help='Set stream to non-blocking.')
    parser.add_argument('-tt', '--track-keywords', help='Search the stream for specific text.')
    return parser.parse_args()


def main():
    args = parse_arguments()

    auth = OAuth(accessToken, accessTokenSecret, consumerKey, consumerSecret)

    stream_args = dict(
        timeout=args.timeout,
        block=not args.no_block,
        heartbeat_timeout=args.heartbeat_timeout)

    query_args = dict()
    if args.track_keywords:
        query_args['track'] = args.track_keywords

    if args.user_stream:
        stream = TwitterStream(auth=auth, domain='userstream.twitter.com', **stream_args)
        tweet_iter = stream.user(**query_args)
    elif args.site_stream:
        stream = TwitterStream(auth=auth, domain='sitestream.twitter.com', **stream_args)
        tweet_iter = stream.user(**query_args)
    else:
        stream = TwitterStream(auth=auth, **stream_args)
        if args.track_keywords:
            tweet_iter = stream.statuses.filter(**query_args)
        else:
            tweet_iter = stream.statuses.sample()

    for tweet in tweet_iter:
        if tweet is None:
            printNicely("-- None --")
        elif tweet is Timeout:
            printNicely("-- Timeout --")
        elif tweet is HeartbeatTimeout:
            printNicely("-- Heartbeat Timeout --")
        elif tweet is Hangup:
            printNicely("-- Hangup --")
        elif tweet.get('text'):
            print(tweet['user']['screen_name'] + ": " + tweet['text'])
        else:
            printNicely(str(tweet))


if __name__ == '__main__':
    main()
