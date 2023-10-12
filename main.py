import asyncio
import json
import os

from twscrape import API, gather
from twscrape.logger import set_log_level
from connection import db_connection

import pandas as pd

async def main():
    api = API()  # or API("path-to.db") - default is `accounts.db`

    # ADD ACCOUNTS
    TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")
    TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
    EMAIL = os.getenv("EMAIL")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

    await api.pool.add_account(TWITTER_USERNAME, TWITTER_PASSWORD, EMAIL, EMAIL_PASSWORD)

    await api.pool.login_all()

    client = db_connection()

    db = client.twitter_data
    tweets_collection = db.tweets


    #user_id = 44196397

    df = pd.read_excel('twitter channels.xlsx')

    df2 = df.groupby("Category")["User_ID"].apply(list).reset_index(name="user_id_list")

    for i in range(len(df2)):
        category = df2.loc[i, "Category"]
        new_tweets = list()
        with open(category + ".json", "a") as f:
            for user_id in df2.loc[i, "user_id_list"]:
                for tweet in await gather(api.user_tweets(user_id, limit=100000)):
                    new_tweets.append(json.loads(tweet.json()))

            print(len(new_tweets))
            json.dump(new_tweets, f)
            #f.write("\n")

            # result = tweets_collection.insert_many(new_tweets)
            # document_ids = result.inserted_ids
            # print(f"ids of the inserted documents: {document_ids}")
    client.close()

    # NOTE 1: gather is a helper function to receive all data as list, FOR can be used as well:
    # async for tweet in api.user_by_id(1701675223295352832):
    #
    #     print(tweet.id, tweet.user.username, tweet.rawContent)

    set_log_level("DEBUG")


if __name__ == "__main__":
    asyncio.run(main())