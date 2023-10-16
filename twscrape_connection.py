import os

from twscrape import API

async def twscrape_conn():
    api = API()

    TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")
    TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
    EMAIL = os.getenv("EMAIL")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

    # ADD ACCOUNTS
    await api.pool.add_account(TWITTER_USERNAME, TWITTER_PASSWORD, EMAIL, EMAIL_PASSWORD)
    await api.pool.add_account("@RaviNuv88976", "Nuvi@8838!", "iqztr001@gmail.com", "Nuvi@8838!")
    await api.pool.add_account("@Tharusha_Iqz", "Thar@5962!", "tharushaanjula666@outlook.com", "Thar@5962!")

    await api.pool.login_all()

    return api
