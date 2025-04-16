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

"""


"""
슈도코드
1. itertools을 import
2. speed, efficiency 리스트 작성
3. comb_speed_list 빈 리스트 작성
4. comb_effi_list 빈 리스트 작성
5. nCr 함수 작성, itertools.combination 사용
6. speed에 슬라이싱 [0]으로 한 range를 만들고 for문 작성
7. combi_speed 변수 만들고 nCr(n의 수, r의 값 입력)
8. com_speed_list 변수 만들고 combi_speed를 comb_speed_list에 append
9. combi_effi 변수 만들고 nCr(n의 수, r의 값 입력)
10. com_effi_list 변수 만들고 combi_effi를 comb_effi_list에 append
11. zip함수에 comb_speed_list, comb_effi_list 입력하고 for문으로 변수 2개 입력
12. zip함수에 11.에서 입력한 변수 2개 입력하고 for문으로 변수 2개 입력
13. 만약 12. for문 변수 중 하나가 True라면(변수 값 null 방지)
14. 12 함수의 변수 2개 출력 speed 요소 변수 sum 출력, efficiency 요소 변수 min 출력
15. sum하고 min 함수 곱한 값 출력
"""
