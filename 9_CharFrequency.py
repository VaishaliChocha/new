def character_frequency(string):
    freq={}
    for char in string:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    for char,count in freq.items():
        print(f"'{char}':{count}")
string=input("Enter a string: ")
character_frequency(string)
