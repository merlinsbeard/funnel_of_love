import requests
import time
from requests_oauthlib import OAuth1
import subprocess
import os

auth = OAuth1(os.environ['twit1'],os.environ['twit2'],os.environ['twit3'],os.environ['twit4'])

#auth = OAuth1('kFm2KNvl0c0W3hLknjTryqrUs','hKi5wwrln94tNJ6oeSGeUQoFU5WgInPouwIkcObGKBmfeXQurr','2826340932-KK0FOPpyFUNC3YG2GNNwaquvDxguPCSzAHeXHt0','y9gC0RFNfCYnckiq6VPrpJd00Q0OFlUHwC7aebq7To69g')

url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=hallo_caffeine"

r=requests.get(url, auth=auth)

tweets=r.json()

oldest = tweets[0]
print 'old tweet', oldest['text']

while True:
    get_tweets = requests.get(url, auth=auth)
    tweets = get_tweets.json()
    new_tweet = tweets[0]
    if new_tweet['id'] != oldest['id']:
        oldest = new_tweet
        print oldest['text']
        print subprocess.call ('python subprocess20.py', shell=True)
        print "===================="
    time.sleep(10)
    print subprocess.call('waiting for new tweets', shell=True)


