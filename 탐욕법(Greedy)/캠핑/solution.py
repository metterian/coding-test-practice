#%%

case_num = 1

while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    if V%P <= L:
        print(f'Case {case_num}: {V//P*L + V%P}')
    else:
        print(f'Case {case_num}: {V//P*L + L}')
    case_num += 1


# %%
