# 문제 설명

# 명령은 총 다섯 가지이다.
#   1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
#   2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
#   3: 스택에 들어있는 정수의 개수를 출력한다.
#   4: 스택이 비어있으면 1, 아니면 0을 출력한다.
#   5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.

import sys
input = sys.stdin.readline
output = sys.stdout.write

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return -1
    
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return 1 if not self.stack else 0
    
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1

# 스택 객체
stack = Stack()

# 입력
n = int(input().strip())
results = []

for _ in range(n):
    command = input().strip()
    if command.startswith('1'):
        _, x = command.split()
        stack.push(int(x))
    elif command == '2':
        results.append(f"{stack.pop()}\n")
    elif command == '3':
        results.append(f"{stack.size()}\n")
    elif command == '4':
        results.append(f"{stack.is_empty()}\n")
    elif command == '5':
        results.append(f"{stack.top()}\n")

# 출력 처리
output(''.join(results))

# 자꾸 타임 에러가 뜬 이유:
# 다량의 수를 처리할 때에는 input이 아니라 sys.stdin.readLine과
# sys.stdout.write를 통해 데이터를 처리해야 느리지 않다.
# 
# print문을 여러번 호출 시, 느려질 수 있기 때문이다.