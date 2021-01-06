#%%

text = input()
f = input()
cnt = 0
#%%
def findDocument(s, f):
    global cnt
    if s.find(f) < 0:
        return
    else:
        cnt+=1
        start = s.find(f)
        findDocument(s[start+len(f):],f)

# %%
findDocument(text, f)
print(cnt)
# %%
