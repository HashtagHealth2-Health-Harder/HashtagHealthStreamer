# -*- coding: utf-8 -*-
"""
	Twitter Streamer for HashtagHealth. 

	Created by Gabby 'newfound strawberry lover' Ortman. 
"""

import tweepy as ty
import pickle
from keys import *


# override tweepy.StreamListener to create HashtagHealth stream listener.
# http://docs.tweepy.org/en/v3.4.0/streaming_how_to.html
class HashtagHealthListener(ty.StreamListener): 
	"""
		Twitter Streamer for HashtagHealth
		More documentation here pls
	"""
	def on_status(self, status): 
		timestamp = '{}:{}'.format(status.created_at, status.timestamp_ms)
		tweet_id = status.id
		# serialize tweet for later processing 
		# ...move to a better directory
		with open('{}-{}.pickle'.format(timestamp, tweet_id), 'wb') as f: 
			pickle.dump(status, f, pickle.HIGHEST_PROTOCOL)

	def on_error(self, error): 
		pass

def set_twitter_auth(): 
	"""
		Authorize via Twitter API
	"""
	auth = ty.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
	api = ty.API(auth, wait_on_rate_limit= True, wait_on_rate_limit_notify= True)
	return api

if __name__ == '__main__':
	api = set_twitter_auth(); 
	health_listener = HashtagHealthListener()
	health_stream = ty.Stream(auth = api.auth, listener = health_listener)
	health_stream.filter(track=["cold"]) #lists of identifiers
	# health_stream.sample() #live tweets
	# with open('2017-06-15 03:25:19:1497497119262-875192467766730752.pickle', 'rb') as f:
	# 	data = pickle.load(f)
	# 	print(data)
	# 	print(type(data))
	# 	print(data.text)