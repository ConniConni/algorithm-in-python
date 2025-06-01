# 010 三角形に文字を並べる
# 文字「■」を複数行に渡り数を１つずつ増やしながら表示する
# 行数はプログラムの先頭で変数に代入することで指定

row = 8

for i in range(row):
    for j in range(i+1):
        print('■',end='')
    print()
