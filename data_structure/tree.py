#Tree
#주요 용도: 데이터 검색(탐색)
#장점: 탐색 속도를 개선할수 있음
#단점:평균 시간 복잡도는  𝑂(𝑙𝑜𝑔𝑛)이지만 트리가 균형잡혀 있을 때의 평균 시간복잡도이며 균형잡혀있지 않은 경우 리스트등과 동일한 성능을 보여줌 (  𝑂(𝑛)  )


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

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
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

    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False


    #삭제할 노드가 1. 없을때 2. 하나있을때 3. 두개있을때로 나누어서 생각

    #0. 삭제할 Node 탐색
    def delete(self, value):
        # 삭제할 노드 탐색
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            # 만약 같으면
            if self.current_node.value == value:
                searched = True
                break
            # 만약 크면
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            # 같거나 작으면
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if searched == False:
            return False


        #1. 하기 자손이 없을때(leaf node, terminal node)
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None

        #2. 하기 자손이 한개 있을때

        elif self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        #3.자식 2개 다 있을때
        elif self.current_node.left != None and self.current_node.right != None:
            #3-1. 삭제할 Node의 오른쪽 자식 중, 가장 작은 값(가장 왼쪽 아래값)을 삭제할 Node의 Parent Node가 가리키도록 한다
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.change_node.left

            #3-2. 삭제할 Node의 왼쪽 자식 중, 가장 큰 값을(가장 오른쪽 아래값) 삭제할 Node의 Parent Node가 가리키도록 한다.
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.right = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left

        return True

#test
# 0 ~ 999 숫자 중에서 임의로 100개를 추출해서, 이진 탐색 트리에 입력, 검색, 삭제
import random

# 0 ~ 999 중, 100 개의 숫자 랜덤 선택
bst_nums = set()
while len(bst_nums) != 100:
    bst_nums.add(random.randint(0, 999))
# print (bst_nums)

# 선택된 100개의 숫자를 이진 탐색 트리에 입력, 임의로 루트노드는 500을 넣기로 함
head = Node(500)
binary_tree = NodeMgmt(head)
for num in bst_nums:
    binary_tree.insert(num)

# 입력한 100개의 숫자 검색 (검색 기능 확인)
for num in bst_nums:
    if binary_tree.search(num) == False:
        print('search failed', num)

# 입력한 100개의 숫자 중 10개의 숫자를 랜덤 선택
delete_nums = set()
bst_nums = list(bst_nums)
while len(delete_nums) != 10:
    delete_nums.add(bst_nums[random.randint(0, 99)])

# 선택한 10개의 숫자를 삭제 (삭제 기능 확인)
for del_num in delete_nums:
    if binary_tree.delete(del_num) == False:
        print('delete failed', del_num)