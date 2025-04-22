"""
문제
문자열 S의 접두사란 S의 가장 앞에서부터 부분 문자열을 의미한다. 예를 들어, S = "codeplus"의 접두사는 "code", "co", "codepl", "codeplus"가 있고, "plus", "s", "cude", "crud"는 접두사가 아니다.

총 N개의 문자열로 이루어진 집합 S가 주어진다.

입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 문자열 중 적어도 하나의 접두사인 것의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다.

다음 N개의 줄에는 집합 S에 포함되어 있는 문자열이 주어진다.

다음 M개의 줄에는 검사해야 하는 문자열이 주어진다.

입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다. 집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.

5 10
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
star
start
code
sunday
coding
cod
online
judge
plus

출력
첫째 줄에 M개의 문자열 중에 총 몇 개가 포함되어 있는 문자열 중 적어도 하나의 접두사인지 출력한다.

7


# from queue import PriorityQueue

# input_num = list(map(int, input().split()))
# word_list = [input() for _ in range(input_num[0])] # ['baekjoononlinejudge', 'startlink', 'codeplus', 'sundaycoding', 'codingsh'] 확인
# prefix_list = [input() for _ in range(input_num[1])] # ['baekjoon', 'star', 'start', 'code', 'sunday', 'coding', 'cod', 'online', 'judge', 'plus'] 확인
# # 원하는 output que = ['baekjoon', 'online', 'star', 'code', 'sunday', 'cod', 'coding']
# # que.qsize = 7


# que = PriorityQueue()
# result = []

# for word in word_list:
#     for prefix in prefix_list:
#         if word in prefix:
#             que.put(word)


# print(que.qsize())

# a = ['baekjoononlinejudge']
# sample_list = ['baekjoon', 'star', 'start', 'code', 'sunday', 'coding', 'cod', 'online', 'judge', 'plus']
# prefix_list = []

# for i in sample_list:
#     if a[0] == i:
#         continue
#     elif i in a[0]:
#         a= a[0].split(i)
#         prefix_list.append(i)
#         a.remove("")
#         print(a)

# print(prefix_list)

# word_list = ['baekjoononlinejudge', 'startlink', 'codeplus', 'sundaycoding', 'codingsh']
# prefix_list = ['baekjoon', 'star', 'start', 'code', 'sunday', 'coding', 'cod', 'online', 'judge', 'plus']
# result = []

# for word in word_list:
#     for prefix in prefix_list:
#         if word == prefix:
#             continue
#         elif word.startswith(prefix):
#             result.append(prefix)
#             word = word.replace(prefix, "")

# print(result)
"""

import sys

input = sys.stdin.readline

input_num = list(map(int, input().split()))
word_list = [input() for _ in range(input_num[0])] # ['baekjoononlinejudge', 'startlink', 'codeplus', 'sundaycoding', 'codingsh'] 확인
prefix_list = [input() for _ in range(input_num[1])] # ['baekjoon', 'star', 'start', 'code', 'sunday', 'coding', 'cod', 'online', 'judge', 'plus'] 확인
result = []

for word in word_list:
    for prefix in prefix_list:
        if word == prefix:
            continue
        elif word.startswith(prefix):
            result.append(prefix)
            word = word.replace(prefix, "")

print(len(result))
