#%%
T = [73, 74, 75, 71, 69, 72, 76, 73]

# %%
stack = []
answer = [0] * len(T)
for i, cur_temp in enumerate(T):
    # 현재 온도 보다 높은 값이 나오면 스택에서 값을 뽑고 인덱스 차이(날짜 차이) 만큼을 저장 리스트에 저장
    while stack and cur_temp > T[stack[-1]]:
        last = stack.pop()
        answer[last] = i - last

    # 현재 온도 보다 낮은 값이 나오면 스택에 저장
    stack.append(i)
# %%
