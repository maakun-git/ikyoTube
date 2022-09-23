# 各チャンネルの情報を出力する

from apiclient.discovery import build
from apiclient.errors import HttpError
from config import Config

config = Config()

YOUTUBE_API_KEY = config.api_key
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

cId = ['UC56lh82cD7lUz2rg7deYdAw', # アイドル教室メインチャンネル
       'UCJlJX_UnSegdENRPWtOFXLw', # アイドル教室サブチャンネル
       'UCkSDNSZxvWCMC_mRhT2z-sQ', # アイドル教室musicチャンネル
       'UCFCwO4zhO84JDUvs8QUDM-w', # アイドル教室旧2ndチャンネル
       'UCVWpv6M08brx2VfEZC7uOsg', # あいじゅにラバー
       'UCPKzKqWwVWR_ph46bV3ayTA'] # パステルガレット

print(cId)

search_response = youtube.channels().list(
    part='snippet,statistics',
    id=cId,
).execute()

total = 0

for item in search_response["items"]:
    print('チャンネル名:',item['snippet']['title'])

    # url = "https://www.youtube.com/c/pops262"
    # url = "https://www.youtube.com/channel/UCJlJX_UnSegdENRPWtOFXLw"
    
    if 'customUrl' in item['snippet'] :
         print('customUrl:',item['snippet']['customUrl'])
    
    print('id:',item['id'])
    print('登録者数:',item['statistics']['subscriberCount'],'人')
    print('公開動画数:',item['statistics']['videoCount'],'本')
    print('総再生数:',item['statistics']['viewCount'],'回')
    total = total + int(item['statistics']['videoCount'])

print(total)

#    print('チャンネル名:',search_response['items'][0]['snippet']['title'])
#    print('登録者数:',search_response['items'][0]['statistics']['subscriberCount'],'人')
#    print('投稿動画数:',search_response['items'][0]['statistics']['videoCount'],'本')
#    print('総再生数:',search_response['items'][0]['statistics']['viewCount'],'回')
