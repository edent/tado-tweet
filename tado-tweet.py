#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json, tweepy

#   Set up the credentials
email    = "you@example.com"
password = "p4ssw0rd"
apiURL   = "https://my.tado.com/mobile/1.9/getCurrentState?username="+email+"&password="+password

#   Get the data
response = requests.get(url=apiURL)
#   Parse the data
data = json.loads(response.text)

#   The data we want
insideTemp   = data['insideTemp']
setPointTemp = data['setPointTemp']
controlPhase = data['controlPhase']

#   Set Up Twitter
twitter_access_token        = ''
twitter_access_token_secret = ''
twitter_consumer_key        = ''
twitter_consumer_secret     = ''

auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)
twitter = tweepy.API(auth)

#   Construct the Tweet
tweet  = u"Current temperature: " + str(insideTemp)   + u"℃. 🌡\n"
tweet += u"Target temperature: "  + str(setPointTemp) + u"℃. 🎯\n"
tweet += u"Mode: " + str(controlPhase) + u" 🔥\n"
tweet += u"Powered by tado°"

#   Send the Tweet
twitter.update_status(tweet)
