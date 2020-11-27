# https: // leetcode.com / problems / valid - anagram
def isAnagram(s: str, t: str) -> bool:
    map_s = {}
    map_t = {}
    for i in s:
        if i not in map_s.keys():
            map_s[i] = s.count(i)
    for i in t:
        if i not in map_t.keys():
            map_t[i] = t.count(i)
    return map_s == map_t


print(isAnagram("a", "b"))
