#%%

def get_divisor(n):
    n = int(n)
    divisors = []
    divisors_back = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisors.append(i)
            if (i != (n // i)):
                divisors_back.append(n//i)

    return divisors + divisors_back[::-1]




def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        surplus = len(get_divisor(i))
        if surplus%2 == 0:
            answer += i
        else:
            answer -= i
    return answer



solution(13, 17)

# %%
