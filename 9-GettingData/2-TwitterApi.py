from twython import Twython
from collections import Counter

# fill these in if you want to use the code
CONSUMER_KEY = "mKwEDKNUvABUPNOjfMSALT2Pr"
CONSUMER_SECRET = "VcjUuzW9KCwS8Gqx7OoHMhAvnkXlNyqf04Qyy9dH8epMNtBPp4"
ACCESS_TOKEN = "100512518-ukGyvgKfu1OVAx1xnwRLbJZQPapyNfJuS0odb7UR"
ACCESS_TOKEN_SECRET = "XGbFcfqyUAZR92CD26npSNqA5KaZ4Czw9pvxxKCunLfQ3"

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET)

# search for tweets containing the phrase "data science"
for status in twitter.search(q='"data science"')["statuses"]:
	user = status["user"]["screen_name"].encode('utf-8')
	text = status["text"].encode('utf-8')
	print user, ":", text
	print

from twython import TwythonStreamer

# appending data to a global variable is pretty poor form
# but it makes the example much simpler
tweets = [] 

class MyStreamer(TwythonStreamer):
    """our own subclass of TwythonStreamer that specifies
    how to interact with the stream"""

    def on_success(self, data):
        """what do we do when twitter sends us data?
        here data will be a Python object representing a tweet"""

        # only want to collect English-language tweets
        if data['lang'] == 'en':
            tweets.append(data)

        # stop when we've collected enough
        if len(tweets) >= 1000:
            self.disconnect()

    def on_error(self, status_code, data):
        print status_code, data
        self.disconnect()

def call_twitter_streaming_api():
    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, 
                        ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # starts consuming public statuses that contain the keyword 'data'
    stream.statuses.filter(track='data')

call_twitter_streaming_api()
top_hashtags = Counter(hashtag['text'].lower()
    for tweet in tweets
    for hashtag in tweet["entitles"]["hashtags"])
print(top_hashtags.most_common(5))