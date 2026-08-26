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

def data_input(date, que, cor):
    """入力されたデータに対して、リストに追加をするか更新するかを判断して処理する"""
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

def data_today_yesterday(que, cor):
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
            return que, cor
        # 昨日よりも問題を解いているにも関わらず、昨日よりも正答数が少ない場合、
        # 新しく問題を始めたとカウントするので、処理はしない。
        elif que_today > que_yesterday and cor_today < cor_yesterday:
            return que, cor
        # 問題数は同じなのに正答数が昨日より多くなっているときは入力が不正とする
        elif que_today == que_yesterday and cor_today > cor_yesterday:
            raise TypeError
        # 昨日と今日で値が変わっていないときは、今日は何もしていないと判定するため、
        # 処理を行わず、先に記録した今日のレコードのデータを破棄する
        elif que_today == que_yesterday and cor_today == cor_yesterday:
            del v1_data.record[-1]
            que = 0
            cor = 0
            return que, cor
        # 昨日と今日で問題数が変わっておらず、正答数が少なくなった場合は
        # 新しく問題を始めたとカウントするので、処理しない。
        elif que_today == que_yesterday and cor_today < cor_yesterday:
            return que, cor
        # 昨日よりも問題数が少なくなった時は新しく問題を始めたとカウントする
        else:
            return que, cor
    else:
        return que, cor
