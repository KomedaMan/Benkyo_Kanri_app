"""入力と出力が正しくできる
入力：問題数、正答数
出力；正答率
"""
from decimal import Decimal, ROUND_HALF_UP


def calc():
    """
    !問題点
    roundでは正確な正答率がでない可能性がある。
    例えば100000問解いて正答数が66665問とすると小数点2桁で四捨五入すると66.67％とならないといけないが
    偶数丸めなので66.66％と出力される
    =>この例は現実的ではないが、正確性に欠けるためdecimalを使う方法に変える
    =>驚くことにこの例ではDecimalを使っても同じ結果になった。
        これは偶数丸めによるものではないようだ。
        どうやら2進数にしたときに有効桁で表現できないことによる誤差が生じるようである。（演算誤差）
    =>inputで入力された変数自体をDecimalで表現することにより、計算過程で2進数に変換されて生じる誤差をなくすことにした。
    """
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
            que_num = Decimal(que_num)
            cor_ans_num = Decimal(cor_ans_num)
            cor_rate = Decimal(str((cor_ans_num / que_num) * 100)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            return cor_rate
    except ValueError:
        print("問題数、回答数はそれぞれ半角数字で入力してください")
        return calc()


def main():
    output = calc()
    print("正答率:" + str(output) + "%")

main()