# 007 横ストライプ
# 奇数行にのみ文字「■」を並べて表示し、横向きのストライプを表示
# 行数や列数はプログラムの先頭で変数に代入することで指定すること

row = 5
col = 7

for i in range(row):
    if i % 2 == 0:
        for j in range(col):
            print('■', end='')
            j += 1
    else:
        pass
    print()
    i += 1