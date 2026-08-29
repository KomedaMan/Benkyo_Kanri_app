import os
import json

def append_to_json(file_path, new_data):
    """
    jsonファイルにデータを追加する関数
    :param file_path: JSONファイルのパス
    :param new_data: 追加するデータ（dictまたはlist）
    :return:
    """
    try:
        # ファイルが存在すれば読み込み、なければ空のリストを作成
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="UTF-8") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []   # JSONが壊れている場合は空にする
        else:
            data = []

        # データ型を確認して追加
        if isinstance(data, list):  # dataがlistのとき
            data.append(new_data)
        elif isinstance(data, dict): # dataがdictのとき
            if isinstance(new_data, dict):
                data.update(new_data)
            else:
                raise ValueError("辞書型のJSONに追加する場合はdictを渡してください。")
        else:
            raise ValueError("サポートされていないJSON構造です。")

        # 上書き保存（インデント付で見やすく）
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print("データを追加しました。")

    except Exception as e:
        print(f"エラーが発生しました: {e}")

# 使用例
if __name__ == "__main__":
    file_path = "test_data2.json"
    date = input("日付")
    question = int(input("問題"))
    corrects = int(input("回答"))
    new_entry  = {
        "date": date,
        "question": question,
        "corrects": corrects
    }
    append_to_json(file_path, new_entry)
