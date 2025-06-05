# 029 配列データのコピー
# 配列に格納された複数の数値データを別に要した配列に同じ並びでコピーする
# コピー先の配列はコピー元の配列と同じ型・同じ要素数となるようにプログラムの先頭で宣言
# 操作対象の配列はプログラムの先頭で宣言して、初期値を代入
# 文字数も変数に代入することで指定
# コピー前とコピー後の２回コピー先の配列の内容を表示

base_array = [10, 20 ,30, 40 ,50]  # コピー元の配列の宣言と初期化
#new_array = [0, 0 ,0, 0 ,0]  # コピー先の配列の宣言と初期化
new_array = [0] * len(base_array)


def print_array(array):
    for i in range(len(array)):
        print(array[i])

print_array(new_array)

for i in range(len(base_array)):
    new_array[i] = base_array[i]

print_array(new_array)



# めも
# base_array[i]を取り出し、
# new_array[i]に代入