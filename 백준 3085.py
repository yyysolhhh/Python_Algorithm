# def checkContinuousPart():
#     result = 1
#     for i in range(N-1):
#         candy = 1
#         for j in range(N-1):
#             if color[i][j] == color[i][j+1]:
#                 candy += 1
#             else:
#                 candy = 1
#             if candy > result:
#                 result = candy
#     for i in range(N-1):
#         candy = 1
#         for j in range(N-1):
#             if color[i][j] == color[i+1][j]:
#                 candy += 1
#             else:
#                 candy = 1
#             if candy > result:
#                 result = candy
#     return result


# N = int(input())
# color = list(list(input()) for _ in range(N))
# maxNum = 0
# for i in range(N):
#     for j in range(N-1):
#         # 옆자리 바꾸기
#         if color[i][j] != color[i][j+1]:
#             color[i][j], color[i][j+1] = color[i][j+1], color[i][j]
#             # print(color)
#             temp = checkContinuousPart()
#             if temp > maxNum:
#                 maxNum = temp
#             # 원위치
#             color[i][j], color[i][j+1] = color[i][j+1], color[i][j]
# for i in range(N-1):
#     for j in range(N):
#         # 위아래 바꾸기
#         if color[i][j] != color[i+1][j]:
#             color[i][j], color[i+1][j] = color[i+1][j], color[i][j]
#             # print(color)
#             temp = checkContinuousPart()
#             if temp > maxNum:
#                 maxNum = temp
#             # 원위치
#             color[i][j], color[i+1][j] = color[i+1][j], color[i][j]
# print(maxNum)

def check(board, start_row, start_col, end_row, end_col):
    result = 1
    # 바꾼 행에서 연속된 사탕 색 개수 세기
    for i in range(start_row, end_row+1):
        candy = 1
        for j in range(N-1):
            if board[i][j] == board[i][j+1]:
                candy += 1
            else:
                candy = 1
            if candy > result:
                result = candy
    # 바꾼 열에서 연속된 사탕 색 개수 세기
    for i in range(start_col, end_col+1):
        candy = 1
        for j in range(N-1):
            if board[j][i] == board[j+1][i]:
                candy += 1
            else:
                candy = 1
            if candy > result:
                result = candy
    return result


N = int(input())
board = list(list(input()) for _ in range(N))
max_num = 0
for i in range(N):
    for j in range(N):
        # 옆자리 바꾸기
        if j < N-1:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            temp = check(board, i, j, i, j+1)
            if temp > max_num:
                max_num = temp
            # 원위치
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        # 위아래 바꾸기
        if i < N-1:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            temp = check(board, i, j, i+1, j)
            if temp > max_num:
                max_num = temp
            # 원위치
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
print(max_num)

# 틀림
# for i in range(N):
#     for j in range(N-1):
#         # 옆자리 바꾸기
#         if board[i][j] != board[i][j+1]:
#             board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
#             max_num = max(max_num, check(board, i, j, i, j+1))
#             # temp = check(board, i, j, i, j+1)
#             # if temp > max_num:
#             #     max_num = temp
#             # 원위치
#             board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

#         # 위아래 바꾸기
#         if board[j][i] != board[j+1][i]:
#             board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
#             max_num = max(max_num, check(board, j, i, j+1, i))
#             # temp = check(board, j, i, j+1, i)
#             # if temp > max_num:
#             #     max_num = temp
#             # 원위치
#             board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
# print(max_num)
