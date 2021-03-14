from typing import Any
import requests
from datetime import timedelta
import json
import os


class GetTweet():
    def __init__(self, bearer: str, uma: int):
        self.bearer = bearer
        # ウマ娘の公式TwitterIDを格納
        self.uma_twi_id = uma
        self.uma_screen_name = 'uma_musu'
        self.hash_tag = '%23ゲームウマ娘'

        self.url = 'https://api.twitter.com/2/tweets/search/recent?query=from:' + \
            str(self.uma_twi_id) + '%20' + self.hash_tag + \
            '&tweet.fields=created_at&max_results='
        self.headers = {'Authorization': '{}'.format(self.bearer)}
        self.json_path = 'tweetdata/previous_data.json'

    def get_uma_twi(self, limit: str):
        """
        ウマ娘公式のツイートURLを取得する

        Parameters
        ----------
        limit: str
            取得件数

        Returns
        -----------
        uma_tweets: list
            ツイートURL配列を返す
        """
        uma_tweets = []
        r = requests.get(self.url + limit, headers=self.headers)
        tweets = r.json()

        # jsonファイルが存在している場合は、前回の最新IDを基準に取得する
        if os.path.isfile(self.json_path):
            prev_data = self.read_previous_data()
            # 取得したツイートから、ツイートIDを取得する
            for tweet in tweets['data']:
                if prev_data['newest'] < tweet['id']:
                    uma_tweets.append('https://twitter.com/' +
                                    self.uma_screen_name + '/status/' + tweet['id'])
        else:
            for tweet in tweets['data']:
                uma_tweets.append('https://twitter.com/' +
                                  self.uma_screen_name + '/status/' + tweet['id'])

        self.save_previous_data(tweets)

        return uma_tweets

    def read_previous_data(self):
        """
        前回取得したツイートの最新IDを取得する

        Returns
        -------
        previous_data: dict
        """
        with open(self.json_path, mode='r') as f:
            previous_data = f.read()

        return json.loads(previous_data)

    def save_previous_data(self, tweets: Any):
        """
        今回取得した最新のツイートIDを書き込む

        Parameters
        ----------
        tweets : Any
            取得したツイートデータ

        Returns
        ----------
        None
        """

        newest_id = tweets['meta']['newest_id']
        previous_data = json.dumps(
            {'newest': newest_id}, separators=(',', ':'))

        with open(self.json_path, mode='w') as f:
            f.write(previous_data)
