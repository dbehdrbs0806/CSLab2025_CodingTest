# 문제 설명

# 첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다.
# 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다.
# N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

row, col = map(int, input().split())
num_list1 = []
num_list2 = []
result_list=[]

for i in range(row):
    num_list1.append(list(map(int, input().split())))
for i in range(row):
    num_list2.append(list(map(int, input().split())))

for i in range(row):
    colList = []
    for j in range(col):
        colList.append(num_list1[i][j]+num_list2[i][j])
    for j in colList:
        print(j, end=' ')
    print('')