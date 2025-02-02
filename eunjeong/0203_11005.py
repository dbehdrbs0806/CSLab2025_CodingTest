# 문제 설명
# 문제 링크: https://www.acmicpc.net/problem/11005

# 10진수 n이 주어질 때, 이를 B진법으로 바꾸어 출력

num, index = map(int, input().split())
num_list = []
last= num

while last>=index:
    num_list.append(last % index)
    last = int(last / index)
num_list.append(last)

num_list.reverse()
for i in num_list:
    if i>=10:
        print(chr(i+55),end='')
    else:
        print(i,end='')