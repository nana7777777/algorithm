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

class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True: #현재노드값이 들어온값보다 크면 왼쪽만 보고 판단 / 작으면 오른쪽만 판단
            if value < self.current_node.value: #만약 현재 노드값이 들어온값보다 크면
                if self.current_node.left != None: #만약 현재노드의 왼쪽자식값이 있으면
                    self.current_node = self.current_node.left #현재노드의 왼쪽 자식값을 현재 노드로 보고 다시 반복
                else: #만약 현재노드의 왼쪽자식값이 없으면
                    self.current_node.left = Node(value) #들어온 값을 현재노드의 왼쪽값으로 놓고 끝내라
                    break
            else:                               #만약 현재 노드값이 들어온값보다 크지 않으면
                if self.current_node.right != None: #만약 현재
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

#test
# head = Node(1)
# BST = NodeMgmt(head)
# BST.insert(2)


###연습2: 이진트리탐색 구현해보기

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True: #현재노드값이 들어온값보다 크면 왼쪽만 보고 판단 / 작으면 오른쪽만 판단
            if value < self.current_node.value: #만약 현재 노드값이 들어온값보다 크면
                if self.current_node.left != None: #만약 현재노드의 왼쪽자식값이 있으면
                    self.current_node = self.current_node.left #현재노드의 왼쪽 자식값을 현재 노드로 보고 다시 반복
                else: #만약 현재노드의 왼쪽자식값이 없으면
                    self.current_node.left = Node(value) #들어온 값을 현재노드의 왼쪽값으로 놓고 끝내라
                    break
            else:                               #만약 현재 노드값이 들어온값보다 크지 않으면
                if self.current_node.right != None: #만약 현재
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self,value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif self.current_node.value > value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

#test
# head = Node(1)
# BST = NodeMgmt(head)
# BST.insert(2)
# BST.insert(3)
# BST.insert(0)
# BST.insert(4)
# BST.insert(8)
# print(BST.search(2))
# print(BST.search(-1))

###연습3: 이진트리탐색 삭제 구현해보기

#삭제할 노드가 1. 없을때 2. 하나있을때 3. 두개있을때로 나누어서 생각

#1.
#2.
#3-1. 삭제할 Node의 오른쪽 자식 중, 가장 작은 값(가장 왼쪽 아래값)을 삭제할 Node의 Parent Node가 가리키도록 한다
#3-2. 삭제할 Node의 왼쪽 자식 중, 가장 큰 값을(가장 오른쪽 아래값) 삭제할 Node의 Parent Node가 가리키도록 한다.