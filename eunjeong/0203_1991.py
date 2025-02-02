# 문제 설명
# 문제 링크: https://www.acmicpc.net/problem/1991
# 전위, 중위, 후위 순회 결과 출력
'''
num = int(input())
num_list = [ False for _ in range(num*3+1)]
head_num = 1

for i in range(num):
    head, left, right = input().split()
    if i != 0:
        num_Index = num_list.index(head)
        num_list[num_Index]=head
        if left != '.':
            num_list[num_Index*2]=left
        if right != '.': 
            num_list[num_Index*2+1]=right

    else:
        num_list[head_num]=head
        if left != '.':
            num_list[head_num*2]=left
        if right != '.': 
            num_list[head_num*2+1]=right
            
    if head_num+1 ==False:
        head_num+=1


# 전위 순회
def Pre_Order(head_num):
    print(num_list[head_num], end='')
    if (head_num*2 < len(num_list) and num_list[head_num*2] != False):
        Pre_Order(head_num*2)
    if (head_num*2+1 < len(num_list) and num_list[head_num*2+1]!=False):
        Pre_Order(head_num*2+1)

# 중위 순회
def In_Order(head_num):
    if (head_num*2 < len(num_list) and num_list[head_num*2] != False):
        In_Order(head_num*2)
    print(num_list[head_num], end='')
    if (head_num*2+1 < len(num_list) and num_list[head_num*2+1]!=False):
        In_Order(head_num*2+1)

# 후위 순회
def Post_Order(head_num):
    if (head_num*2 < len(num_list) and num_list[head_num*2] != False):
        Post_Order(head_num*2)
    if (head_num*2+1 < len(num_list) and num_list[head_num*2+1]!=False):
        Post_Order(head_num*2+1)
    print(num_list[head_num], end='')




Pre_Order(1)
print()
In_Order(1)
print()
Post_Order(1)

'''
# 위 방식은 재귀 함수=> 시간 多 소비

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.nodes = {}
    
    def insert(self, head, left, right):
        if head not in self.nodes:
            self.nodes[head] = Node(head)
        
        if left != '.':
            self.nodes[left] = Node(left)
            self.nodes[head].left = self.nodes[left]
        
        if right != '.':
            self.nodes[right] = Node(right)
            self.nodes[head].right = self.nodes[right]

    def pre_order(self, node):
        if node:
            print(node.value, end='')
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.value, end='')
            self.in_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value, end='')

# 입력 및 트리 구성
num = int(input())
tree = BinaryTree()

for _ in range(num):
    head, left, right = input().split()
    tree.insert(head, left, right)

# 순회 결과 출력
root = tree.nodes['A']

tree.pre_order(root)
print()
tree.in_order(root)
print()
tree.post_order(root)

# 클래스 내에서 재귀 함수 사용 시 시간 매우 단축 가능