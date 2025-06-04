# 026 配列の内容をカンマ区切りで表示
# 配列に格納されたデータを先頭から順にカンマ区切りで表示する
# 操作対象の配列はプログラムの先頭で宣言して、初期値を代入

array = [10, 20, 30, 40, 50]  # 配列の宣言と初期化

for i in range(len(array)):
    print(array[i], end="")
    if i != len(array)-1:
        print(end=",")
    else:
        break
print()