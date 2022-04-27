# 画像変換に必要なライブラリを読み込むここから
import os
from PIL import Image
# 画像変換に必要なライブラリを読み込むここまで

# このソースコードが保存されているフルパスを取得する
# current_dirname = C:\app\workspace\subject-0427\python-0427-01\
current_dirname = os.path.dirname(__file__) + '\\'

# 変換対象の画像ファイルを開く
# C:\app\workspace\subject-0427\python-0427-01\files\flower01.jpg
image = Image.open(current_dirname + 'files/flower01.jpg')
# 変換対象の画像ファイルを表示
image.show()

# RGB毎に分離
r, g, b = image.split()

# RGB→BGRに置き換え
# 赤と青を入れかて合体(merge)している
convert_image = Image.merge("RGB",(b, g, r))

# 変換後の画像を保存
convert_image.save(current_dirname + 'files/flower01_convert.jpg')

# 変換した画像を表示する
convert_image.show()
