"""
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오
"""

def fac(value):
    if value<=1:
        return 1
    else:
        return fac(value-1)*value

print(fac(int(input())))