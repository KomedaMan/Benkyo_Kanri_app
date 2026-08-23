"""可読性の向上を目的として、フレームをクラス化して作成してみる"""
"""
本当は、今日の日付、今日の解いた問題数、今日の正答数、今日の正答率を出力したい。
そのためには、昨日まで解いた問題数、昨日までの正答数が保存されていなければならない。
まずはリストか辞書で管理することでそれを計算して出せるようにならなければいけない。
具体的には
record=[
{
    "date": "yyyy-mm-dd",
    "question": 100,
    "correct": 30
}
]
みたいな感じ。
正答率はリストの値から導き出される値なので保存しなくてもよい。
後々データベース化するならば正規化のことも考えて、重複する意味の値は除いたほうがよい。
"""
import tkinter as tk
from tkcalendar import DateEntry
from src.version.func.v1_func import test_calc

class MainFrame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=1440, height=1024)
        def button_push():
            que = self.input_form.que_entry.get()
            cor = self.input_form.ans_entry.get()
            try:
                text_react = "正答率" + test_calc(que, cor) + "%"
            except TypeError:
                text_react = "入力が不正です"
            self.output_form.result_text.config(text=text_react)
        self.root = root

        self.title_form = Title()
        self.input_form = InputForm(button_push)
        self.output_form = OutputForm()

        self.title_form.grid(row=0,column=0, columnspan=2)
        self.input_form.grid(row=1, column=0, padx=10, pady=20)
        self.output_form.grid(row=1, column=1, padx=10, pady=20)



class Title(tk.Frame):
    def __init__(self):
        super().__init__(root, width=1440, height=200,
                         borderwidth=1, relief="ridge", background="lightblue")
        # self.root = root
        # self.pack()
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
    def __init__(self, button_push):
        super().__init__(root, width=600, height=200,
                         borderwidth=1, relief="groove")
        self.ans_entry = None
        self.que_entry = None
        self.date_entry = None
        # self.root = root
        self.button_push = button_push
        # self.pack(anchor="nw", padx=10, pady=20)
        self.pack_propagate(0)
        self.create_input_widgets()
        # 計算ボタン
        calc_button = tk.Button(self, text="計算", command=self.button_push)
        calc_button.pack(side="bottom", pady=10)

    # 入力欄ウィジェットの作成
    def create_input_widgets(self):
        # 計算ボタンを押下したときの処理


        """入力欄（日付、回答数、正答数）のウィジェットを作成する"""
        """ 
        ==selfについて==
        入力欄は変数としてクラス外で使用する必要があるかもしれないので
        インスタンス変数として持っておく。
        クラス変数=>全インスタンスが共有する変数
        ローカル変数=>関数の処理内で完結できる変数
        インスタンス変数=>メソッドの実行が終了した後も保持する変数
        """


        # 日付(row=0)
        date_label = tk.Label(self, text="日付")
        date_label.grid(row=0, column=0, padx=20, pady=(50, 10))
        self.date_entry = DateEntry(self,width=12, background='green',
                foreground='white', borderwidth=20, locale='ja_JP')
        self.date_entry.grid(row=0, column=1, padx=20, pady=(50, 10))

        # 問題数(row=1)
        que_label =tk.Label(self, text="解いた問題数")
        que_label.grid(row=1, column=0, padx=20, pady=10)
        self.que_entry = tk.Entry(self, width=15)
        self.que_entry.grid(row=1, column=1, padx=20, pady=10)

        # 正答数(row=2)
        ans_label = tk.Label(self, text="正解数")
        ans_label.grid(row=2, column=0, padx=20, pady=(10, 50))
        self.ans_entry = tk.Entry(self, width=15)
        self.ans_entry.grid(row=2, column=1, padx=20, pady=(10, 50))



class OutputForm(tk.Frame):
    def __init__(self):
        super().__init__(root, width=600, height=200,
                         borderwidth=1, relief="groove")
        self.result_text = None
        # self.root = root
        # self.pack(anchor="nw", padx=10, pady=20)
        self.pack_propagate(0)
        self.create_output_widgets()

    def create_output_widgets(self):
        self.result_text = tk.Label(self, text="", font=("Arial", 30))
        self.result_text.pack(pady=10)

root = tk.Tk()
root.title("GUI_test_app")
root.geometry("1440x1024")
app = MainFrame(root=root)
app.mainloop()