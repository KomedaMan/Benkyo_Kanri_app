"""入力と出力が正しくできる
入力：問題数、正答数
出力；正答率
"""

def calc():
    try:
        que_num = int(input("何問解きましたか？（半角の数字で入力）"))
        cor_ans_num = int(input("何問正答しましたか？（半角の数字で入力）"))

        if que_num == 0:
            print("今日は問題を解きませんでしたね。")
            return calc()
        elif que_num < cor_ans_num:
            print('不正な入力です。 "解いた問題数 >= 正答数" となるように入力してください。')
            return calc()
        else:
            cor_rate = round((cor_ans_num / que_num) * 100 , 2)
            return cor_rate
    except ValueError:
        print("問題数、回答数はそれぞれ半角数字で入力してください")
        return calc()


def main():
    output = calc()
    print("正答率:" + str(output) + "%")

main()