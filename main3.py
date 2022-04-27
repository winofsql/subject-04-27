#モジュール読込
# https://di-acc2.com/programming/python/3678/
import requests
import tkinter as tk
base = tk.Tk()

# 関数定義(function)
def push() :
    print('押された')
    url = "https://avatars.githubusercontent.com/u/1501327?v=4"
    response = requests.get(url)
    file = open("1501327.jpg","wb")
    #iter_content()メソッドでWebファイルのデータを渡す
    for chunk in response.iter_content(100000):
        #ファイル書込
        file.write(chunk)
    
    #ファイルを閉じる
    file.close()
    print('完了')

button = tk.Button(base,text='ボタン', command=push).pack()
base.mainloop()
