#Hash Table
#키에 대한 데이터 값을 주소로 가지고 있는 구조
#장점: 키를 통해 데이터를 바로 받아올수 있어 저장, 읽기 속도 빠름
#단점: 여러 키에 대한 주소값이 동일한 경우를 위해 별도 자료구조 필요


###연습: 리스트 변수로 hash 구현해보기
#1. 해쉬 함수: key % 8
#2. 해쉬 키 생성: hash(data)

hash_table = list([0 for i in range(8)])

def get_key(data): #해쉬 키 생성
    return hash(data)

def hash_function(key): #해쉬 함수 수치에 맞게 구현
    return key % 8

def save_data(data, value): #해쉬 주소에 데이터 저장
    hash_address=hash_function(get_key(data))
    hash_table[hash_address]=value

def read_data(data): #키에 대한 데이터 읽기
    hash_address=hash_function(get_key(data))
    return hash_table[hash_address]

#test
# save_data('Dave', '0102030200')
# save_data('Andy', '01033232200')
# print(read_data('Dave'))


### 연습2: 해쉬 충돌(collision) 해결 알고리즘 구현하기
#1. 해쉬 함수: key % 8
#2. 해쉬 키 생성: hash(data)

hash_table = list([0 for i in range(8)])

def get_key(data): #해쉬 키 생성
    return hash(data)

def hash_function(key): #해쉬 함수 수치에 맞게 구현
    return key % 8

#여기 수정
def save_data(data, value): #해쉬 주소에 데이터 저장
    index_key=get_key(data)
    hash_address=hash_function(index_key)
    if hash_table[hash_address] != 0:
        hash_table[hash_address].append([[index_key,value]])
    else:
        hash_table[hash_address]=[[index_key,value]]

#여기 수정
def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None

#test
save_data('Dd111', '1201023010')
save_data('Datta', '3301023010')
read_data('Datta')