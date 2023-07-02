# PDFファイルをOCR処理するプログラム
# !apt-get install -qq tesseract-ocr
# !apt-get install -qq libtesseract-dev
# !apt-get install -qq poppler-utils
# !pip install -q pytesseract
# !pip install -q pdf2image

# 対応言語
#https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html
# 日本語の場合
#!apt-get install -qq tesseract-ocr-jpn

# Tesseractの言語データパスを設定
import os
os.environ["TESSDATA_PREFIX"] = "/usr/share/tesseract-ocr/4.00/tessdata"

import pytesseract
from pdf2image import convert_from_path
from PIL import Image

# PDFファイルのパス
pdf_path = "日本語.pdf"

# PDFを画像に変換
images = convert_from_path(pdf_path)

text = ""

# 各ページの画像に対してOCRを実行
for image in images:
    # 画像を一時的に保存してOCRを実行
    image_path = "temp_image.jpg"
    image.save(image_path)

    # OCRを実行してテキストを取得
    page_text = pytesseract.image_to_string(Image.open(image_path), lang='chi_tra')  # 言語データに合わせて指定

    # テキストを結合
    text += page_text

# テキストを表示
print(text)
