#연결 리스트
#기본구조: 데이터와 연결할 다음 데이터의 주소를 가지고 있음 - 노드:데이터 저장 단위(데이터, 포인터로 구성)
#장점 : 미리 공간을 만들지 않아도 됨
#단점 : 연결정보를 위한 별도 데이터 공간 필요, 연결정보찾는데 시간걸림, 삭제 및 추가 번거로움


####연습1: linked list 구성해보기

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

node1 = Node(1)
head = node1
for index in range(2, 5):
    add(index)

node = head #head는 node 변수에 담아두어야 함. head 자체가 다 안고있는게 아니라서
while node.next:
    print("이것",node.next)
    print(node.data)
    node = node.next
print ("last:",node.data)


#### 연습2 : 중간에 끼워넣기

node2=Node(2.5)

node=head
while node.data != 2:
    node=node.next
node_next = node.next #node.next를 node_next라는 변수에 담아두고
node.next = node2 #대체한후
node2.next=node_next #다시연결

node=head
while node.next:
    print(node.data)
    node = node.next
print ("last:",node.data)


### 연습3. 특정 노드를 찾는 함수를 만들고 테스트 하기

class Node:
    def __init__(self, data,next=None):
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data): #가장 첫 노드
        self.head = Node(data)

    def add(self, data): #더하기 - 맨 마지막으로 가서 더함
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self): #다음 노드로 가기
        node = self.head
        while node:
            node = node.next

    def delete(self, data): #삭제노드
        #가장 첫번째 노드 없애는 경우
        #중간 노드 없애는 경우
        #마지막 노드 없애는 방법
        if self.head =='':
            print('값 없음')
            return
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                else:
                    node=node.next



    def search_node(self, data): #그 노드 찾기
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next


#테스트
node_mgmt = NodeMgmt(0)
for data in range(1, 5):
    node_mgmt.add(data)

node = node_mgmt.search_node(4)
print (node.data)