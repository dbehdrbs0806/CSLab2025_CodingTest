1# 문제 설명

# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 위치한 행 번호와 열 번호를 빈칸을 사이에 두고 차례로 출력한다.
# 최댓값이 두 개 이상인 경우 그 중 한 곳의 위치를 출력한다.

row = 0
col = 0
num_list = []

for i in range(9):
    num_list.append(list(map(int, input().split())))

max = num_list[row][col]
for i in range(9):
    for j in range(9):
        if (max<num_list[i][j]):
            max = num_list[i][j]
            row = i
            col = j
print(max)
print(row+1, col+1)
