
a = input()
b = input()

print(a+b)



s = input()
k = int(input())

if k>=0 and k < len(s):
    print(s[k])
else:
    print("Invalid index")



s = input() 

if len(s) <= 1: 
    print("No characters found at odd indices.") 
else: 
    print(*s[1::2])


s = input()

if len(s) == 0:
    print("No characters found at even indices.")
else:
    print(*s[0::2])


#Reverses a given string.
#Input Format
#The input consists of a single line containing a string.
#Output Format
#Output the reversed string.

S = input()

Print(s[::-1])





s = input()

if s == s[::-1]:
    print("Yes")
else:
    print("No")


#Prints all the alphabetic characters present in a given string in the order of their occurrence.
#Input Format
#The program takes a single line of input containing a string. The string can contain alphabets (both uppercase and lowercase), whitespaces, and special characters.
#Output Format
#Print the characters in the order of their occurrence. If no valid characters are found, output 'No valid characters found.'


s = input()

found = False

for ch in s:
    if ch.isalpha():
        print(ch, end=" ")
        found = True

if not found:
    print("No valid characters found.")


#Extracts and prints all the special characters present in a given string in the order of their occurrence.
#Input Format
#The program takes a single line of input containing a string.
#Output Format
#Print the special characters in the order of their occurrence separated by spaces.
#If no special characters are found, output 'No special characters found.'

s = input()

found = False

for ch in s:
    if not ch.isalnum() and not ch.isspace():
        print(ch, end=" ")
        found = True

if not found:
    print("No special characters found.")




#Count the number of vowels in a given string.
#Input Format
#The input consists of a single line containing the input string.
#Output Format
#Output the count of vowels in the given string.


s = input() 
count = 0 

for ch in s: 
    if ch.lower() in "aeiou": 
        count += 1 

print(count)
















