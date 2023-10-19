import asyncio
import json

from twscrape import API, gather, api
from twscrape.logger import set_log_level
from contextlib import aclosing

async def main():
    api = API()  # or API("path-to.db") - default is `accounts.db`vim
    # ADD ACCOUNTS (for CLI usage see BELOW)
    await api.pool.add_account("@Tharusha_Iqz", "Thar@5962!", "tharushaanjula666@outlook.com", "Thar@5962!")

    await api.pool.login_all()



    # API USAGE

    #Searching the Key word

    # async with aclosing(api.search("elon musk")) as gen:
    # async with aclosing(api.search("elon musk")) as gen:
    #       async for tweet in gen:
    #         if tweet.id < 200:
    #             break
###########################################################################################

    # NOTE 1: gather is a helper function to receive all data as list, FOR can be used as well:
    # async for tweet in api.search("elon musk"):
    #     print(tweet.id, tweet.user.username, tweet.rawContent)  # tweet is `Tweet` object

###################################################################################

    #NOTE 2: all methods have `raw` version (returns `httpx.Response` object):

    # async for rep in api.search_raw("elon musk"):
    #     print(rep.status_code, rep.json())  # rep is `httpx.Response` object


##################################################################################
    # user info
    user_id = 44196397
    # user_info = await api.user_by_id(user_id)
    # followers = await gather(api.followers(user_id, limit=20))
    following = await gather(api.following(user_id, limit=20))
    #user_tweets = await gather(api.user_tweets(user_id, limit=20))
    print(following)

    # user_tweets_replies = await gather(api.user_tweets_and_replies(user_id, limit=20))
    #
    # # Print the results
    # print("User Info:", user_info)
    # print("Followers:", followers)
    # print("Following:", following)
    # print("User Tweets:", user_tweets)
    # print("User Tweets and Replies:", user_tweets_replies)



 #####################################################################################



    # change log level, default info
    set_log_level("DEBUG")

    # Tweet & User model can be converted to regular dict or json, e.g.:

    # doc = await api.user_by_id(user_id)  # User
    # doc.dict()  # -> python dict
    # doc.json()  # -> json string




if __name__ == "__main__":
    asyncio.run(main())