#재귀 Recursion
#: 자기 자신을 호출하는 프로그래밍 기법
# - 문제를 작은 부분으로 나누어 해결하는 데 사용
# 그래프탐색, 트리, DP
# -- Factorial, Fibonaccci

# *** 점화식 + base case *** -> 이 두 가지를 연습하는 것이 필수

# factorial 팩토리얼 4! = 4 * 3* 2* 1
#n!= nx(n-1)x(n-2)x...x1

# 복잡한 답을 사람도 한번에 구하기 어려움
# 7! = 7 * 6!
# 6! = 6 * 5!

# - 단점: 부하가 생길 수 있다

def factorial(n):
    if n == 1: #base case (factorial(1)=1) 간단. 그리고 factorial(0)=0. 다 없애버림
        return 1
    answer = n * factorial(n-1)
    return answer
ans = factorial(5)
print(ans)


#코드 짤때는 예시 한개만 해보고 팩토리얼 쓰면 되겠다! 아이디어를 떠올리는 게 중요


#피보나치 수열: 앞 두개 항이 다음항
#코드 구현시에: 우리가 할 수 있는것만 말해서 f(8) = f(7) + f(6) -> f(7)이 어쨌든 답을 가져온다. f(6)이 어쨌든 답을 가져온다.
#큰 문제를 작은 부분으로 나누는 재귀함수 중 하나

def fibo(n):
  # basecase
  if n == 1 or n == 2:
    return 1
  return fibo(n-1) + fibo(n-2)

print(fibo(7))

#디버깅 시: 내부 동작을 잘 알아야 함.
#재귀에 '깊이'가 있음. 예) f(6) > f(5)(>f(4) f(3).. )+ f(4)(f(3), f(2)))..

def fibo(n, depth):
  print('   ' * depth, f'ㄴfibo({n})')
  # basecase
  if n == 1 or n == 2:
    return 1
  return fibo(n-1, depth+1) + fibo(n-2, depth+1)

print(fibo(6, 0))

"""
 ㄴfibo(6)
    ㄴfibo(5)
       ㄴfibo(4)
          ㄴfibo(3)
             ㄴfibo(2)
             ㄴfibo(1)
          ㄴfibo(2)
       ㄴfibo(3)
          ㄴfibo(2)
          ㄴfibo(1)
    ㄴfibo(4)
       ㄴfibo(3)
          ㄴfibo(2)
          ㄴfibo(1)
       ㄴfibo(2)

"""




# 수학적 접근
#: n번째 함수를 n-1번째 함수로 표현하는 것이다. 
# 1. 점화식이 꼭 필요.
# -- 예 ) f(n) = n * f(n-1) (factorial)  / f(n) = f(n-1) + f(n-2)
#무한루프 빠질 수 있음
# 2. base case 꼭 필요: 무한루프 방지. 더 이상 자기자신을 재참조하지 않아도 return 가능한 상황


# 재귀의 시간복잡도 (정확하진 않음)
# 1. n = 재귀 함수 몇 번 호출 n번
# 2. 재귀함수 하나 당 시간복잡도
# factorial 함수 ->  호출 n번 * O(1) = O(n*1)  
# fibonacci 함수 ->  호출 2^n * O(1) = O(2^n*1)