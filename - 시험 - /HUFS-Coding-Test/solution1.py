#%%
n = int(input())
# n = 2
height = n*3
width = 2*height  -1
wide = -1
if n%2 ==0: mid = width//2
else: mid =  width//2

for r in range(height):
    wide+=1
    for c in range(width):
        if c == mid:
            print('*', end='')
        elif mid-wide  <= c <= mid+wide:
            print('*', end='')
        else:
            print(' ', end='')
    print('')
if n%2==0:
    t_wide = n-1
else:
    t_wide = -1
for r in range(n):
    for c in range(width):
        if c == mid:
            print('|', end='')
        elif mid -t_wide <= c <= mid+t_wide:
            print('|', end='')
        else:
            print(' ', end='')
    print()

# %%

3# %%
