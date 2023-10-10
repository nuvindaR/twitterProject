import asyncio
import json

from twscrape import API, gather
from twscrape.logger import set_log_level
from connection import db_connection

async def main():
    api = API()  # or API("path-to.db") - default is `accounts.db`

    # ADD ACCOUNTS (for CLI usage see BELOW)
    # await api.pool.add_account("@Tharush28383713", "Tharushaiqz12", "tharushaiqz@gmail.com", "Tharushaiqz12")

    await api.pool.add_account("@NuvindaC", "Nuvinda8838!", "nuvi8838@gmail.com", "Nuvinda8838!")

    await api.pool.login_all()

    client = db_connection()

    db = client.twitter_data
    tweets_collection = db.tweets
    new_tweets = list()

    user_id = 44196397

    for tweet in await gather(api.user_tweets(user_id, limit=20)):
        new_tweets.append(json.loads(tweet.json()))

    result = tweets_collection.insert_many(new_tweets)
    document_ids = result.inserted_ids
    print(f"ids of the inserted documents: {document_ids}")
    client.close()

    # NOTE 1: gather is a helper function to receive all data as list, FOR can be used as well:
    # async for tweet in api.user_by_id(1701675223295352832):
    #
    #     print(tweet.id, tweet.user.username, tweet.rawContent)




    set_log_level("DEBUG")


if __name__ == "__main__":
    asyncio.run(main())