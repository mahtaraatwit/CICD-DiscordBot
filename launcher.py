from lib.bot import bot
from server import keep_alive

runner = bot.Bot()
keep_alive()
runner.run()