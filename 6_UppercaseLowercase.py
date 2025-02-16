def count_characters(sentence):
    digits=sum(c.isdigit() for c in sentence)
    uppercase=sum(c.isupper() for c in sentence)
    lowercase=sum(c.islower() for c in sentence)
    print(f"Digits: {digits}, Uppercase: {uppercase}, Lowercase: {lowercase}")
sentence = input("Enter a sentence: ")
count_characters(sentence)