"""
자연수 
\(N\)과 정수 
\(K\)가 주어졌을 때 이항 계수 
\(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.
"""

N, K = map(int, input().split())

def fac(value):
    if value<=1:
        return 1
    else:
        return fac(value-1)*value

value = 1
count = N
for i in range(K):
    value *= count
    count-=1

print(int(value/fac(K)))