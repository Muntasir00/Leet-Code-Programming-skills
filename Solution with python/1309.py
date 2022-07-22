from typing import Mapping


def freqAlphabets(s):
    s = list(s)
    mapping = {str(i):chr(96+i) for i in range(1,27)}
    final_string = ""
    while(s):
        ch = s.pop()
        if(ch=="#"):
            x1,x2 = s.pop(),s.pop()
            final_string+=mapping[x2+x1]
        else:
            final_string+=mapping[ch]
    return final_string[::-1]

print(freqAlphabets("10#11#12"))