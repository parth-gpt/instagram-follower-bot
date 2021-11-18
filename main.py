from bot import InstaFollower

CHROME_DRIVER_PATH = "/Users/parth_gpt/Development/chromedriver"

bot = InstaFollower()

bot.login()
bot.find_followers()
bot.follow()
