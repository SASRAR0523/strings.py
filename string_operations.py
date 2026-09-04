
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

# Add * before every occurrence of a in the string

s = input()

result = ""

for ch in s:
    if ch == 'a':
        result += "*" + ch
    else:
        result += ch

print(result)

# Remove all vowels from the string

s = input()

vowels = "aeiouAEIOU"
result = ""

for ch in s:
    if ch not in vowels:
        result += ch

print(result)

# Swap uppercase characters to lowercase and lowercase characters to uppercase

s = input()

result = ""

for ch in s:
    if ch.isupper():
        result += ch.lower()
    elif ch.islower():
        result += ch.upper()
    else:
        result += ch

print(result)

# Convert the given string to uppercase

s = input()

print(s.upper())

# Convert the given string to lowercase

s = input()

print(s.lower())

# Move all digits to the end of the string

s = input()

letters = ""
digits = ""

for ch in s:
    if ch.isdigit():
        digits += ch
    else:
        letters += ch

print(letters + digits)

# Keep letters first and digits after them

s = input()

letters = ""
digits = ""

for ch in s:
    if ch.isdigit():
        digits += ch
    else:
        letters += ch

print(letters + digits)

# Move all special characters to the end of the string

s = input()

specials = ""
others = ""

for ch in s:
    if not ch.isalnum() and ch != ' ':
        specials += ch
    else:
        others += ch

print(others + specials)

#Insert an asterisk (*) before each numeric character (0-9) in a given string.

s = input()

result = ""

for ch in s:
    if ch.isdigit():
        result += "*" + ch
    else:
        result += ch

print(result)


#Insert an asterisk (*) before each occurrence of the characters 'a' and 'A' in a given string.

s = input()

result = ""

for ch in s:
    if ch == 'a' or ch == 'A':
        result += "*" + ch
    else:
        result += ch

print(result)


#Insert an asterisk (*) before each vowel (a, e, i, o, u) in a given string.

s = input()

result = ""

for ch in s:
    if ch in vowels:
        result += "*" + ch
    else:
        result += ch

print(result)  


#Write a Java program that removes all leading and trailing spaces from a given string.

# Input string
s = input()

# Remove leading and trailing spaces
print(s.strip())


#Remove all lowercase characters from a given string.

s = input()

result = ""

for ch in s:
    if not ch.islower():
        result += ch

print(result)

#Remove all consonants from a given string.

S = input()

vowels = "aeiouAEIOU"
result = ""

for ch in s:
    if ch.isalpha() and ch not in vowels:
        continue
    result += ch

print(result)
#Remove all numeric characters from a given string.

s = input()

result = ""

for ch in s:
    if not ch.isdigit():
        result += ch

print(result)

#Remove all special characters from a given string.

s = input()

result = ""

for ch in s:
    if ch.isalnum():
        result += ch

print(result)

#Given a lowercase string, remove duplicate characters from it.

s = input()

result = ""

for ch in s:
    if ch not in result:
        result += ch

print(result

#Given a string, sort it in ascending order.

# Input string
s = input()

# Sort characters and join
print("".join(sorted(s)))

#Given a string, calculate the sum of all the digits in the string and concatenate the sum at the end.

s = input()

digit_sum = 0
result = ""

for ch in s:
    if ch.isdigit():
        digit_sum += int(ch)
    else:
        result += ch
                                              
result += str(digit_sum)

print(result)

#Given a string, replace all uppercase letters with '#' characters.

s = input()

result = ""

for ch in s:
    if ch.isupper():
        result += "#"
    else:
        result += ch

print(result)

#Converts a given string to its corresponding ASCII values.

s = input()

result = []

for ch in s:
    result.append(str(ord(ch)))

# Output
print(" ".join(result))

#Given a string, remove all alphanumeric characters and return the modified string.


s = input()

result = ""

for ch in s:
    # remove letters and digits
    if not ch.isalnum():
        result += ch

print(result)

#Remove all uppercase characters from a given string.

s = input()

result = ""

for ch in s:
    if not ch.isupper():
        result += ch

print(result)

#Given a string, find the smallest word from it.

str1 = input()
str2 = input()

count = 0
n = len(str2)

# Traverse str1
for i in range(len(str1) - n + 1):
    if str1[i:i+n] == str2:
        count += 1

print(count)

#Print the largest palindromic substring of a given string.

s = input()

longest = ""

for i in range(len(s)):
    for j in range(i, len(s)):
        sub = s[i:j+1]

        if sub == sub[::-1] and len(sub) > len(longest):
            longest = sub

print(longest)

#Print all palindromic substrings of length 4 from a given string.

s = input()

result = []

for i in range(len(s) - 3):
    sub = s[i:i+4]
            
    if sub == sub[::-1]:
        result.append(sub)
                      
print(" ".join(result))

#Print all palindromic substrings of a given string.

s = input()

palindromes = []
for i in range(len(s)):
    for j in range(i, len(s)):
        sub = s[i:j+1]
        if sub == sub[::-1]:
            palindromes.append(sub)

palindromes.sort(key=len)

for p in palindromes:
    print(p)

#Given a string and a substring, find the frequency of the substring in the string.

s = input()
sub = input()

count = 0
n = len(sub)

# slide through main string
for i in range(len(s) - n + 1):
    if s[i:i+n] == sub:
        count += 1

print(count)

#Print all possible substrings of a given string.

s = input()

# Generate and print all substrings
for i in range(len(s)):
    for j in range(i, len(s)):
        print(s[i:j+1])

#Check whether characters in the second string are present in the first string . There is no need for the characters to be consecutive.

str1 = input()
str2 = input()

i = 0  # pointer for str1
j = 0  # pointer for str2

while i < len(str1) and j < len(str2):
    if str1[i] == str2[j]:
        j += 1
    i += 1

if j == len(str2):
    print("Yes")
else:
    print("No")

#Given a string, find the smallest word from it.

s = input()

words = s.split()

smallest = words[0]

for w in words:
    if len(w) < len(smallest):
        smallest = w

print(smallest)

#Given a string, find the largest word from it.

# Input string
s = input()

words = s.split()

largest = words[0]

for w in words:
    if len(w) > len(largest):
        largest = w

print(largest)

#Write a program to swap the words present at odd indexes with the words present at even indexes. 

# Input string
s = input()

words = s.split()

# swap adjacent words
for i in range(0, len(words) - 1, 2):
    words[i], words[i + 1] = words[i + 1], words[i]

print(" ".join(words))

#Find the count of characters after each word in a given string.

s = input().strip()

words = s.split()

result = []

for w in words:
    result.append(w + str(len(w)))

print(" ".join(result))

#Reverse all the words in a given string while maintaining the order of the words.

# Input string
s = input()

words = s.split()

result = []

for w in words:
    result.append(w[::-1])  # reverse each word

print(" ".join(result))

#Remove duplicate characters from a given string, preserving the original order.

s = input()
seen = set()
result = []

for ch in s:
    if ch not in seen:
        seen.add(ch)
        result.append(ch)
        
print("".join(result))

#Remove duplicate characters from a given string and output the remaining characters in lexicographical order.

s = input()

unique_chars = set(s)
sorted_chars = sorted(unique_chars)

print(" ".join(sorted_chars))

# Given a string s, find the longest palindromic substring in s.

# Input Format
# A string s consisting of digits and English letters.

# Output Format
# Return a string, the longest palindromic substring found in s.

s = input()

longest = ""

for i in range(len(s)):
    for j in range(i, len(s)):
        sub = s[i:j+1]

        if sub == sub[::-1]:
            if len(sub) > len(longest):
                longest = sub

print(longest)









            

































