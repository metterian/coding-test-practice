"""
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""
#%%
s = "0123454321"
# %%
def longestPalindrome( s: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right <= len(s) and s[left] == s[right-1]:
            left -= 1
            right += 1
        return s[left+1: right-1]

    result = ''
    for i in range(len(s)-1):
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)
    return result

longestPalindrome(s)
# %%
