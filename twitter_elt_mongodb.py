import asyncio
import json
from datetime import datetime

from twscrape import API, gather
from twscrape.logger import set_log_level
from mongodb_connection import db_connection

import pandas as pd

from twscrape_connection import twscrape_conn


async def main():
    #create twscrape connection
    api = await twscrape_conn()

    # create mongodb connection
    client = db_connection()
    db = client.twitter_data
    tweets_collection = db.tweets

    #read excel file containing twitter categories and channel details
    df = pd.read_excel('twitter channels.xlsx')

    df2 = df.groupby("Category")["User_ID"].apply(list).reset_index(name="user_id_list")
    new_tweets = list()
    #loop through each category and user_id and make api call to retrieve tweets
    for i in range(len(df2)):
        category = df2.loc[i, "Category"]

        for user_id in df2.loc[i, "user_id_list"]:
            for tweet in await gather(api.user_tweets(user_id, limit=5000)):
                tweet_json = json.loads(tweet.json())
                tweet_json['category'] = category
                tweet_json['inserted_date_time'] = datetime.now()
                new_tweets.append(tweet_json)

    result = tweets_collection.insert_many(new_tweets)
    document_ids = result.inserted_ids
    print(f"ids of the inserted documents: {document_ids}")

    set_log_level("DEBUG")

    client.close()


if __name__ == "__main__":
    asyncio.run(main())