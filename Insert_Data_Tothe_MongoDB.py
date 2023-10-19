import asyncio
import json
from twscrape import API, gather, api
from twscrape.logger import set_log_level
from contextlib import aclosing
from datetime import datetime, date
import pandas as pd
from mongodb_connection import get_mongodb_client  # Import the function



async def main():
    # Get the MongoDB client from the separate file
    client = get_mongodb_client()

    api = API()  # or API("path-to.db")

    # ADD ACCOUNTS (for CLI usage see BELOW)
    await api.pool.add_account("@Tharusha_Iqz", "Thar@5962!", "tharushaanjula666@outlook.com", "Thar@5962!")
    await api.pool.add_account("@NuvindaC", "Nuvinda8838!", "nuvi8838@gmail.com", "Nuvinda8838!")


    await api.pool.login_all()


    # API USAGE

    # Insert the following data into MongoDB
    db = client["Twitter_Data"]
    collection = db["Tweets"]

    df = pd.read_excel('twitter channels.xlsx')

    df2 = df.groupby("Category")["User_ID"].apply(list).reset_index(name="user_id_list")
    y= 1

    for i in range(len(df2)):
        for user_id in df2.loc[i, "user_id_list"]:

                for tweet in await gather(api.user_tweets(user_id, limit=5000)):

                    user_dict = tweet.dict()
                    tweet_date = user_dict["date"].date()
                    if tweet_date == date.today():
                        # result = collection.insert_one(user_dict)
                        # inserted_id = result.inserted_id
                        # print(f"Inserted document with ID: {inserted_id}")
                        print("date is",tweet_date)



        print(f'###########################{y} category is done################################')
        y += 1





    print('Successfully Collect the Data')


if __name__ == "__main__":
    asyncio.run(main())
