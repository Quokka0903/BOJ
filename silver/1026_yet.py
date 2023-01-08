import sys
input = sys.stdin.readline

N = int(input())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

hubo = set()
def makecombi(stack, rest):
    if len(stack) == 5:
        hubo.add(stack)
        return
    
    for unit in rest:
        rest.remove(unit)
        makecombi(stack + [unit], rest[:])
        rest.append(unit)

print(hubo)

# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# # 가장 작은 숫자부터 B의 가장 큰숫자랑 곱해주면 가장 작은 값이 나올 것
# # A를 정렬
# A.sort()
# # 결과값 초기화
# result = 0
# # N만큼 반복해보자
# for i in range(N):
#     # 결과값에 가장작은 A와 가장 큰 B를 곱하자
#     result += A[i] * max(B)
#     # 가장 큰 B는 곱해졌기 때문에 제외시키자
#     B.remove(max(B))
# # 결과출력
# print(result)