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

- 좀 더 깔끔하게 고칠 순 없나...
    - python 문법에서 !=랑 is not은 용례상 차이가 있는 듯 함
        - !=는 값만 비교 / is not은 객체가 같은 메모리를 참조하는지 비교(객체 참조 비교) => 그래서 None의 경우에는 is not None 사용
    - None은 0이나 False랑 같이 취급되는 듯? 조건식을 좀 더 알아보자
        - python 문법상 None / 0 / False / 이외 공백문자열은 같게 취급함 => None이 아닌 경우만을 필요로 하면 is not None을 쓰는 게 정확하긴 하다
    - enumerate() 라는 함수가 있음! 이 경우 인덱스와 값을 동시에 활용 가능, 이 부분 활용해서 코드 고치면 좀 더 가독성 올라갈듯
    - python은 ! 연산자를 사용하지 않음! 대신 not 키워드를 사용한다
    - 지금 인덱스 참조가 1-based index랑 0-based index를 혼용해서 헷갈리는 부분이 좀 있음 => 1-based index로 입력받은 값을 0-based index로 처음부터 맞춰주는 게 좋을듯?
        - 근데 이러면 0으로 if문이 false 판정 날 경우를 대비해야 할듯
    - if not (visited[parent[curr-1]-1] if parent[curr-1] else True):는 너무 가독성이 떨어지고 지저분함 => parent 값의 None 여부를 먼저 검사하면 깔끔
    - return을 통해 깔끔하게 종료할 수 있게 다음부터는 함수로 만들어보기
"""
from collections import deque

allp = int(input()) # 전체 사람 수
a, b = map(int, input().split()) # 촌수를 계산해야 하는 각각의 사람 번호
n = int(input()) # 부모 자식들 간의 관계의 개수
parent = [None] * allp # parent 배열(=어떤 사람(인덱스)에 대한 부모 값을 갖는 배열)을 None으로 초기화

# 관계 입력받아 parent에 저장
for _ in range(n):
    p, c = map(int, input().split())
    parent[c-1] = p

deq = deque([(a, 0)]) # 덱 생성 후 (출발점, dist(거리)) 튜플 추가
visited = [False] * allp # 방문한 노드 표시 배열 False로 초기화
visited[a-1] = True # 첫번째 노드를 방문 표시
length = None # 최종 거리 저장 겸 플래그용 변수

while deq: # 덱이 빌 때까지 반복
    curr, dist = deq.popleft()
    # 부모 검사
    if parent[curr-1] and not visited[parent[curr-1]-1]: # parent 값이 None일 경우 오류 회피 위해 parent 값을 먼저 검사하도록 함
        if parent[curr-1] == b: # 부모 노드가 도착점과 일치할 경우 탈출
            length = dist + 1
            break
        deq.append((parent[curr-1], dist+1)) # 거리를 1 추가하여 덱에 추가
        visited[parent[curr-1]-1] = True # 방문하였음을 체크
    # 자식 검사
    for i, p in enumerate(parent): # enumerate() 함수를 사용하여 for문에서 인덱스와 값 둘 다 사용
        if p == curr and not visited[i]: # curr의 자식이고 방문하지 않은 노드
            if i == b-1: # 자식 노드 중 도착점과 일치하는 노드가 있으면 탈출
                length = dist + 1
                break
            deq.append((i+1, dist+1)) # 거리를 1 추가하여 덱에 추가
            visited[i] = True # 방문 여부 체크
    if length is not None: break # length가 None이 아니게 되면 도착점을 찾은 것이므로 루프 탈출(for문 탈출 후 while문 종료용)

print(length if length is not None else -1)