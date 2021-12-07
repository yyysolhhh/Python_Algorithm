import heapq
T = int(input())
for _ in range(T):
    k = int(input())
    max_heap = []
    min_heap = []
    visited = [False for _ in range(k)]
    for i in range(k):
        op, num = input().split()
        num = int(num)
        if op == 'I':   # 삽입
            heapq.heappush(max_heap, (-1 * num, i))
            heapq.heappush(min_heap, (num, i))
            visited[i] = True
        elif op == "D":   # 삭제
            if num == 1:    # 최댓값 삭제

                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            elif num == -1:   # 최솟값 삭제
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
        print(max_heap, min_heap, visited)
    if max_heap and min_heap and max_heap[0][1] != min_heap[0]:
        print(max_heap[0][1], min_heap[0])
    else:
        print('EMPTY')
