#Accept a String input from the stdin or file
# Print the count of words in the String. Space is assumed to be the separator between words
#Print the count of alphabets & numbers in the String

#Accept input from uer and remove starting and ending spaces using strip()
s=input("Enter your word").strip()
word=1
alphabet=1
digit=0
#loop through string to count number of words,alphabets and digits(isalpha()&isdigit())
for i in range(len(s)-1):
    if(s[i]==" "):
        word=word+1
    if(s[i].isalpha()):
        alphabet=alphabet+1
    else:
        if(s[i].isdigit()):
            digit=digit+1
print("Total words-",word)
print("alphabets -",alphabet)
print("Numbers -",digit)





