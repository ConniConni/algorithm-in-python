# 008 縦ストライプ
# 複数行にわたり奇数列に文字列「■」
# 偶数列に文字「　」（全角スペース）を交互に並べて表示

row = 5
col = 7

for i in range(row):
    for j in range(col):
        if j % 2 == 0:
            print('■',end='')
        else:
            print('　',end='')
    print()