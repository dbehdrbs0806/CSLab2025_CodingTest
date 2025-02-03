# 문제 요약
# 문제 링크:https://www.acmicpc.net/problem/5086
# 두 수가 주어졌을 때, 다음 3가지 중 어떤 관계인지 구하는 프로그램을 작성하시오.

#   1. 첫 번째 숫자가 두 번째 숫자의 약수이다.
#   2. 첫 번째 숫자가 두 번째 숫자의 배수이다.
#   3.첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.

case = ['factor','multiple','neither']

while True:
    num1, num2 = map(int, input().split())
    if (num1==num2==0):
        break
    if(num2>num1 and num2%num1 == 0):
        print(case[0])
    elif (num1>num2 and num1%num2 == 0):
        print(case[1])
    else:
        print(case[2])
