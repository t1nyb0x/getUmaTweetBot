import discord
from discord.ext import commands
from config import token
from umafunc import uma_tweet

# CK = token.API_KEY
# CSK = token.API_SECRET_KEY
# AT = token.ACCESS_TOKEN
# AST = token.ACCESS_SECRET_TOKEN
UMA = token.UMA_MUSU_TWITTERID
TOKEN = token.DISCORD_TOKEN
BEARER = token.BEARER
prefix = '?uma '


class HelpCommand(commands.DefaultHelpCommand):
    def __init__(self):
        super().__init__()
        self.commands_heading = 'コマンド:'
        # self.no_category = 'その他'
        # self.command_attrs['help'] = ""


class Uma(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    def subscribeUma(self):
        """
        ウマ娘公式のツイートを監視する
        """
        twitter = uma_tweet.GetTweet(bearer=BEARER, uma=UMA)
        uma_tweets = twitter.get_uma_twi(limit='10')
        res = "\n".join(uma_tweets)
        return res

    @commands.command()
    async def startSubscribe(self, ctx):
        res = self.subscribeUma()
        await ctx.send(res)


bot = commands.Bot(command_prefix=prefix,
                   help_command=HelpCommand())
bot.add_cog(Uma(bot=bot))
bot.run(TOKEN)
