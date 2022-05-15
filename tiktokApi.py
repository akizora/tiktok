import sys
import os
import time
from dotenv import load_dotenv
from TikTokApi import TikTokApi


# load_dotenv(verbose=True)
# dotenv_path = os.path.dirname('.env')
# load_dotenv(dotenv_path)

verifyfp = ''
api = TikTokApi.get_instance(use_api_endpoints = True, custom_verifyFp=verifyfp)

# 特定のハッシュタグを持つ動画を10個取得
results = 10
hashtag = 'エバーテイル'
tiktoks = api.by_hashtag(count=results, hashtag=hashtag)

# 各動画の情報をループ処理で取得
for tiktok in tiktoks:
    print(tiktok)
    # sys.exit()
    # 動画のダウンロード
    video_bytes = api.get_video_by_tiktok(tiktok)
    video_title = tiktok["id"]

# sys.exit()

# 動画のダウンロード
video_bytes = api.get_video_by_tiktok(tiktoks[0])
video_title = tiktoks[0]["id"]

# urlを指定して動画をダウンロードする場合は以下を使用
# video_bytes = api.get_video_by_url('https://www.tiktok.com/@clearlyhemo/video/7032985960992361730?is_copy_url=1&is_from_webapp=v1&q=Messi&t=1638852369929')

# 動画の保存
with open(f"{video_title}.mp4", "wb") as o:
    o.write(video_bytes)
    # urlを指定して動画をダウンロードする場合は以下を使用
    # video_bytes = api.get_video_by_url('https://www.tiktok.com/@clearlyhemo/video/7032985960992361730?is_copy_url=1&is_from_webapp=v1&q=Messi&t=1638852369929')

    # 動画の保存
    # with open(f"{video_title}.mp4", "wb") as o:
    #     o.write(video_bytes)
    # time.sleep(2)
