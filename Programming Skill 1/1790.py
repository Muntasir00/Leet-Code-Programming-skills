def areAlmostEqual(s1: str, s2: str):
    if list(s1) != list(s2): return False
    mark = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]: mark += 1
        print(mark)
        if mark > 2: 
            print(mark)
            return False
    return True

print(areAlmostEqual("abcc", "abca"))