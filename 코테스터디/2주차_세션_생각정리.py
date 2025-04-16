"""
문제 설명
여러분은 n명의 엔지니어와 다음과 같은 정보를 갖고 있습니다:

speed[i]: i번째 엔지니어의 속도
efficiency[i]: i번째 엔지니어의 효율성

이제 여러분은 이들 중에서 최대 k명까지의 엔지니어를 선택해서 팀을 구성하려고 합니다.

🎯 팀의 성능(Performance)
팀의 성능은 아래와 같이 계산됩니다:

성능 = 선택한 모든 엔지니어들의 속도의 합 × 선택한 엔지니어들 중 가장 낮은 효율성
즉, 효율성이 낮은 사람이 팀 전체의 효율성을 끌어내리게 됩니다.

✅ 목표
최대 k명의 엔지니어를 선택해서 팀의 성능을 최대화 하세요.
단, 결과 값이 너무 클 수 있으니 10⁹ + 7로 나눈 나머지를 반환하세요.

📘 예시
예제 1

입력: 
n = 6, 
speed = [2,10,3,1,5,8], 
efficiency = [5,4,3,9,7,2], 
k = 2

출력: 60
2번 엔지니어: 속도 10, 효율 4

5번 엔지니어: 속도 5, 효율 7
→ 둘을 선택하면, 성능 = (10 + 5) × min(4, 7) = 15 × 4 = 60

예제 2

k = 3일 경우 출력: 68
1, 2, 5번 엔지니어 선택 → 속도 합: 2+10+5=17, 최소 효율: 4 → 성능: 17×4=68

예제 3

k = 4일 경우 출력: 72
1, 3, 5, 2번 엔지니어 선택 → 속도 합: 2+3+5+10=20, 최소 효율: 3 → 성능: 20×3=60 (더 나은 조합은 있음)

⛓️ 제약 조건
1 ≤ k ≤ n ≤ 100,000

speed와 efficiency의 길이는 n

1 ≤ speed[i] ≤ 100,000
1 ≤ efficiency[i] ≤ 1,000,000,000

슈도코드
n = 6, 
speed = [2,10,3,1,5,8], 
efficiency = [5,4,3,9,7,2], 
k = 2

---
import sys

input = sys.stdin.readline

num_int = int(input("총 엔지니어 수를 입력하세요 : "))
speed = [int(v) for v in list(map(int, input("속도를 입력하세요 : ").split()))[:num_int]] if num_int > 0 else print(ValueError)
efficiency = [int(v) for v in list(map(int, input("효율성을 입력하세요 : ").split()))[:num_int]] if num_int > 0 else print(ValueError)
k = int(input("선택할 엔지니어 수를 입력하세요 : ")) if num_int > 0 or k > num_int else print(ValueError)
assert 0 < k <= num_int, "선택할 엔지니어 수는 1 이상, 전체 수 이하로 입력해야 합니다."
---

import sys

input = sys.stdin.readline

# 총 엔지니어 수 입력
print("총 엔지니어 수를 입력하세요 : ", end="", flush=True)
num_int = int(input())
assert num_int > 0, "엔지니어 수는 1 이상이어야 합니다."

# 속도 입력
print("속도를 입력하세요: ", end="", flush=True)
speed_input = list(map(int, input().split()))
assert len(speed_input) >= num_int, "입력된 속도 수가 부족합니다."
speed = speed_input[:num_int]

# 효율성 입력
print("효율성을 입력하세요: ", end="", flush=True)
eff_input = list(map(int, input().split()))
assert len(eff_input) >= num_int, "입력된 효율성 수가 부족합니다."
efficiency = eff_input[:num_int]

# 길이 확인
assert len(speed) == len(efficiency), "속도와 효율성의 수가 일치하지 않습니다."

# 선택할 엔지니어 수 입력
print("선택할 엔지니어 수를 입력하세요 : ", end="", flush=True)
k = int(input())
assert 0 < k <= num_int, "선택할 엔지니어 수는 1 이상, 전체 수 이하여야 합니다."

"""

result = 0

n = 6, 
speed = [2,10,3,1,5,8],# k명 고르고 더하기 / 이거 튜플이야...
efficiency = [5,4,3,9,7,2],# k명 중 최소값 곱하기 / 이거 튜플이야...
k = 2
# k 명의 팀이 최대 효율을 내기 위해서는 speed 합계가 높고 팀의 efficiency 최소값이 높아야 함.
# for i in speed[0]: # [0] 이 표현을 통해서 튜플 자물쇠를 풀 수 있음.
#     for j in speed[0]:
#         if j != i: # j가 i와 다르면
#             for k in speed[0]:
#                 if k != i and k != j: # k가 i와 j와 다르면
#                     print(i+j+k) # 더해라

max_speed_list = []
max_eff_list = []
max_value = 0

# for i, x in zip(speed[0], efficiency[0]): # [0] 이 표현을 통해서 튜플 자물쇠를 풀 수 있음.
#     for j, y in zip(speed[0], efficiency[0]):
#         if j != i: # j가 i와 다르면
#             for k, z in zip(speed[0], efficiency[0]):
#                 if k != i and k != j: # k가 i와 j와 다르면
#                     print("[",i,j,k,"]=",i+j+k, "[", x, y, z,"]=", min(x,y,z), "->", (i+j+k) * min(x,y,z)) # 더해라
# 뭔가 이제 최대값을 result에 기록하고 최대값이 나오는 i,j,k와 x,y,z를 출력하면 될거 같은데?

for i, x in zip(speed[0], efficiency[0]): # [0] 이 표현을 통해서 튜플 자물쇠를 풀 수 있음.
    for j, y in zip(speed[0], efficiency[0]):
        if j != i: # j가 i와 다르면
            for k, z in zip(speed[0], efficiency[0]):
                if k != i and k != j: # k가 i와 j와 다르면
                    if (i+j+k) * min(x,y,z) >= max_value:
                        max_speed_list = [i,j,k]
                        max_eff_list = [x,y,z]
                        max_value = (i+j+k) * min(x,y,z)

print(max_speed_list, max_eff_list, max_value)

# result / (10**9 + 7)

1. 빈 리스트 두 개를 생성:
     comb_speed_list ← 빈 리스트
     comb_effi_list  ← 빈 리스트

2. 함수 nCr(리스트, r)을 정의:
     - 입력된 리스트의 원소들 중에서 r개를 선택하는 모든 조합을 리스트 형태로 반환.

3. 두 개의 리스트를 정의:
     speed      ← [2, 10, 3, 1, 5, 8]
     efficiency ← [5, 4, 3, 9, 7, 2]

4. 0부터 speed 리스트의 길이까지 (즉, 0개부터 6개까지) 반복:
     a. speed 리스트에서 i개씩 뽑은 모든 조합 생각.
     b. 구한 조합들을 comb_speed_list에 추가.

5. 0부터 efficiency 리스트의 길이까지 (즉, 0개부터 6개까지) 반복한다:
     a. efficiency 리스트에서 z개씩 뽑은 모든 조합을 구한다.
     b. 구한 조합들을 comb_effi_list에 추가한다.

6. comb_speed_list에 저장된 요소(각 조합 집합)의 개수를 출력한다.

7. 각 조합의 크기별 (0개, 1개, 2개, …, 6개)로 comb_speed_list와 comb_effi_list의 대응되는 원소들에 대해 다음을 수행:
     a. speed 리스트에서의 조합 집합과 efficiency 리스트에서의 조합 집합을 각각 current_speed와 current_effi에 할당.
     b. current_speed와 current_effi에서 같은 위치에 있는 각각의 조합을 쌍으로 매칭하여 반복.
          i. 만약 speed 조합(예: j)이 비어있지 않으면 다음을 계산:
               - speed 조합의 합: sum(j)
               - efficiency 조합의 최솟값: min(y)
               - 두 값을 곱한 결과: sum(j) * min(y)
          ii. 이 결과들을 출력.

import itertools

comb_speed_list = []
comb_effi_list = []

def nCr(a, r):
    return list(itertools.combinations(a, r))

speed = [2,10,3,1,5,8],
efficiency = [5,4,3,9,7,2],

for i, z in zip(range(len(speed[0])+1), range(len(efficiency[0])+1)):
    combi_speed = nCr(speed[0],i)
    comb_speed_list.append(combi_speed)
    combi_effi = nCr(efficiency[0],z)
    comb_effi_list.append(combi_effi)

print(len(comb_speed_list))

num = 0

for i, x in zip(comb_speed_list, comb_effi_list):
    for j, y in zip(i, x):
        if j :
            print(j, y, sum(j), min(y), sum(j)*min(y))
