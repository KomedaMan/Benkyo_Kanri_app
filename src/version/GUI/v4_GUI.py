"""可読性の向上を目的として、フレームをクラス化して作成してみる"""

import tkinter as tk
from tkcalendar import DateEntry

class InputForm(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=720, height=400,
                         borderwidth=1, relief='groove')
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_input_widgets()

    # 入力欄ウィジェットの作成
    def create_input_widgets(self):
        """入力欄（日付、回答数、正答数）のウィジェットを作成する"""
        """ 
        ==selfについて==
        入力欄は変数としてクラス外で使用する必要があるかもしれないので
        インスタンス変数として持っておく。
        クラス変数=>全インスタンスが共有する変数
        ローカル変数=>関数の処理内で完結できる変数
        インスタンス変数=>メソッドの実行が終了した後も保持する変数
        """

        # 日付
        date_label = tk.Label(self, text="日付")
        date_label.pack(row=0, column=0)
        self.date_entry = tk.Entry(self)
        self.date_entry["width"] = 50
        self.date_entry.grid(row=0, column=1)

        # 問題数




root = tk.Tk()
root.title("GUI_test_app")
root.geometry("1440x1024")

root.mainloop()