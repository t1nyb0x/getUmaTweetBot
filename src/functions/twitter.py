import tweepy
# from config import token
from datetime import timedelta

class Listener(tweepy.StreamListener):
    def on_status(self, status):
        status.created_at += timedelta(hours=9)  # 世界標準時から日本時間に

        # #ゲームウマ娘のツイートのみ出力する
        if ('#ゲームウマ娘' in status.text):
            # print('------------------------------')
            print(status.text)
            print("{name}({screen}) {created} via {src}\n".format(
                name=status.author.name, screen=status.author.screen_name,
                created=status.created_at, src=status.source))

        return True

    def on_error(self, status_code):
        print('エラー発生: ' + str(status_code))
        return True

    def on_timeout(self):
        print('Timeout...')
        return True


class Twitter():
    def __init__(self, ck: str, csk: str, at: str, ast: str, uma: str):
        # auth = tweepy.OAuthHandler(token.API_KEY, token.API_SECRET_KEY)
        auth = tweepy.OAuthHandler(ck, csk)
        # auth.set_access_token(token.ACCESS_TOKEN, token.ACCESS_SECRET_TOKEN)
        auth.set_access_token(at, ast)
        self.api = tweepy.API(auth)

        # ウマ娘の公式TwitterIDを格納
        self.uma_twiId = uma

    def startStream(self):
        listener = Listener()
        myStream = tweepy.Stream(auth=self.api.auth, listener=listener)
        # ウマ娘のツイートストリームを取得開始
        myStream.filter(follow=[self.uma_twiId], is_async=True)
