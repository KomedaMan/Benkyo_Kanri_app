"""GUIの作成と動作を関数化してmainで使用できるようにする。"""
import tkinter as tk

from src.version.v6_func import test_calc

# GUI関数（メイン処理で使えるように関数化する。）
def test_gui():

    def button_push():
        que = entry_que.get()
        cor = entry_cor_ans.get()
        print(test_calc(que, cor) + "%")
    #    上を消してここの下にGUIに結果を載せる処理を書く

    root = tk.Tk()
    root.title("GUI_test_app")
    root.geometry('1440x1024')

    # 入力欄フレームの作成
    frame_input = tk.Frame(root, width=1440, height=512, bg="gray")
    # frame_input.propagate(False)    #サイズを固定する
    frame_input.pack()

    # 日付フレームの作成
    frame_date = tk.Frame(frame_input, width=400, height=500, bg="black")
    frame_date.grid(row=0, column=0)

    # 解いた問題数フレームの作成
    frame_que = tk.Frame(frame_input, width=400, height=500, bg="white")
    # frame_que.propagate(False)
    frame_que.grid(row=0, column=1)

    # 正答数フレームの作成
    frame_cor_ans = tk.Frame(frame_input, width=400, height=500, bg="blue")
    frame_cor_ans.grid(row=0, column=2)

    # 出力フレーム
    frame_output = tk.Frame(root, width=1440, height=512)
    frame_output.pack()

    # 日付欄の記述
    label_date = tk.Label(frame_date, text="日付", background="gray")
    label_date.pack(pady=10)
    entry_date = tk.Entry(frame_date, width=50)
    entry_date.pack(padx=10, pady=10)

    # 解いた問題数欄の記述
    label_que = tk.Label(frame_que, text="解いた問題数")
    label_que.pack()
    entry_que = tk.Entry(frame_que, width=50)
    entry_que.pack(padx=10, pady=10)

    # 正答数欄の記述
    label_cor_ans = tk.Label(frame_cor_ans, text="正答数")
    label_cor_ans.pack()
    entry_cor_ans = tk.Entry(frame_cor_ans, width=50)
    entry_cor_ans.pack(padx=10, pady=10)

    # 計算ボタン
    button_cal = tk.Button(frame_que, text="計算", command=button_push)
    button_cal.pack(pady=10)

    # 結果記載用テキスト
    text = tk.StringVar(frame_output)
    text.set("")

    # メインループ
    root.mainloop()





test_gui()
