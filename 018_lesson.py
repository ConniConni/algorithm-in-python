# 018 指定の数から１まで縦に表示
# 1以上の指定の数から1までの数複数行に渡り順に表示する
# 行数はプログラムの先頭で変数に代入することで指定

n = 10              # 指定の数を設定

for i in range(n):  # 0からn-1までn回繰り返す
    num = n - i     # 表示する数値を格納
    print(num)      # 数値を表示し、改行

print('***** 別解1 *****')

n = 10

while n > 0:
    print(n)
    n -= 1

print('***** 別解2 *****')

n = 10                      # 表示する最大の数

for i in range(n, 0 , -1):  # nから1まで１ずつ減らす
    print(i)                # iを表示