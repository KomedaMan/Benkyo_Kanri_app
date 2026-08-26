"""
~~やること~~
・出力に「今日解いた問題数」、「今日の正答数」を追加して表示できるようにする。=>済
・リストかなんかで、出力した値を記憶できるようにする

===今やらないが、今後すること===
・グラフ化
・データベース化
"""

import tkinter as tk
from tkcalendar import DateEntry
from src.version.func.v1_func import test_calc
from src.version.data import v1_data

# 記憶用リスト{"日付":oo, "問題数":oo, "正答数":oo}
# record =[]
"""
record.append({
"date": (str)date, 
"questions": (int)que,
""corrects": (int)cor,
})
で追加する
もしかしたらこれはメイン処理で持っていたほうがいいかも
=>新たにdata保存用のディレクトリを作成してそこに保存
後々データベースを保存
"""



# アプリケーション全体のフレーム作成用
class MainFrame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=1440, height=1024)

        # 部品ごとのフレーム
        self.title_form = Title(self)
        self.input_form = InputForm(self, self.button_push)
        self.output_form = OutputForm(self)

        self.title_form.grid(row=0,column=0, columnspan=2)
        self.input_form.grid(row=1, column=0, padx=10, pady=20)
        self.output_form.grid(row=1, column=1, padx=10, pady=20)

    # 計算ボタンを押下したときの処理
    def button_push(self):
        """計算ボタンを押したときに正答率をOutputFrameに記載する"""
        date, que, cor = self.input_form.get_values()
        que = int(que)
        cor = int(cor)
        try:
            """この辺の処理系はfuncに書いたほうがいいかも？"""
            # データがあるとき
            if v1_data.record:
                exists = any(d.get("date") == date for d in v1_data.record)
                data_num = len(v1_data.record)
                # dateがすでにあるならば、更新にする
                if exists:
                    for i in range(data_num):
                        if v1_data.record[i]["date"] == date:
                            v1_data.record[i]["questions"] = que
                            v1_data.record[i]["corrects"] = cor
                # ないならば追加する
                else:
                    v1_data.record.append({
                        "date": date,
                        "questions": que,
                        "corrects": cor
                    })
            # データがない場合は、追加処理をする
            else:
                v1_data.record.append({
                    "date": date,
                    "questions": que,
                    "corrects": cor
                })
            # データが二つ以上あるとき、昨日のデータと今日のデータの差を出力する
            if len(v1_data.record) > 1:
                que_today = v1_data.record[-1]["questions"]
                que_yesterday = v1_data.record[-2]["questions"]

                cor_today = v1_data.record[-1]["corrects"]
                cor_yesterday = v1_data.record[-2]["corrects"]
                # 問題数と正答数がともに今日のほうが多くなっているとき、昨日との差を求める
                # （正答数は昨日と同じでもよい。)
                if que_today > que_yesterday and cor_today >= cor_yesterday:
                    que = que_today - que_yesterday
                    cor = cor_today - cor_yesterday
                # 昨日よりも問題を解いているにも関わらず、昨日よりも正答数が少ない場合、
                # 新しく問題を始めたとカウントするので、処理はしない。
                elif que_today > que_yesterday and cor_today < cor_yesterday:
                    pass
                # 問題数は同じなのに正答数が昨日より多くなっているときは入力が不正とする
                elif que_today == que_yesterday and cor_today > cor_yesterday:
                    raise TypeError
                # 昨日と今日で値が変わっていないときは、今日は何もしていないと判定するため、
                # 処理を行わず、先に記録した今日のレコードのデータを破棄する
                elif que_today == que_yesterday and cor_today == cor_yesterday:
                    del v1_data.record[-1]
                # 昨日と今日で問題数が変わっておらず、正答数が少なくなった場合は
                # 新しく問題を始めたとカウントするので、処理しない。
                elif que_today == que_yesterday and cor_today < cor_yesterday:
                    pass
                # 昨日よりも問題数が少なくなった時は新しく問題を始めたとカウントする
                else:
                    pass

            text_que = "解いた問題：" + str(que) + " 問"
            text_cor = "正答数：" + str(cor) + " 問"
            text_rate = "正答率" + test_calc(que, cor) + "%"
        except TypeError:
            text_que = ""
            text_cor = ""
            text_rate = "入力が不正です"
        self.output_form.result_que_text.config(text=text_que)
        self.output_form.result_cor_text.config(text=text_cor)
        self.output_form.result_text.config(text=text_rate)

# アプリケーション上部のタイトルとその説明に使用するフレーム作成用
class Title(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=1440, height=200,
                         borderwidth=1, relief="ridge", background="lightblue")
        self.pack_propagate(0)
        self.title_text()

    def title_text(self):
        """アプリケーションの見出しとその説明分を記載するための処理"""
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

# アプリケーションの中央左側に位置する値を入力するためのフォーム作成用
class InputForm(tk.Frame):
    """
    中央左側に入力用のフレームを作成する。
    計算ボタンのコマンドはMainFrameからオブジェクトを作る際に引き渡された関数を使用。
    そのため、そのコマンド関数はMainFrameに記載されている
    入力された値はMainFrameのボタン押下関数の処理に使用されるため、引き渡すための関数が
    定義されている。。
    """
    def __init__(self,root, button_push):
        super().__init__(root, width=600, height=200,
                         borderwidth=1, relief="groove")
        self.pack_propagate(0)
        self.create_input_widgets()
        # 計算ボタン
        calc_button = tk.Button(self, text="計算", command=button_push)
        calc_button.pack(side="bottom", pady=10)

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

    # メインフレームへ問題数と正答数の値を渡す関数
    def get_values(self):
        """
        MainFrameのbutton_push関数の処理用に値を返す。
        MainFrameで値を直接定義すると子クラスとの内部構造に依存するため、
        関数を作りそれを渡したほうがよいと考え作成。
        """
        date = self.date_entry.get()
        que = self.que_entry.get()
        cor = self.ans_entry.get()
        return date, que, cor


# アプリケーションの中央左側に位置する計算などの結果を出力するフォーム作成用
class OutputForm(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=600, height=200,
                         borderwidth=1, relief="groove")
        self.pack_propagate(0)
        self.create_output_widgets()

    # 計算後の出力を表示する処理
    def create_output_widgets(self):
        """
        InputFrameの入力フォームに各値を入力後、計算ボタンを押した後に記載される文字を制御する
        初期は計算前なのでテキストは空となっている。
        ボタンを押し、計算されるとこのテキストがconfigで書き換えられる
        """
        # この下に今日解いた問題数を表示する処理を記載する
        self.result_que_text = tk.Label(self, text="", font=("Arial", 20))
        self.result_que_text.pack(pady=(10,0))

        # この下に今日解いた正答数を表示する処理を記載する。
        self.result_cor_text = tk.Label(self, text="", font=("Arial", 20))
        self.result_cor_text.pack()

        # 正答率を表示する
        self.result_text = tk.Label(self, text="", font=("Arial", 30))
        self.result_text.pack()

# GUI作成メイン処理
def main():
    root = tk.Tk()
    root.title("GUI_test_app")
    root.geometry("1440x1024")
    app = MainFrame(root=root)
    app.pack()
    app.mainloop()

if __name__ == '__main__':
    main()
