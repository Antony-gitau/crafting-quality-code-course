"""
this function will receive a string and output a boolean
algorithm 1
we shall reverse that string 
   - this means we shall grab the first character of the input string
   - then add it to it the reversed string
then compare it with the original string
it has to be the same if it a palindrome
else not

 """
def Is_palindrome_algo1(s):
    print(reverse(s) == s)
    

def reverse(s):
    rev = "" #this is the empty string that we append the reversed string

    for ch in s:  #for every character in the input string,
        rev =ch + rev #ass the character to the beginning of rev
    return rev #then return the new string

stringy = input("input a string:" ) #ask someone to input a string

Is_palindrome_algo1(stringy) #call the function and pass the input string.