# 문제 요약
# 문제 링크: https://www.acmicpc.net/problem/2720

# 거스름돈 C(센트)가 주어질 때, 최소 개수의 동전으로 나누어 출력하는 프로그램을 작성하시오.
# 
# [동전 단위]
# - 쿼터(Quarter) : $0.25 (25센트)
# - 다임(Dime)    : $0.10 (10센트)
# - 니켈(Nickel)  : $0.05 (5센트)
# - 페니(Penny)   : $0.01 (1센트)
# 
# [입력]
# - 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# - 각 테스트 케이스마다 거스름돈 C(1 ≤ C ≤ 500, 단위: 센트)가 주어진다.
# 
# [출력]
# - 각 테스트 케이스마다 필요한 동전 개수를 공백으로 구분하여 출력한다.
#   (순서: 쿼터 개수, 다임 개수, 니켈 개수, 페니 개수)

num = int(input())
coin_Kind=[25,10,5,1]

for i in range(num):
    coin_List=[]
    value = int(input())
    for j in coin_Kind:
        coin_List.append(int(value / j))
        value = value % j
    for j in coin_List:
        print(j, end=' ')