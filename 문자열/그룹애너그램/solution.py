#%%
strs = ["eat","tea","tan","ate","nat","bat"]
# %%
from collections import defaultdict
from typing import *
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagram = defaultdict(list)

    for word in strs:
        anagram["".join(sorted(word))].append(word)
    return anagram
groupAnagrams(strs)
# %%
