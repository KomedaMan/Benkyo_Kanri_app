"""可読性の向上を目的として、フレームをクラス化して作成してみる"""

import tkinter as tk
from tkcalendar import DateEntry

class MainFrame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=1440, height=1024)
        self.root = root

        self.title_form = Title(self.root)
        self.input_form = InputForm(self.root)

        self.title_form.pack()
        self.input_form.pack()

class Title(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=1000, height=200,
                         borderwidth=1, relief="ridge", background="lightblue")
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.title_text()

    def title_text(self):
        # タイトル
        title = tk.Label(self,
                         text="勉強記録",
                         font=("Arial", 30, "bold"),
                         background="lightblue")
        title.pack(pady=(50, 0))
        explain = tk.Message(self,
                             text="日付と勉強記録を入力すると今日やった分の"
                                  "勉強記録が振り返れます。",
                             width=720,
                             background="lightblue")
        explain.pack(pady=10)

class InputForm(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=720, height=400)
        self.root = root
        self.pack(anchor="nw")
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
        date_label.grid(row=0, column=0, padx=(100, 10), pady=10)
        self.date_entry = DateEntry(self,width=12, background='green',
                foreground='white', borderwidth=20, locale='ja_JP')
        self.date_entry.grid(row=0, column=1, padx=20, pady=10)

        # 問題数




root = tk.Tk()
root.title("GUI_test_app")
root.geometry("1440x1024")
app = MainFrame(root=root)
app.mainloop()