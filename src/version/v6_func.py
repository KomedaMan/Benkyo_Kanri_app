from decimal import Decimal, ROUND_HALF_UP

def test_calc(que, cor):

    if que == 0:        # 問題数が0ならば処理しない
        return
    elif que < cor:     # 問題数が正答数より多いなら、不正なので処理しない。
        return
    else:
        try:
            rate = Decimal(str((cor / que) * 100)).quantize(Decimal("0.01"),
                                                            rounding=ROUND_HALF_UP)
        except ValueError:  # 半角数字以外が入力されたとき、不正なので処理しない。
            return

