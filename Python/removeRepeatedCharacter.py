'''
Created on Oct 15, 2014

@author: Ben Athiwaratkun (pa338)

'''

# This python code removes repeated character in string (adjacent repeated characters)

def removeRepeatedCharacter(s):
    sA = []
    previousCh = None
    for ch in s:
        if not ch == previousCh:
            sA.append(ch)
            previousCh = ch
    return "".join(sA)

#################
def main():
    print removeRepeatedCharacter("benn")
    print removeRepeatedCharacter("been")
    print removeRepeatedCharacter("ben")
    print removeRepeatedCharacter("")

if __name__ == "__main__":
    main()