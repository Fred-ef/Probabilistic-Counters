from utils.stream import *

def message_length():
    happy_msg_len = 0
    sad_msg_len = 0

    happy_tweet_counter = 0
    sad_tweet_counter = 0

    x = mystream("data_sets/sample.csv")
    s = x.nextRecord ()

    while s is not None:
        words = x.tokenizedTweet()
        tweet_len = 0
        # count number of characters of the tweet
        for word in words:
            tweet_len += len(word) + 1 # +1 for the space between words
        
        if x.ispositive():
            happy_msg_len += (tweet_len - 1) / 280 # we are removing the final space and renormalizing wrt max tweet length
            happy_tweet_counter += 1
        else:
            sad_msg_len += (tweet_len - 1) / 280
            sad_tweet_counter += 1
        
        s = x.nextRecord ()

    print("Average length of happy users' tweets:", round(happy_msg_len * 280/happy_tweet_counter))
    print("Average length of unhappy users' tweets:", round(sad_msg_len * 280/sad_tweet_counter))