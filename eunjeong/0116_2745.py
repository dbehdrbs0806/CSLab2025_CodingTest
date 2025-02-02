# 문제 설명:
# 문제 링크: https://www.acmicpc.net/problem/2745
# B진법 수 N이 주어진다. 이 수를 10진법으로 변환하는 프로그램을 작성하시오.

# B진법:
# - B진법은 2 이상 36 이하의 진법이다.
# - 10진법을 넘어가는 자리수는 알파벳 대문자를 사용하여 표현한다.
#   예: A는 10, B는 11, ..., F는 15, ..., Y는 34, Z는 35를 의미한다.

# 입력:
# - 첫째 줄에 B진법 수 N과 진법 B가 공백으로 구분되어 주어진다. (2 ≤ B ≤ 36)

# 출력:
# - N을 10진법으로 변환한 값을 출력한다.

num, index = input().split()
num_Index = int(index) ** (len(num)-1)
total = 0
for i in num:
    if ord(i)>=65:
        total += num_Index * (ord(i)-55)
    else:
        total += num_Index * int(i)
    num_Index /= int(index)
    
print(int(total))