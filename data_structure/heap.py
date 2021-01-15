#Hip
#데이터의 최소값과 최대값을 빠르게 찾기위한 완전탐색트리
#이진탐색트리와 완전탐색트리의 차이점
#이진탐색트리 : 1. 왼쪽자식노드가 오른쪽 자식노드보다 작음, 2. 탐색을 위한 구조
#완전탐색트리 : 1. 왼쪽자식노드가 오른쪽 자식노드보다 작을수도 클수도 있음음 2. 최대, 최소값 검색을 위한 구조

class Heap:
    def __init__(self,data):
        self.heap_array=list()
        self.heap_array.append(None) #index를 1로 하기위해 가장 처음 None으로 놓음
        self.heap_array.append(data)

    def insert(self, data):
        self.heap_array.append(data) #append로 이용하는 이유는 완전 이진트리 성질과 같기 때문 (append 를 사용하면 맨 뒤에 넣어주는 성질)
        return True

print(Heap(10).insert(2))


###heap 삭제