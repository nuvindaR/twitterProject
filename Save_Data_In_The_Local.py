import asyncio
import json
from twscrape import API, gather, api
from twscrape.logger import set_log_level
from contextlib import aclosing
from datetime import datetime
import pandas as pd
from mongodb_connection import get_mongodb_client  # Import the function

# Custom JSON encoder to handle datetime objects
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

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

    for i in range(len(df2)):
        category = df2.loc[i, "Category"]
        new_tweets = list()
        with open(category + "_v2.json", "a") as f:
            first_record = True
            for user_id in df2.loc[i, "user_id_list"]:
                for tweet in await gather(api.user_tweets(user_id, limit=5000)):
                    user_dict = tweet.dict()
                    if not first_record:
                        f.write(",\n\n")
                    else:
                        first_record = False

                    json.dump(user_dict, f, cls=DateTimeEncoder)

            print(len(user_dict))
            json.dump(new_tweets, f)






    #for user_id in user_ids:

    # with open("ESPN.json", "w") as f:
    #     first_record = True
    #     for user in user_tweets:
    #         user_dict = user.dict()
    #         #records.append(user_dict)
    #
    #         if not first_record:
    #             f.write(",\n\n")
    #         else:
    #             first_record = False
            # result = collection.insert_one(user_dict)
            # inserted_id = user_dict.inserted_id
            # print(f"Inserted document with ID: {inserted_id}")

            json.dump(user_dict, f, cls=DateTimeEncoder)


    print('Successfully Collect the Data')


if __name__ == "__main__":
    asyncio.run(main())
