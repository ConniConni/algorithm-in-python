# 027 文字数が指定数以下のデータのみを表示
# 文字列型の配列に格納された複数の文字列データについて、
# 文字数が指定数以下のデータのみを先頭から表示する
# 操作対象の配列はプログラムの先頭で宣言して、初期値を代入
# 文字数も変数に代入することで指定

array = ["abc", "abcd", "abcde" , "xx", "yyy"]  # 配列の宣言と初期化
num = 3

for i in range(len(array)):
    if len(array[i]) <= num:
        print(array[i])
    else:
        pass