#%%
# INPUT
croatias = 'ddz=z='

# %%
alphabets = [
'c=',
'c-',
'dz=',
'd-',
'lj',
'nj',
's=',
'z=',
]
# %%
count = 0
for alphabet in alphabets:
    croatias = croatias.replace(alphabet, '0')


len(croatias)

# %%
