#google colaboratoryで実行
#!pip install git+https://github.com/openai/whisper.git
#!pip install pydub

import whisper
from pydub import AudioSegment

#select small or medium or large
#largeを選ぶと時間はかかるが，文字起こしの精度が上がる
model = whisper.load_model("medium")

# 音声ファイルを指定
audio_file = "171721130715048.mp3"

segment_length = 30 * 1000  # ms
sound = AudioSegment.from_file(audio_file, format="mp3")

# 30秒ごとに音声を切り出す
segments = []
for i in range(0, len(sound), segment_length):
    segment = sound[i:i+segment_length]
    segment_path = f"segment_{i//segment_length}.mp3"
    segment.export(segment_path, format="mp3")
    segments.append(segment)

# 切り出された音声ファイルをリストに格納
segment_paths = [f"segment_{i}.mp3" for i in range(len(segments))]

#日本語指定で音声の文字起こし
for i in range(len(segment_paths)):
  result = model.transcribe(segment_paths[i], verbose=True, language="ja")
  print(result["text"])
