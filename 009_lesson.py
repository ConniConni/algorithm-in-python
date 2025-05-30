# 市松模様
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