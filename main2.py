import tkinter as tk
import tkinter.filedialog as fd
base = tk.Tk()
def open() :
    filename = fd.askopenfilename()
    print('ファイルを開く => ' + filename)
def exit() :
    base.destroy()
def find() :
    print('見つけた！')

menubar = tk.Menu(base)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label='ファイル', menu=filemenu)
filemenu.add_command(label='開く', command=open)
filemenu.add_separator()
filemenu.add_command(label='終了', command=exit)
editmenu = tk.Menu(menubar)
menubar.add_cascade(label='編集', menu=editmenu)
editmenu.add_command(label='検索', command=find)
base.config(menu=menubar)
base.mainloop()
