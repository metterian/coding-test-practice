#%%
n =2
# n = int(input())
height = n*3
width = 2*height  -1

def print_star( left, mid, right):
    if mid <= 0:
        return

    print_star(left +1, mid-2, right+1)

    #left
    print(' '*left, end='')
    #star
    print('*'*mid, end='')
    # right
    print(' '*right)



print_star(0, width, 0 )
# %%
