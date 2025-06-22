#완전 탐색: 모든 가능성을 모두 찾아, 주어진 조건을 만족하는 최적 해를 찾는 패러다임
# 반복문, 재귀, 비트마스크
# - 장점: 가장 기초적 방법 / 최적의 해
# - 단점: 시간 복잡도가 높아짐 / 10^8 이내로 시간복잡도 구현해야 통과

# 참고) 탐색 알고리즘: 선형탐색, 이진탐색, 비선형탐색(DFS/BFS)


# 문) 
print("문1) 리스트 [4,9,7,5,1]에서 두 개의 숫자를 더해서 14가 될 수 있나요? (중복x)")
nums =  [4,9,7,5,1]
target = 14

def solution(nums, target):
    n = len(nums)
    ans_ = []

    for i in range(n):
        for j in range(i+1, n):
            print(nums[i], nums[j], "=", nums[i] + nums[j])
            if nums[i] + nums[j] == target:
                print("valid solution")
                ans = "yes"
                ans_.append((nums[i], nums[j]))
    if ans == None:
        ans = "no"
        ans_ = None
            
    return ans, ans_

ans, ans_ = solution(nums, target)
print(ans, ans_)



#debugging
print("============= debugging ============")
nums =  [4,9,7,5,1]
target = 14

def solution(nums, target):
    n = len(nums)
    ans_ = []

    for i in range(n):
        print(nums[i])

        for j in range(i+1, n):
            print(f"ㄴ {nums[j]}")#, nums[j], "=", nums[i] + nums[j])
            if nums[i] + nums[j] == target:
                print("valid solution")
                ans = "yes"
                ans_.append((nums[i], nums[j]))
    if ans == None:
        ans = "no"
        ans_ = None
            
    return ans, ans_

ans, ans_ = solution(nums, target)
print(ans, ans_)




print()
print("문2) 리스트 [4,9,7,5,1]에서 세 개의 숫자를 더해서 15가 될 수 있나요? (중복x)")

def solution(nums, target):
    n = len(nums)
    ans_ = []

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                print(nums[i], nums[j], nums[k], "=", nums[i] + nums[j]+nums[k])
                if nums[i] + nums[j]+nums[k] == target:
                    print("valid solution")
                    ans = "yes"
                    ans_.append((nums[i], nums[j], nums[k]))
    if ans == None:
        ans = "no"
        ans_ = None
            
    return ans, ans_

nums =  [4,9,7,5,1]
target = 15

ans, ans_ = solution(nums, target)
print(ans, ans_)


print("============= debugging ============")
def solution(nums, target):
    n = len(nums)
    ans_ = []

    for i in range(n):
        print(nums[i])
        for j in range(i+1, n):
            print(f"   ㄴ {nums[j]}")
            for k in range(j+1, n):
                print(f"      ㄴ {nums[k]} => {nums[i] + nums[j]+nums[k]}")
                #print(nums[i], nums[j], nums[k], "=", nums[i] + nums[j]+nums[k])
                if nums[i] + nums[j]+nums[k] == target:
                    print("valid solution")
                    ans = "yes"
                    ans_.append((nums[i], nums[j], nums[k]))
            print()
        print()
    if ans == None:
        ans = "no"
        ans_ = None
            
    return ans, ans_

nums =  [4,9,7,5,1]
target = 15

ans, ans_ = solution(nums, target)
print(ans, ans_)