



def check(bracket):
    stack = []
    for i, letter in enumerate(bracket):
        if letter == '[': stack.append(i)
        elif letter == ']':
            if stack:
                stack.pop()
            else:
                stack.append(i)
                return len(stack)==0
    return len(stack)==0


n = input()
text = input()
print(check(text))


