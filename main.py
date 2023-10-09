import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level

async def main():
    api = API()  # or API("path-to.db") - default is `accounts.db`

    # ADD ACCOUNTS (for CLI usage see BELOW)
    await api.pool.add_account("@Tharush28383713", "Tharushaiqz12", "tharushaiqz@gmail.com", "Tharushaiqz12")

    await api.pool.login_all()



    # NOTE 1: gather is a helper function to receive all data as list, FOR can be used as well:
    async for tweet in api.search("Sri Lanka Cricket"):
        print(tweet.id, tweet.user.username, tweet.rawContent)  # tweet is `Tweet` object


    set_log_level("DEBUG")


if __name__ == "__main__":
    asyncio.run(main())