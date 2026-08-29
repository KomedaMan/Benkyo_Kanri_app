import json

file_name = "test_data.json"

data = {
    "date" :"8/26",
    "question" :100,
    "corrects" : 20
}

with open(file_name, "w") as json_file:
    json.dump(data, json_file, indent=4)
# データ構造をjson型式に変換するために使用できる。

data2 = {
    "date": "8/27",
    "question": 200,
    "corrects": 50
}

with open(file_name, "w") as json_file:
    json.dump(data2, json_file, indent=4)

print(f"jsonファイルが作成されました：　{json_file}")