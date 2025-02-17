def exchange_first_last(string):
    if len(string)<2:
        return string
    return string[-1]+string[1:-1]+string[0]
string=input("Enter a string: ")
new_string=exchange_first_last(string)
print(f"Modified string:{new_string}")