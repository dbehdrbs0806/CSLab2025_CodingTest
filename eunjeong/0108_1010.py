"""
서쪽의 사이트와 동쪽의 사이트를 다리로 연결하려고 한다.
(이때 한 사이트에는 최대 한 개의 다리만 연결될 수 있다.)
재원이는 다리를 최대한 많이 지으려고 하기 때문에 서쪽의 사이트 개수만큼 (N개) 다리를 지으려고 한다.
다리끼리는 서로 겹쳐질 수 없다고 할 때 다리를 지을 수 있는 경우의 수를 구하는 프로그램을 작성하라.
"""
count = int(input())
for i in range(count):
    K, N = map(int, input().split())

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
