# 036 配列データの並び替え（選択法）
# 配列に格納された数値データのについて、
# 照準になるように並び替え
# 確認のため、並び替えの前後で配列データを表示
# 操作対象の配列はプログラムの先頭で宣言して、初期値を代入

ary = [68, 55, 72, 93, 87]    # コピー元の配列の宣言と初期化

def print_ary(ary):           # 配列要素を表示する関数
    for i in range(len(ary)): # 要素数分繰り返す
        print(ary[i])         # 要素を表示する


print("並び替え前")
print_ary(ary)

for i in range(len(ary)):
    min_index = i
    for j in range(i + 1, len(ary)):
        if ary[j] < ary[min_index]:
            min_index = j

    ary[i], ary[min_index] = ary[min_index], ary[i]

print("並び替え後")
print_ary(ary)

# めも

# 最小値を探す 範囲(1,len(ary)=5)
# 最小値を0番目に移動
# 移動は前後を入れ替える
# ２回目以降は未整列の範囲で最小値を探す 範囲(2,len(ary)=5)
# 3回目の最小値を探す 範囲(3,len(ary)=5)
# 終了





# i =3 とすると
# tmp = ary[2]
# ary[2] = ary[3]
# ary[3] = tmp


# i < 1の間繰り返す
# tmp = ary[i-1]
# ary[i-1] = ary[i]
# ary[i] = tmp

# i =3 とすると
# ループ１(i=3)
# tmp = ary[2]
# ary[2] = ary[3]
# ary[3] = tmp

# ループ２(i=2)
# tmp = ary[1]
# ary[1] = ary[2]
# ary[2] = tmp

# ループ3(i=1)
# tmp = ary[0]
# ary[0] = ary[1]
# ary[1] = tmp





