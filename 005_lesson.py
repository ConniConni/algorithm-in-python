# row = 5
# col = 5

# for i in range(row):
#     for j in range(col):
#         print('●', end='')
#         # j += 1
#     print()
#     # print('\n', end='')
#     # i += 1

# 別解

row = 5
col = 5
i = 0

while i < row:
    j = 0
    while j < col:
        print('●', end='')
        j += 1
    print()
    i += 1