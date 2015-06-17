import tweepy, datetime, sys
import random
import twitterKeys
 
class TwitterAPI:
    def __init__(self):
        auth = tweepy.OAuthHandler(twitterKeys.consumer_key, twitterKeys.consumer_secret)
        auth.set_access_token(twitterKeys.access_token, twitterKeys.access_token_secret)
        self.api = tweepy.API(auth)
 
    def tweet(self, message):
        self.api.update_status(status=message)

toPrint = True

while True:
    current_time = datetime.datetime.now()
    #print current_time
    #print current_time.minute
    #Attributes: hour, minute, second, microsecond, and tzinfo
    if current_time.second == 00:
        if toPrint == True:
            print current_time
            toPrint = False
            if __name__ == "__main__":
                firstList = open('pulpNovels.txt','r')
                secondList = open('finish.txt', 'r')
                
                first = firstList.readlines()
                second = secondList.readlines()
                first = [n.replace('\n', '') for n in first]
                firstList.close()
                secondList.close()

                tweet = random.choice(first) + random.choice(second)    

            print tweet
            #twitter = TwitterAPI()
            #twitter.tweet(tweet)
    elif current_time.second != 00:
        toPrint = True
        #print current_time.second







     