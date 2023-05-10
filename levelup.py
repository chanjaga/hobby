#　音声提供：https://chakushinon123.com/level-up-dragon-quest/ 

import time
from playsound import playsound

#　レベルアップ時間間隔
n = 5

# 最後に再生した時刻を初期化
last_reminder = time.time()

# レベルアップ音の再生
def play_levelup_sound():
    # ここに音声ファイルを指定する
    playsound('レベルアップ-ドラゴンクエスト-dragon-quest.mp3')
    
# 作業中にレベルアップ！！
while True:
    # 現在時刻と最後の通知表示時刻を比較
    if time.time() - last_reminder > n:
        play_levelup_sound()
        last_reminder = time.time()
    
    # 1秒待機して再度比較
    time.sleep(1)
