# 034 最小値の探索
# 配列に格納された数値データのうち、
# 最小値とその格納位置（添字）を表示
# 操作対象の配列はプログラムの先頭で宣言して、初期値を代入

ary = [68, 55, 72, 93, 87]    # コピー元の配列の宣言と初期化
min_value = ary[0]
min_index = 0


for i in range(1, len(ary)):
    if ary[i] < min_value:
        min_value = ary[i]
        min_index = i

print(min_value)
print(min_index)