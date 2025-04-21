"""
문제
후위 표기식과 각 피연산자에 대응하는 값들이 주어져 있을 때, 그 식을 계산하는 프로그램을 작성하시오.

입력
첫째 줄에 피연산자의 개수(1 ≤ N ≤ 26) 가 주어진다. 그리고 둘째 줄에는 후위 표기식이 주어진다. (여기서 피연산자는 A~Z의 영대문자이며, A부터 순서대로 N개의 영대문자만이 사용되며, 길이는 100을 넘지 않는다) 그리고 셋째 줄부터 N+2번째 줄까지는 각 피연산자에 대응하는 값이 주어진다. 3번째 줄에는 A에 해당하는 값, 4번째 줄에는 B에 해당하는값 , 5번째 줄에는 C ...이 주어진다, 그리고 피연산자에 대응 하는 값은 100보다 작거나 같은 자연수이다.

5
ABC*+DE/-
1
2
3
4
5

후위 표기식을 앞에서부터 계산했을 때, 식의 결과와 중간 결과가 -20억보다 크거나 같고, 20억보다 작거나 같은 입력만 주어진다.

6.20

출력
계산 결과를 소숫점 둘째 자리까지 출력한다.
"""

import sys
import re
import operator # 사칙연산자
input = sys.stdin.readline


input_num = int(input())
input_expr = list(input().strip())
stack = []

for i in input_expr:
    if i in r'[A-Z]':
        input_expr = input_expr.replace(i, input().strip()) # 변수를 숫자로 교체
    if input_expr.count(i) > 1:
        break

print(input_expr)

# 사칙연산 operator 모듈
ops_dict = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

# while len(input_expr) > 1: # input_expr의 길이가 1이상인 동안
#     for idx, i in enumerate(input_expr): # input_expr의 인덱스와 요소
#         if i in ["+","-","*","/"]: # i가 사칙연산자인 경우
#             calc = ops_dict[i](float(input_expr[idx-2]), float(input_expr[idx-1])) # input_expr[idx-2]과 input_expr[idx-1] 사칙연산
#             del input_expr[idx-2:idx+1] # 계산에 들어간 요소를 input_expr에서 제거
#             input_expr.insert(idx-2, calc) # 계산된 결과를 input_expr에 삽입

# for i in input_expr:
#     if i in ops_dict:
#         next = stack.pop()
#         prev = stack.pop()
#         stack.append(ops_dict[i](prev, next))
#     else:
#         stack.append(float(i))


# print(stack[0]) # 최종 결과
