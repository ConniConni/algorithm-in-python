# 031 配列データの平均
# 配列に格納された数値データの平均を求め表示する
# 操作対象の配列はプログラムの先頭で宣言して、初期値を代入

ary = [68, 55, 72, 93, 87]    # コピー元の配列の宣言と初期化
ary_ave = 0                   # 平均値の格納先
ary_sum = 0                   # 足し算の結果の格納先

for i in range(len(ary)):     # 配列の要素の数分繰り返す
    ary_sum += ary[i]         # 配列の要素を足す

ary_ave = ary_sum / len(ary)  # 平均値を求める
print(ary_ave)                # 平均値を表示する