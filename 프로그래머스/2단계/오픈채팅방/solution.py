#%%
record = [
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan",
]

# %%
user_info = {}
result = []

for r in record:
    try:
        method, user_id, name = r.split()
        user_info[user_id] = name
    except:
        pass

for r in record:
    try:
        method, user_id, _ = r.split()
        if method == "Enter":
            result.append(user_info[user_id] + "님이 들어왔습니다.")
    except:
        method, user_id = r.split()
        result.append(user_info[user_id] + "님이 나갔습니다.")


result
# %%
