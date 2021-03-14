import asyncio
from discord.ext import commands
from config import token
from umafunc import uma_tweet
import schedule
import os, signal, time

UMA = token.UMA_MUSU_TWITTERID
TOKEN = token.DISCORD_TOKEN
BEARER = token.BEARER
prefix = '?uma '
admin_id = [token.HAL, token.NAKAKOMA]


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

    async def startSchedule(self, ctx):
        """
        スケジュール実行されるメソッド
        """
        res = self.subscribeUma()
        await ctx.send(res)

    @commands.command()
    async def start(self, ctx):
        """
        ウマ娘公式ツイートのデータを取得する
        """
        user_id = ctx.message.author.id

        if str(user_id) in admin_id:
            await ctx.send('ウマ娘公式ツイート取得定期実行を開始します\n')
            #1時間毎のjob実行を登録
            schedule.every(1).hours.do(self.startSchedule)

            while True:
                # 50秒ごとに実行をペンディングする
                schedule.run_pending()
                await asyncio.sleep(30)
        else:
            await ctx.send('管理者以外からの実行はできません')

    @commands.command()
    async def stop(self, ctx):
        """
        ウマ娘公式ツイートデータ取得処理を止める
        """
        user_id = ctx.author.id
        if user_id in admin_id:
            os.exit(os.getpid(), signal.SIGTERM)
            await ctx.send('ウマ娘公式ツイート取得定期実行を停止します\n')
        else:
            await ctx.send('管理者以外からの実行はできません')


bot = commands.Bot(command_prefix=prefix,
                   help_command=HelpCommand())
bot.add_cog(Uma(bot=bot))
bot.run(TOKEN)