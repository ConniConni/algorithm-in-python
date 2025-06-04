# オプション問題　データ構造　配列の基本

# 1. 整数形5個分の配列を宣言し、利用できるようにしてください
array = [0] * 5
print(array)

# 2. 添字指定で代入
array[0] = 10
array[1] = 25
array[2] = 9
array[3] = 3
array[4] = 15
print(array)

# 3. 0番目のデータの内容を表示
print(array[0])

# 4. 1番のデータと4番のデータの和
sum = array[1] + array[4]
print(sum)

# 5. 新しい配列（整数形3個分）を宣言（）配列宣言と同時に初期化
array2 = [4, 8, 12]
print(array2)

# 6. １つ目の配列の3番のデータと２つ目の配列の2番のデータを掛け算
mul = array[3] * array2[2]
print(mul)