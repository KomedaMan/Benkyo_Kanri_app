"""v5よりもよりフレームの使い方をシンプルにした。
日付欄はカレンダーにする

次は値をリストに保存したりする。
これはメインに渡すことになる？
後々データベース化するため、そこに渡すデータとなる。
"""

import tkinter as tk
from tkcalendar import DateEntry
from src.version.v6_func import test_calc


# GUI関数（メイン処理で使えるように関数化する。）
def test_gui2():
    # 計算ボタンを押したときの処理をする関数
    def button_push():
        text_react = ""
        que = que_entry.get()
        cor = cor_ans_entry.get()
        # 結果を記載するテキストを生成
        try:
            text_react = "正答率：" + test_calc(que, cor) + "%"
        except TypeError:
            text_react = "入力が不正です"
        result_text.config(text=text_react)

    # rootの作成
    root = tk.Tk()
    root.title("GUI_test_app")
    root.geometry("1440x1024")

    # ====================================================
    # フレーム作成について
    # ====================================================

    #フレームの作成
    frame = tk.Frame(root, width=1440, height=1024)
    frame.propagate(False)
    frame.pack()

    # ヘッダー（入力欄）フレームの作成
    header_frame = tk.Frame(frame, width=1440, height=400)
    header_frame.propagate(False)
    header_frame.pack(pady=50)

    # mid(計算用）フレームの作成
    mid_frame = tk.Frame(frame, width=1440, height=200)
    mid_frame.propagate(False)
    mid_frame.pack(pady=50)

    # ====================================================
    # 各機能について
    # ====================================================

    # 日付
    date_label =tk.Label(header_frame, text="日付", font=("Arial", 20))
    date_label.grid(row=0, column=0, padx=10, pady=10)
    date_entry = DateEntry(header_frame, width=50, background="green",
                           foreground="white", borderwidth=10, lovate="ja_JP")
    date_entry.grid(row=1, column=0, padx=10, pady=10)

    # 解いた問題数
    que_label = tk.Label(header_frame, text="解いた問題数", font=("Arial", 20))
    que_label.grid(row=0, column=1, padx=10, pady=10)
    que_entry = tk.Entry(header_frame, width=50)
    que_entry.grid(row=1, column=1, padx=10, pady=10)

    # 正答数
    cor_ans_label = tk.Label(header_frame, text="正答数", font=("Arial", 20))
    cor_ans_label.grid(row=0, column=2, padx=10, pady=10)
    cor_ans_entry = tk.Entry(header_frame, width=50)
    cor_ans_entry.grid(row=1, column=2, padx=10, pady=10)

    result_text = tk.Label(mid_frame, text="", font=("Arial", 30))
    result_text.pack(pady=10, side="bottom")

    # 計算ボタン
    cal_button = tk.Button(mid_frame, text="計算", command=button_push)
    cal_button.pack(pady=10, side="top")



    root.mainloop()

# 動作チェック
test_gui2()