#%%
numbers  = [3, 30, 34, 5, 9]

#%%
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x: x*3, reverse=True)
    print(list(map(lambda x: x*3, numbers)))
    answer = int("".join(numbers))
    return str(answer )

solution(numbers)

"""

문자열 비교연산의 경우엔 첫번째 인덱스인 666[0]인 6과 101010[0]인 1과 222[0]인 2를 ascii숫자로 바꿔서 비교합니다.
물론 같으면, 다음 인덱스도 비교합니다. 비교한 결과 [6, 2, 10]의 순으로 정렬됩니다.


"""
# %%
from functools import cmp_to_key

def myCompare(a, b):
    t0 = int(a + b)
    t1 = int(b + a)
    return (t0 > t1) - (t0 < t1)

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=cmp_to_key(myCompare), reverse=True)
    return str(int(("".join(numbers))))


solution(numbers)






# %%
