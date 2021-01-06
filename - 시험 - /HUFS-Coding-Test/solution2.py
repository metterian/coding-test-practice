
def palindrome (s, left, right):
    if len(s)%2 == 0  and left+1 == right:
        if s[left] == s[right]:
            return True
        else:
            return False

    if len(s)%2 != 0 and left+1== right-1:
        if s[left] == s[right]:
            return True
        else:
            return False

    if s[left] == s[right] and palindrome(s, left+1, right-1 ):
        return True
    else:
        return False

s = input().lower()
# s = input().lower()
s = "".join(s.split())

result = palindrome(s, 0, len(s)-1)
print(result)


