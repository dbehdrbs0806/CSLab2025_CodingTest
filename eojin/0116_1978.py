"""
Baekjoon #1978 소수 찾기
- 알고리즘: 수학/정수론/소수 판정

- 문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

- 입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
4
1 3 5 7

- 출력
주어진 수들 중 소수의 개수를 출력한다.
3

- 오답노트
    - foreach문으로 배열의 원소를 탐색할 때 탐색중인 배열의 원소를 삭제하거나 추가하면 생각한 대로 안 움직일 수 있다,,, 이걸 생각을 못 하고 짜서 계속 오류남
        - 아마 python for문의 내부 구조랑 관련이 있지 않을까? 싶음
"""
n = int(input())
numlist = list(map(int, input().split()))
notpri = []

for i in numlist:
    if i == 1:
        notpri.append(i)
        continue
    for j in range(2, round(i/2)+1):
        if i%j==0:
            notpri.append(i)
            break

print(len(numlist)-len(notpri))