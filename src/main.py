import discord
from discord.ext import commands
from config import token
import functions

CK = token.API_KEY
CSK = token.API_SECRET_KEY
AT = token.ACCESS_TOKEN
AST = token.ACCESS_SECRET_TOKEN
UMA = token.UMA_MUSU_TWITTERID
TOKEN = token.DISCORD_TOKEN
prefix = '?'

class Uma(command.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot


    def subscribeUma(self):
        twitter = functions.twitter.Twitter(CK, CSK, AT, AST, UMA)
        twitter.startStream()
        return

    @commands.command()
    def startSubscribe(self, ctx):
        self.subscribeUma()
        ctx.send('@uma_musuのツイート監視を始めます')


bot = commands.Bot(command_prefix=prefix)
bot.add_cog(Uma(bot=bot))
bot.run(TOKEN)