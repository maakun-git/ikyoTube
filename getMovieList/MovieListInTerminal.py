## Youtubeの動画リストをターミナルに出力する

from functools import total_ordering
from apiclient.discovery import build
from apiclient.errors import HttpError
from config import Config

config = Config()

# No module named 'apiclient'　エラー(YouTube Data API(v3)) 出た場合
# https://qiita.com/SEI_Go/items/df354b639506d9a2cd82

YOUTUBE_API_KEY = config.api_key

youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

cId = ['UC56lh82cD7lUz2rg7deYdAw', # アイドル教室メインチャンネル
       'UCJlJX_UnSegdENRPWtOFXLw', # アイドル教室サブチャンネル
       'UCkSDNSZxvWCMC_mRhT2z-sQ', # アイドル教室musicチャンネル
       'UCFCwO4zhO84JDUvs8QUDM-w', # アイドル教室旧2ndチャンネル
       'UCVWpv6M08brx2VfEZC7uOsg', # あいじゅにラバー
       'UCPKzKqWwVWR_ph46bV3ayTA' # パステルガレット
       ]

search_response = youtube.search().list(
    part="snippet",
    channelId= cId[0],  # 取得するチャンネルの要素番号を入れる
    maxResults=200,
    order="date",
    publishedAfter="2022-09-01T00:00:00Z",
    publishedBefore="2022-10-01T00:00:00Z"
).execute()

#titles = [item["snippet"]["title"] for item in search_response["items"]]

total = 0
disp = 0

for item in search_response["items"]:
    total = total + 1
    if item["id"]["kind"] == 'youtube#video':
        print(item["snippet"]["publishedAt"], ";", "https://www.youtube.com/watch?v=" + item["id"]["videoId"], ";",  item["snippet"]["title"])
        disp = disp + 1
    else:
        print(item["id"]["kind"])

print(total, disp)
