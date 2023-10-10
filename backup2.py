import asyncio
import json
from twscrape import API, gather, api
from twscrape.logger import set_log_level
from contextlib import aclosing
from mongodb_connection import get_mongodb_client  # Import the function


async def main():
    # Get the MongoDB client from the separate file
    client = get_mongodb_client()

    api = API()  # or API("path-to.db")

    # ADD ACCOUNTS (for CLI usage see BELOW)
    await api.pool.add_account("@Tharush28383713", "Tharushaiqz12", "tharushaiqz@gmail.com", "Tharushaiqz12")

    await api.pool.login_all()

    # API USAGE

    user_id = 44196397
    user_tweets = await gather(api.user_tweets(user_id, limit=20))

    # Insert the following data into MongoDB
    db = client["Twitter"]
    collection = db["Twitter_Data"]

    for user in user_tweets:
        user_dict = user.dict()
        result = collection.insert_one(user_dict)
        inserted_id = result.inserted_id
        print(f"Inserted document with ID: {inserted_id}")



if __name__ == "__main__":
    asyncio.run(main())
