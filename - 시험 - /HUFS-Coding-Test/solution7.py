#%%
text = input()

# %%
espa = ["a,", "e,", "i,", "n~", "o,", "u,", "u.."]

for ch in espa:
    if text.find(ch) >= 0:
        text = text.replace(ch, ch[0])

# %%
print(len(text))
# %%
