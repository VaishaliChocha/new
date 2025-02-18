def find_character_indices(string,char):
    indices=[i for i, c in enumerate(string) if c==char]
    print(f"Indices of '{char}' in the string:{indices}")
string=input("Enter a string: ")
char=input("Enter the character to find: ")
find_character_indices(string,char)
