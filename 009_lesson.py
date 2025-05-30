# 009 市松模様
# 複数行にわたり文字「■」と文字「　」(全角スペース)を交互に並べて表示
# 奇数行の表示順は「■」と文字「　」(全角スペース)
# 偶数行の表示順は「■」と文字「　」(全角スペース)

row = 6
col = 10

for i in range(row):
    for j in range(col):
        if i % 2 == 0:
            if j % 2 == 0:
                print('■',end='')
            else:
                print('　',end='')
        else:
            if j % 2 == 0:
                print('　',end='')
            else:
                print('■',end='')
    print()

# 別解
# 文字「■」を表示するのは奇数行目の時
# 文字「　」を表示するのは偶数行目の時

row = 6
col = 10

for i in range(row):
    x = i % 2
    for j in range(col):
        if j % 2 == x:
            print('■',end='')
        else:
            print('　',end='')
    print()