"""
사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다.
입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다.
그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다.
넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다.
이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.

각 사람의 부모는 최대 한 명만 주어진다.
"""
TRUE = 1
FALSE = 0
MAX = 100

class GraphType:
    n:int = None
    adj_mat = [[0 for col in range(MAX)] for row in range(MAX)]
    count:int = None

visited = [FALSE for col in range(MAX)]
relCount = 0

def insert_edge(GraphType, start, end):
    if (GraphType.n <= start and GraphType.n <=end):
        return
    GraphType.adj_mat[start][end] = 1
    GraphType.adj_mat[end][start] = 1

def dfs_mat(GraphType, value, target):
    visited[value] = TRUE
    if (value == target):
        return relCount
    else:
        for i in range(GraphType.n):
            if (GraphType.adj_mat[value][i]==TRUE and visited[i]==FALSE):
                relCount+=1
                dfs_mat(GraphType, i, target)
        return -1


graph = GraphType()

people = int(input())
graph.n=people
tar1, tar2 = map(int, input().split())

rel = int(input())
for i in  range(rel):
    start, end = map(int, input().split())
    insert_edge(graph, start-1, end-1)

print(dfs_mat(graph, tar1-1, tar2-1))

"""
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
"""