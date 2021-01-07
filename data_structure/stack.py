#Stack
#LIFO, FILO
#장점: 단순한 구조이기 때문에 데이터 저장, 읽기 속도 빠름(push, pop을 이용해 빠르게 처리 가능)
#단점: 미리 공간을 지정해주어야 하기 때문에 저장공간에 대한 낭비가 있을수 있음(사용가능한 공간이 한정되어 있음)



#연습: 리스트 변수로 스택을 다루는 pop, push 기능 구현해보기

stack_list = list()

def push(data):
    stack_list.append(data)

def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data

for index in range(10):
    push(index)

print(pop())