# 014 １から指定の数まで縦に表示
# 014 1から指定の数まで複数行にわたり数値を表示する
# 行数はプログラムの先頭で変数に代入することで指定

print('回答１')
count = 7
num = 1

for i in range(count):
    print(num,end='')
    num += 1
    print()

print('回答１の改良版')

count = 7
num = 1

for i in range(count):
    print(num)
    num += 1

# 別解
print('別解')
count = 7

for i in range(count):
    print(i + 1, end='')
    print()

# 別解の改良版
print('別解の改良版')
count = 7

for i in range(count):
    print(i + 1)

# 解答例
print('解答例')
count = 7

for i in range(1, count + 1): # 1からcountまで繰り返す
    print(i)