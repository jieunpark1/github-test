#hash set : hash table에서 우리가 저장하고 싶은건 key값, value는 필요없는 경우
# - 특징
# -- key값이 겹치지 않음
# -- 있는지 없는지 여부 확인: O(1) <- hash function 덕분에 가능

hash_set = set()

# add
hash_set.add(2022348)
hash_set.add(2023123)
hash_set.add(2024374)
hash_set.add(2024958)
hash_set.add(2024958) #같은 값은 중복해서 저장x
hash_set.add(2024374) #같은 값은 중복해서 저장x
print(hash_set)

print(2023348 in hash_set) #hash set에서 어떤 값의 존재 여부 -> O(1)