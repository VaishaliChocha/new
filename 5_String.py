def makeNewStr(s):
    if len(s)<2:
        return 
    return s[:2]+s[-2:]
str=input("Enter string:")
print("New string:",makeNewStr(str))