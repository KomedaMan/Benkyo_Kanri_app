import tkinter as tk
from tkcalendar import DateEntry

root = tk.Tk()
root.title("日付選択アプリ")
root.geometry("300x200")

# カレンダー付き入力欄の作成
cal = DateEntry(root, width=12, background='green',
                foreground='white', borderwidth=20, locale='ja_JP')
cal.pack(padx=20, pady=20)

# 選択した日付を取得する関数
def show_date():
    selected_date = cal.get_date()  # date型で取得
    print(selected_date)

btn = tk.Button(root, text="日付を取得", command=show_date)
btn.pack(padx=20, pady=10)

root.mainloop()