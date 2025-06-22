#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys


#LIFO(Last In First Out) => 벌집통을 위로 차곡차곡 쌓는 모양
#push & pop / stack.pop (stack[-1])
#List 이용, 굳이 linkedlist 사용할 필요가 없음

stack = []
#push O(1)
stack.append(1)  # [1]
stack.append(2)  # [1, 2]
stack.append(3)  # [1, 2, 3]
stack.append(4)  # [1, 2, 3, 4]

#pop  => O(1)
# stack.pop()  # output: 4 / stack = [1, 2, 3]
# print(stack)
# print(stack[-1])

# stack.pop()  # output: 3 / [1, 2]
# print(stack)
# print(stack[-1])

# stack.pop()  # output: 2 / [1]
# print(stack)
# print(stack[-1])

# stack.top (세로로 표현하는게 더 이해하기 쉬움, 프링글스!)
print(stack[-1]) #top [4]

while stack:
    print(stack[-1])
    print(stack.pop())
    print(stack)
    