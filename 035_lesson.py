# 035 最大値の探索
# 配列に格納された数値データのうち、
# 最大値とその格納位置（添字）を表示
# 操作対象の配列はプログラムの先頭で宣言して、初期値を代入

ary = [68, 55, 72, 93, 87]  # コピー元の配列の宣言と初期化
max_value = ary[0]  # 最大値の宣言と初期化
max_index = 0  # 最大値の格納位置の宣言と初期化

for i in range(1, len(ary)):  # 2番目の要素から要素数分繰り返す
    if max_value < ary[i]:  # 現在の最大値が配列に格納された数値データより小さいとき
        max_value = ary[i]  # 最大値を更新
        max_index = i  # 最大値の格納位置を更新

print(max_value)  # 最大値を表示
print(max_index)  # 最大値の格納位置を表示

print("##### 別解 #####")

ary = [68, 55, 72, 93, 87]  # コピー元の配列の宣言と初期化
max_index = 0  # 最大値の格納位置の宣言と初期化

for i in range(1, len(ary)):
    if ary[max_index] < ary[i]:
        max_index = i

print(ary[max_index])
print(max_index)
