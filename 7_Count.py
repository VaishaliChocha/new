def count_vowels_consonants_blanks(string):
    vowels="aeiouAEIOU"
    blanks=string.count(" ")
    vowel_count=sum(1 for c in string if c in vowels)
    consonant_count=sum(1 for c in string if c.isalpha() and c not in vowels)
    print(f"Vowels:{vowel_count},Consonants:{consonant_count},Blanks:{blanks}")
string=input("Enter a string:")
count_vowels_consonants_blanks(string)