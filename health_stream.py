# -*- coding: utf-8 -*-
"""
	Streaming porton of HashtagHealth. 

	Created by Gabby 'newfound strawberry lover' Ortman. 
"""

import tweepy as ty
from keys import *


# override tweepy.StramListener to create HashtagHealth stream listener.
# http://docs.tweepy.org/en/v3.4.0/streaming_how_to.html
class HashtagHealthListener(ty.StreamListener): 
	def on_status(self, status): 
		print(status.text)

def set_twitter_auth(): 
	"""
		Authorize via Twitter API
	"""
	auth = ty.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = ty.API(auth)
    return api

if __name__ == '__main__':
	api = set_twitter_auth(); 
	health_listener = HashtagHealthListener()
	health_stream = ty.Stream(auth = api.auth, listener = health_listener) 
	health_stream.filter()