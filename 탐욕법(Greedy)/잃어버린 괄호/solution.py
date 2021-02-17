#%%
polynomial = '55-50+40'
# %%
n = len(polynomial)

# 입력을 숫자와 연산자로 분리
operators, digits = [], []
k = 0
for i in range(n-1):
    if not polynomial[i].isdigit():
        operators.append(polynomial[i])
        digits.append(polynomial[k:i])
        k = i + 1
digits.append(polynomial[k:])
digits = list(map(int, digits))

# %%
# - 일 경우 괄호를 씌어 연산
minus = False
num = digits[0]
j = 1
for opt in operators:
    if opt == '-':
        minus  = True

    if minus:
        num -= digits[j]
    else:
        num += digits[j]
    j += 1

print(num)
# %%

# %%
