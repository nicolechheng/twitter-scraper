import snscrape.modules.twitter as sntwitter
import pandas as pd

tweets_list1 = []
tweets_list2 = []
tweets_list3 = []
count = 0

for i, tweet in enumerate(
        sntwitter.TwitterSearchScraper('always since:2019-01-01 until:2019-01-02').get_items()):
    if i > 50:
        break
    #tweets_list1.append([tweet.date, tweet.id, tweet.content])
    count = i

# Creating a dataframe from the tweets list above
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text'])
#tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text'])
#tweets_df3 = pd.DataFrame(tweets_list3, columns=['Datetime', 'Tweet Id', 'Text'])
print(count)
