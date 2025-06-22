#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
#running time 실행시간. : 실행된 코드의 실제 실행 시간을 의미
#시간 복잡도: 입력크기에 따라 알고리즘의 실행 시간이 어떻게 증가하는지를 나타낸다.
# 사람 수가 많을수록 실행 시간이 중요해진다
#실행시간을 n에 대한 함수로 나타내면 이를 시간복잡도라 함.
#입력값이 컸을 때 어떻게 예측? - 계산이 필요. 직접 재는 건 의미가 없다.
#설계하는 과정에서 사람 수가 많을 때도 통과할 수 있도록 알고리즘을 짜야함
#빅오 노테이션을 사용
# 상수항 O(1) = 빅오 원
# average, worst, best time
# input size & 데이터의 형식(순서 배열 등)에 의해서도 시간 복잡도에서 차이가 남
 

import timeit

def test_code():
    sum = 0
    for i in range(1000000):
        sum += i


run_time = timeit.timeit(test_code, number=10)/10 #average time

print(run_time)


#list는 c언어의 array에서 파생된 것임
#배열: 고정된 저장공간(static) -> 유연성있게 조정(dynamic), 순차적 데이터 저장
#python의 list는 dynamic array임.

#순차적 데이터 저장의 장점
# Static Array
# - Random Access(direct access) (O(1)) (알고리즘 사용시에 자료구조를 알고, 어떻게 동작하는지 알아야 자료구조를 풍부하고 이용가능)
#메모리 상에서 순서대로 저장 -> 갖다 써야 함 eg) arr[2] -> 주소 -> 값 가지고 옴
#array -> 가장 첫번째 배열의 주솟값을 가지고 있음, 시작점과 끝 주소값을 앎.
#데이터 접근 위해 주솟값 필요 = arr의 첫번째 주솟값 + idx * 4byte(int) (즉시 계산이 가능 O(1))

# - 한계: 선언 시 정한 size보다 더 많은 데이터를 저장해야하는 경우,
#메모리 공간이 없어 문제가 발생.
#매번 큰 배열을 선언하면 메모리 비효율이 발생.
#그것보다 큰 배열이 들어올 수도 있을 문제점


# Dynamic Array: 배열의 크기를 resizing
#기존 할당 사이즈를 초과하면, size를 일반적으로 2배 늘린 배열을 다시 선언(doubling) 
#(이 때 O(n))
# - 사용법: 파이썬 List
# -- 파이썬도 결국 c언어로 작성되어있음. 정적리스트를 쓰기쉽게 동적리스트(list)로 만들어놓음

# - 연산 & 시간복잡도
# 선언 및 초기화 - O(n)
# 접근 - O(1) => (정적arr random access) arr의 첫번째 주솟값 + idx * 4byte(int)
# 데이터 추가(append) - O(1)
##  resizing(doubling) - O(n) ##
### 데이터 추가 시, worse case O(n), average case O(1), best case O(1)
### -> append는 O(1)이라 생각하면 됨!
# 마지막 데이터 삭제 - O(1)
# 중간 데이터 추가 - O(n) #하나씩 다 밀어야해서
# 중간 데이터 삭제 - O(n) (순차적이어야 random access 가능하므로)




#Linked List: node라는 구조체가 연결되는 형식으로 데이터를 저장하는 자료구조
# 데이터 값 + next node 주솟값
# 비연속적으로 저장. next node 덕분에 논리적으로는 연속적
# - 장점: 메모리 상에서 사용이 좀 더 자유로움
# - 단점: 주소값도 저장해야해서 데이터 하나 당 차지하는 메모리가 더 큼
# - 직접 구현할 필요가 없다
# 장점 - 앞뒤 데이터 **수정** 많은 경우 linked list가 효율적
# 단점 - 하지만 데이터 **접근** 은 O(n)임


#클래스로 node 구현
class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):    
        self.head = None    #head: 리스트의 첫 번째 노드를 가리키는 포인터변수
                            #처음엔 head가 0000을 가리킴

    def append(self, value):
        new_node = Node(value) #new_node(1, 00000)가 왔을 때 

        if self.head is None:       #head가 아직 아무것도 가리키고 있지 않을 때
            self.head = new_node    #head가 new_node를 가리키도록
                                    
        else:
            current = self.head     #current: head가 가리키는 node
            while(current.next):    #head에서 주소값 타고 이동해서 다음 node = current node
                                        #current.next = None일때까지 즉, next 주솟값이 지정되지 않은 노드까지 이동
                current = current.next
            current.next = new_node     #다음 노드의 주솟값이 지정되어있지 않은 노드에 next 주소값 연결

first = Node(1)
second = Node(2)
third = Node(3)

first.next = second #first의 다음 노드는 second node 주솟값
second.next = third #second의 다음 노드는 third node 주솟값
first.value = 6 #update

print(first.next)
print(second.next)


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)


#리스트 구현
list_ = [1,3,6,7]
len(list_)
list_[3] #O(1)
list_.append(100) #O(1)
list_.insert(2, 20) #index2에 20 추가 # O(n)

for v in list_:
    print(v)     #O(n)

len_ = len(list_)
for i in range(list_): #for i in range(len_):
    print(i, list_[i])

for idx, v in enumerate(list_):
    print(idx, v)

list_.sort() #O(nlogn) 퀵정렬 직접 구현할 필요x
list_.sort(reverse = True)


#LinkedList
from collections import deque
#덱은 앞으로 뒤로 모두 연결되어있어, appendleft가능 head만 옮겨주면 됨. O(1)
#list의 insert가 O(n)이라면, ll은 appendleft가 O(1)
#append, appendleft, pop, popleft = O(1)
# 장점 - 앞뒤 데이터 수정 많은 경우 linked list가 효율적
# 단점 - 하지만 데이터 접근은 O(n)임

ll_ = deque() #덱 자료구조를 사용
print(ll_)
ll_.append(1)
ll_.append(10)
ll_.append(7)  
ll_.appendleft(8)  #head를 앞으로 이동

ll_.pop() #tail을 앞 주솟값으로 포인팅
ll_.popleft() #head가 뒤로 이동

ll_[3] #접근 - random access 불가. head로부터 주소를 3번 넘어가야함.


#queue -> 응용이 더 중요!
#선입선출

#enqueue - 큐의 맨 뒤에 데이터 넣는 것
#dequeue - 큐의 맨 앞의 데이터를 빼는 것

#리스트를 큐로 -> .pop(0) => 뒤에 있는걸 하나하나 다 옮겨야 하므로 dequeue 시 O(n)
#리스트로 큐를 써도 되지만 디큐시 시간복잡도가 오래걸린다.


#linked list deque 사용
#append로 추가
#popleft로 front(head)가 다음 노드의 주소값으로 -> O(1)
## **deque(덱)** 를 많이 사용할 예정이므로 아래 코드 잘 알아두기!!

"""
from collections import deque
queue = deque() #비어있는 큐 생성 # []

#insert => O(1)
queue.append(1) # [1]
queue.append(4) # [1, 4]

#pop => O(1)
queue.popleft() #FIFO => #[4]



#queue가 빌 때까지 dequeue() 하기

print(queue)
while queue:
    queue.popleft()
    print(queue)
print(queue)
    

#활용 방법
## 그래프의 BFS -> 단독으로 큐가 나오는 경우는 별로 없음.
## 반대로, stack은 단독으로 나올 수 있음


"""


#Stack 자료구조
