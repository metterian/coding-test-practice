#%%
n = 8
input_data = 'c2'
c, r = ord(input_data[0]) - ord('a')+1, int(input_data[1])


# %%
moves = [(2,1), (-2,1), (-2,-1), (2,-1), 
         (1,2), (1, -2), (-1,2), (-1,-2)]


answer = 0
for col, row in moves:
    if 1 <= r+row <= 8 and 1<= c+col <=8:
        print(r+row, c+col)
        answer+=1

print(answer)

# %%

# %%
