#%%
num  = input()

Mors = []

for i in str(num):
    if int(i) == 1:
        Mors.append("*----")
    elif int(i) == 2:
        Mors.append("**---")
    elif int(i) == 3:
        Mors.append("***--")
    elif int(i) == 4:
        Mors.append("****-")
    elif int(i) == 5:
        Mors.append("*****")
    elif int(i) == 6:
        Mors.append("-****")
    elif int(i) == 7:
        Mors.append("--***")
    elif int(i) == 8:
        Mors.append("---**")
    elif int(i) == 9:
        Mors.append("----*")
    elif int(i) == 0:
        Mors.append("-----")

reversed(Mors)
print("".join(Mors))

# %%
