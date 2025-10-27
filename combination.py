def allAnagrams(text):
    if len(text) == 0:
        return ['']
    
    anagrams = []
    for i, char in enumerate(text):
        remaining = text[:i] + text[i+1:]
        for sub_anagram in allAnagrams(remaining):
            anagrams.append(char + sub_anagram)
    
    return anagrams

print(allAnagrams('abc'))
