# 원본 문제는 합이 1976이 되는 자연수들의 곱의 최대 곱을 구하라는 문제였음.

# n을 받아서 맞는 답을 내면서 시간, 공간 복잡도를 최적화해보고 싶어짐

# 일단 수학적인 답부터
# Official solution:
# Answer: 2·(3^658).
# There cannot be any integers larger than 4 in the maximal product, because for n > 4, 
# we can replace n by 3 and n - 3 to get a larger product. 
# There cannot be any 1s, because there must be an integer r > 1 (otherwise the product would be 1) 
# and r + 1 > 1.r. 
# We can also replace any 4s by two 2s leaving the product unchanged. 
# Finally, there cannot be more than two 2s, 
# because we can replace three 2s by two 3s to get a larger product. 
# Thus the product must consist of 3s, and either zero, one or two 2s. 
# The number of 2s is determined by the remainder on dividing the number 1976 by 3.
# 1976 = 3·658 + 2, so there must be just one 2, giving the product 2·(3^658).

# 해석하자면 결과론적으로 얻는 최대 곱에서 4보다 큰 수는 있을 수 없음. => n > 4에서 n(n - 3)이 n 보다 크기 때문임.
# 또한 1도 있을 수 없음. => 1보다 큰 수가 하나라도 있다면, n > 1 에서 n + 1 > n * 1 이기 때문임. (또한 이 n > 1은 항상 찾을 수 있음)
# 또한 모든 4를 2 * 2로 쪼개도 곱은 변하지 않음.
# 지금까지 그럼 남은 후보군은 2, 3밖에 없음. 
# 여기서 2개 초과의 2는 존재할 수 없음.
# 2가 3개 이상 있다면 2 ^ 3 < 3 ^ 2에 의해서 3개씩 줄여나갈 수 있음.
# 따라서 2는 0개, 1개, 2개 까지 있을 수 있고, 나머지는 전부 3이여야 함.
# n개에 대해서 확장시켜 보자면 n을 3으로 나눈 나머지는 0, 1, 2일 수 있음.

# n = 3k인 경우, 3 ^ k가 있게 됨. 이를 합쳐서 2로 나누면 작아지므로 이거밖에 없음.
# n = 3k + 1 => 3 ^ k * 1 과 2 ^ 2 * 3 ^ (k - 1)을 비교하면, 후자가 더 큼
# n = 3k + 2 => 3 ^ k * 2 밖에 있을 수 없음. 

# pip install sympy 필요, 소인수분해해주는 라이브러리래
from sympy import factorint

def solution(n):
    """합이 n인 자연수들의 곱의 최대값 리턴"""
    if n % 3 == 0:
        return 3 ** (n // 3)
    elif n % 3 == 1:
        return 4 * (3 ** (n // 3 - 1))
    else:
        return 2 * (3 ** (n // 3))

factors = factorint(solution(1976))
print(factors)  # {2: 1, 3: 658}
