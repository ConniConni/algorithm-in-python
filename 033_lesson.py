# 033 配列データから目的のデータを探す（線形探索）
# 配列に格納された複数の文字列データの中から、
# 指定した文字列（探索キー）の格納位置（添字）を表示
# 操作対象の配列はプログラムの先頭で宣言して、初期値を代入
# 探索キーもプログラムの先頭で代入
# 指定の文字列が配列の文字列データに含まれない場合は文字列「Not found」を表示

ary = ["abc", "abcd", "abcde", "xx", "yyy"]    # 配列の宣言と初期化
search_key = "abcde"            # 探索キーの宣言と初期化

print(" ##### 回答 #####")
match_count = 0

for i in range(len(ary)):
    if ary[i] == search_key:
        match_count += 1
        print(i)
if match_count == 0:
    print("Not found")

print(" ##### 別解 #####")

for i in range(len(ary)):
    if ary[i] != search_key:
        pass
    else:
        break
if i + 1 < len(ary):
    print(i)
else:
    print("Not found")

print(" ##### 模範解答 #####")

i = 0 # カウンタ変数
while i < len(ary):
    if ary[i] == search_key:
        break
    i += 1

if i < len(ary):
    print(i)
else:
    print("Not found")