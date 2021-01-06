# %%
n = input()
numbers = list(map(int, input().split()))
max_num = max(numbers)
max_num_len = len(str(max_num))

numbers = sorted(numbers, key=lambda x: int(str(x)+ "0"*(max_num_len-len(str(x)))), reverse=True)
numbers = list(map(str, numbers))
print("".join(numbers))
# %%
