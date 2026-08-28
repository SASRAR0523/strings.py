
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

#Given a string, count the number of alphanumeric characters in it.

s = input()

# Count alphanumeric characters
count = 0
for ch in s:
    if ch.isalnum():
        count += 1

print(count)

#Given a string, count the number of characters in it.

s = input()

# Count characters
print(len(s))

#Given a string, count the number of numeric characters in it.

s = input()

# Count numeric characters
count = 0
for ch in s:
    if ch.isdigit():
        count += 1

# Output
print(count)

#Given a string, count the number of uppercase characters in it.

s = input()

# Count uppercase characters
count = 0
for ch in s:
    if ch.isupper():
        count += 1

# Output
print(count)

#Given a string, count the number of uppercase characters in it.

s = input()

# Count uppercase characters
count = 0
for ch in s:
    if ch.isupper():
        count += 1

# Output
print(count)

#Given a string, count the number of lowercase characters in it.

s = input()

# Count uppercase characters
count = 0
for ch in s:
    if ch.islower():
        count += 1

# Output
print(count)

#Counts the number of special characters in a given string. Do not consider space as special character for this problem.

s = input()

# Count special characters
count = 0
for ch in s:
    if not ch.isalpha() and not ch.isdigit() and ch != ' ':
        count += 1

print(count)

#Count the number of consonants in a given string.

s = input()

# Define vowels
vowels = "aeiouAEIOU"

# Count consonants
count = 0
for ch in s:
    if ch.isalpha() and ch not in vowels:
        count += 1

print(count)

#Counts the number of vowels, consonants, and special characters in a given string.

vowels = "aeiouAEIOU"

v_count = 0
c_count = 0
s_count = 0

s = input()

for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1
    else:
        s_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)
print("Special Characters:", s_count)

























