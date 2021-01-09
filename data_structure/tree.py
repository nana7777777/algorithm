#Tree
#주요 용도: 데이터 검색(탐색)
#장점: 탐색 속도를 개선할수 있음
#단점:


###연습: 이진트리 구현해보기

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


# 1. 현재 노드가 가치보다 클때 오른쪽으로가
        #만약 노드가 있다면
            #그 노드가 value 보다 작다면 self.a = self.a.left
            #그 노드가 value 보다 크다면 self.a.left=value 후 break
        #만약 노드가 없다면 self.a.right=value
# 1. 현재 노드가 가치보다 크지 않을때 왼쪽
class NodeMgmt:
    def __init__(self,head):
        self.head = head

class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True: #있으면 다시하고 없으면 넣어라
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

#test
head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)