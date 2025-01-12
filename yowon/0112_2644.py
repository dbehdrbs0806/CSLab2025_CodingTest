from collections import deque

def calc_relation():
    n = int(input())  # 사람 수
    x, y = map(int, input().split())  # 촌수 계산 대상
    m = int(input())  # 관계 수

    # 그래프 생성
    graph = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # BFS 탐색
    queue = deque([(x, 0)])  # (현재 노드, 촌수)
    visited = set([x])

    while queue:
        current, distance = queue.popleft()
        if current == y:
            print(distance)
            return
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    # 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없는 경우
    print(-1)

calc_relation()
