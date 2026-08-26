from decimal import Decimal, ROUND_HALF_UP
from src.version.data import v1_data

def test_calc(que, cor):
    try:
        que = int(que)
        cor = int(cor)

        if que == 0:  # 問題数が0ならば処理しない
            return
        elif que < cor:  # 問題数が正答数より多いなら、不正なので処理しない。
            print("ooi")
        else:
            rate = Decimal(str((cor / que) * 100)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            # rateはdecimal型なのでstrに変形する
            return str(rate)
    except ValueError:
        print("ValueError")
        return

def data_input(data, que, cor):



