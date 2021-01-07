#Queue
#가장 대표적 특징 :FIFO(first in first out), LILO(last in last out)
#이외 변형된 aue 대표적 2가지: LifoQueue(last in first out), PriorityQueue(우선순위 지정)
#queue는 어디에 많이 쓰이나? 프로세스 스케줄링에 많이 사용(프로세스 스케줄링: cpu를 사용하는데 우선순위를 관리하는것)

#연습: 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현해보기

queue_list = list()

def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

for index in range(10):
    enqueue(index)

len(queue_list)

print(dequeue())