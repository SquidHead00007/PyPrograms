wrd=input("Please enter a word: ")
wrd=str(wrd)
rvs=wrd[::-1]
print("This is the word in reverse.")
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")