#%%
import sys
input = sys.stdin.readline
n = 7

# %%
stack = []
for _ in range(n):
    inst = input().split()


    if len(inst) == 2:
        inst, data = inst
    else:
        inst = inst[0]

    if inst == 'push':
        stack.append(data)
    elif inst == 'top':
        if not stack:
            print(-1)
        else: print(stack[-1])
    elif inst == 'size':
        print(len(stack))
    elif inst == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif inst == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
# %%
