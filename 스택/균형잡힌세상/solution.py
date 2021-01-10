#%%


strings = [
"""So when I die (the [first] I will see in (heaven) is a score list).""",
"""[ first in ] ( first out ).""",
"""Half Moon tonight (At least it is better than no Moon at all].""",
"""A rope may form )( a trail in a maze.""",
"""Help( I[m being held prisoner in a fortune cookie factory)].""",
"""([ (([( [ ] ) ( ) (( ))] )) ]).""",
""" .""",

]

strings = []
while True:
    string = input()
    if string == '.': break
    strings.append(string)

# %%
def balanced(string):
    stack = []
    table = {
        ')' : '(',
        ']' : '['
    }

    for char in string:
        if char not in ['(', ')', '[', ']']:
            continue
        if char not in table:
            stack.append(char)
        elif not stack or stack.pop() != table[char]:
            return False
    return not stack

for string in strings:
    if balanced(string):print("yes")
    else: print("no")

# %%
