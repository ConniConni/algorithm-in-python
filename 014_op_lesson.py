# 014 オプション問題繰り返しの増分式の活用　奇数の表示
# 014 1から指定の数まで複数行にわたり奇数だけを表示する
# 行数はプログラムの先頭で変数に代入することで指定

n = 7

for i in range(1, n +1):
    if i % 2 == 1:
        print(i)
    else:
        pass

# 別解1
n = 7

for i in range(1,n+1,2):
    print(i)

# 別解2

n = 7
i = 1

while i <= n:
    print(i)
    i += 2