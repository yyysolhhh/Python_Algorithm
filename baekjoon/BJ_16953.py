from collections import deque
import sys

# 메모리 초과
# def bfs(A):
#     queue = [A]
#     while queue:
#         # 1. 큐에서 꺼내옴
#         curr = queue.pop(0)
#         # 2. 목적지인가?
#         if curr == B:
#             return visited[curr]
#         # 3. 연결된 곳을 순회
#         for i in (curr * 2, int(str(curr) + '1')):
#             #   4. 갈 수 있는가?
#             if A <= i <= B and not visited[i]:
#                 #   5. 체크인
#                 visited[i] = visited[curr] + 1
#             #   6. 큐에  넣음
#                 queue.append(i)
#     return (-2)


# input = sys.stdin.readline
# A, B = map(int, input().split())
# visited = [0 for _ in range(B + 1)]
# print(bfs(A) + 1)

def bfs(A):
    queue = deque([(A, 0)])
    while queue:
        curr, cnt = queue.popleft()
        if curr == B:
            return cnt
        for i in (curr * 2, int(str(curr) + '1')):
            if A <= i <= B:
                queue.append((i, cnt + 1))
    return (-2)


input = sys.stdin.readline
A, B = map(int, input().split())
print(bfs(A) + 1)
