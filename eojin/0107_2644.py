"""
Baekjoon #2644 촌수계산
- 알고리즘: BFS
    - 참고할 점: BFS는 queue를 통해 구현 (시작 노드의 인접 노드를 큐에 enqueue(append) > dequeue(popleft)하여 방문 처리하며 검사)

- 문제
우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 이러한 촌수는 다음과 같은 방식으로 계산된다. 기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.
여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.

- 입력
사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다. 입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다. 그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.

9 < 전체 사람 수
8 6 < 촌수를 계산해야 하는 사람 번호
7 < 부모 자식간 관계 수
1 2 < 2의 부모 1
1 3
2 7
2 8
2 9
4 5
4 6

각 사람의 부모는 최대 한 명만 주어진다.

- 출력
입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다. 어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 이때에는 -1을 출력해야 한다.

- 오답노트
    - 그래프를 제대로 정의하지 않아도 해결할 수 있을 것 같아서 1차원 그래프(자식 인덱스로 부모를 조회하는~)로 정리해봤는데 의미 없는 회전도 카운트하다보니 오류가 있는듯...
        - addflag를 통해서 큐에 값이 추가될 때만 length 값을 증가시켰는데 이 경우도 의미 없는 추가가 같이 카운트됨
        - 귀찮다고 flag를 늘리지 말고 알고리즘 자체의 문제를 찾아야 함
    - 뭔가 같은 스텝에 추가된 값에 대해선 length를 증가시키지 않게 하면 될 것 같은데,,, 그러려고 뭔가 더 넣고 싶진 않다
        - 현재 아이템을 빼고(popleft)난 후에 큐가 비어있는 경우에만 length를 증가 < 안됨, 그야 당연히... 꼭 마지막 경우 쪽으로만 가진 않으니까,,,
    - 챗지피티 힌트) 최상위 조상
        - 한 아이템에서 다른 아이템까지로 탐색하는 게 아니라, 각 아이템의 최상위 조상을 찾고 그 경로를 비교하면 된다
            - 그러면 BFS에서 너무 멀어지지 않나?
    - 다시 굴려봄) 큐에 사람하고 거리 정보를 둘 다 저장해서 계산... < 이거 된다
        - 구현하면서 틀렸던 거
            - 인덱스( 찾아보니 0-based / 1-based를 혼용해서 써서 그렇다고 함... 앞으로는 입력 받을 때부터 0-based로 고쳐 받는 게 좋을듯)
            - python 문법상 != 보다는 is not이나 not을 쓰는 게 좀 더 익숙해지면 좋을듯 (가독성이 좀 더 좋아진다)
"""
from collections import deque

allp = int(input()) # 전체 사람 수
a, b = map(int, input().split()) # 촌수를 계산해야 하는 각각의 사람 번호
n = int(input()) # 부모 자식들 간의 관계의 개수
parent = [None] * allp

for _ in range(n):
    p, c = map(int, input().split())
    parent[c-1] = p

deq = deque([(a, 0)])
visited = [False] * allp
visited[a-1] = True
length = None

while deq:
    curr, dist = deq.popleft()
    # 부모 검사
    if not (visited[parent[curr-1]-1] if parent[curr-1] is not None else True):
        if parent[curr-1] == b:
            length = dist + 1
            break
        deq.append((parent[curr-1], dist+1))
        visited[parent[curr-1]-1] = True
    # 자식 검사
    for i in range(allp):
        if parent[i] == curr and (not visited[i]):
            if i == b - 1:
                length = dist + 1
                break
            deq.append((i+1, dist+1))
            visited[i] = True
    if length is not None: break

print(length if length is not None else -1)