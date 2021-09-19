# -*- coding: utf-8 -*-
"""
Stack
1) 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
2) 스택에 저장된 자료는 선형구조를 가짐
선형구조: 자로 간의 관계가 1대 1의 관계를 가짐
비선형구조: 자료 간의 관계가 1대 N의 관계를 가짐(예: 트리)
3) 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있음
4) 마지막에 삽입한 자료를 가장 먼저 꺼냄
5) 후입선출(LIFO, Last-In-First-Out)이라고 부름

자료구조
자료를 선형으로 저장할 저장소가 필요
C언어에서는 배열을 사용할 수 있음
파이썬에서는 리스트를 사용할 수 있음
저장소 자체를 스택이라 부르기도 함
스택에서 마지막 삽입된 원소의 위치를 Top이라고 부름

연산
삽입: 저장소에 자료를 저장하고 보통 push라고 부름
삭제: 저장소에서 자료를 꺼냄
      꺼낸 자료는 삽입한 자료의 역순으로 꺼냄 보통 pop이라고 부름
isEmpty: 스택이 공백인지 아닌지를 확인하는 연산
peek: 스택의 top에 있는 item(원소)을 반환하는 연산

스택의 삽입/삭제 연산 과정
빈 스택에 원소 A, B, C를 차례로 삽입 후 한 번 삭제하는 연산 과정

push 알고리즘
def push(item):
    s.append(item)
    
pop 알고리즘
def pop():
    if len(s) == 0:
        # underflow
        return
    else:
        return s.pop(-1)
    

구현하기
1. 스택 구현하기
2. 구현한 스택을 이용하여 3개의 데이터를 스택에 저장하고
   다시 3번 꺼내서 출력하기
def push(item):
    s.append(item)
    
def pop():
    if len(s) == 0:
        print("Stack is Empty!!") #underflow
        return
    else:
        return s.pop(-1)

s = []
push(1)
push(2)
push(3)
print("pop item =>", pop())
print("pop item =>", pop())
print("pop item =>", pop())


스택 구현 고려사항
* 리스트를 사용하여 스택을 구현하는 경우
장점: 구현이 용이하다
단점: 리스트의 크기를 변경하는 작업은 내부적으로
      큰 overhead 발생 작업으로 많은 시간이 소요된다.

해결방법
* 리스트의 크기가 변동되지 않도록 배열처럼 크기를 미리 정해놓고 사용하는 방법
* 동적 연결리스트를 이용하여 저장소를 동적으로 할당하여 스택을 구현하는 방법
장점: 구현이 용이하다
단점: 리스트로 구현하는 것보다 구현이 복잡하다.
"""



























