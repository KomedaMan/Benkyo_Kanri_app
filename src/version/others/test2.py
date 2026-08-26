data = [{"a": 1, "b": 2, "c": 3}]

data.append({"a": 4, "b": 5, "c": 6})

print(data)

print(len(data))

print(data[-2]["a"] + data[-1]["b"])

# リスト内辞書の要素に対する値が存在するかどうかを調べる方法
a = int(input())
exists = any(d.get("a") == a for d in data)
if exists:
    print("ある")
else:
    print("ない")