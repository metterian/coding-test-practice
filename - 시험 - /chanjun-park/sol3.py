#%%


s = '''iPhone 12 / iPhone 12 Pro are available up to 256/512GB storage size respectively.'''
arr1 = [12, 256, 512]
arr2 = [13, 512, 1024]
ANSWER = """iPhone 13 / iPhone 13 Pro are available up to 512/1,024GB storage size respectively."""
#%%
s = '''Pujols(41, infielder) reached 11,114/275 ABs, 679/17 HRs, 672/3 2Bs for his 21-season-career/this season.'''
arr1 = [2, 41, 17, 21, 11114]
arr2 = [3, 51, 21, 34, 12345]
ANSWER = """Pujols(41, infielder) reached 12,345/275 ABs, 679/21 HRs, 672/3 3Bs for his 34-season-career/this season."""


thousand_sep = lambda num : '{:,}'.format(num)


arr1 = list(map(thousand_sep, arr1))
arr2 = list(map(thousand_sep, arr2))

translation  = {a : b for a,b in zip(arr1, arr2)}

import re
extract = lambda x : re.findall('[0-9,]+', x)
#%%
def custom_make_translation(text, translation):
    regex = re.compile('|'.join(map(re.escape, translation)))
    return regex.sub(lambda match: translation[match.group(0)], text)

#%%
tokens = []

for token in s.split():
    for a, b in zip(arr1, arr2):
        if '(' in token or ')' in token:
            if token in tokens:
                break
            tokens.append(token)
        elif a in extract(token):
            token = token.replace(a, b)
            tokens.append(token)
        elif token not in tokens:
            if not extract(token):
                tokens.append(token)


print(' '.join(tokens))

# %%
