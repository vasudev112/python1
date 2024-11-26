#count occurrence of given character 1
a = "wellcome to python"
aa = a.count("l")
print(aa)

# Python Code to check if two Strings are anagram of 
# each other using sorting 2
def areAnagrams(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    return s1 == s2

if __name__ == "__main__":
    s1 = "geeks"
    s2 = "kseeg"
    print("true" if areAnagrams(s1, s2) else "false")

# Write a program to check whether a string is palindrome or not in python 3
def is_palindrome(s):
    return s == s[::-1]

string = "amaama"
if is_palindrome(string):
    print("The entered string is palindrome")
else:
    print("The entered string is not palindrome")    

#replace the string space with a given character 4
a = "hello python"
a = a.replace(" ","-")
print(a)

#replace a string character using replace() method 5
a = "wellcome to my python"
aa = a.replace("python","program")
print(aa)
print(".......")

#convert lowercase to uppercase 6
a = "wellcome to my program"
ss = a.upper()
print(ss)
print("...")

# define lowercase vowels 7
str1="Great Power";  
newStr = "";  
for i in range(0, len(str1)):   
    if str1[i].islower():  
        newStr += str1[i].upper()
    elif str1[i].isupper():  
        newStr += str1[i].lower();  
      
    else:  
        newStr += str1[i];          
print("String after case conversion : " +  newStr)

#seperater character in a given string 8
a = "skywaves"
aa = list(a)
print(aa)
print(",,,,")

#remove blank space from string 9
a = "wellcome to my world"
aa = a.replace (" ","")
print(aa)
 
 #concatenate two strings using join()method 10
a = "Python" 
s = "program"
print(" ".join([a,s])) 

 #concatenate two strings without using join()method  11
a = "python"
s = "program"
r = a+s
print(r)

#remove repeated character from string 12
def remove_duplicates(input_string):
    return ''.join(dict.fromkeys(input_string))

print(remove_duplicates("programming"))

# character is vowel or consonant. 13
l = ['a', 'e', 'i', 'o', 'c'] 
if chr in l: 
	print(chr, "is a vowel") 
else: 
	print(chr, "is a consonant") 

#check the character is digit or not 14
a = "abc123"
aa = a.isdigit()
print(aa)	
b = "123"
s = b.isdigit()
print(s)

# delete vowels string in given string 15
string = "PrepInsta"
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""
for i in range(len(string)):
    if string[i] not in vowels:
        result = result + string[i]
print("\nAfter removing Vowels: ", result)

# count the occurrence of vowels and consonants in string 16
str1 = input("Please Enter Your Own String : ")
vowels = 0
consonants = 0

for i in str1:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
       or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1
print("Total Number of Vowels in this String = ", vowels)
print("Total Number of Consonants in this String = ", consonants)

# print the highest frequency character in string 17
string= "python"
print(string)
char_freq={}
for i in string:
    if i in char_freq:
        char_freq[i]=char_freq[i]+1
    else:
        char_freq[i] = 1
result= max(char_freq, key = char_freq.get)
print("Most frequent character: ",result)

# replace first occurrence of vowel with "-" in strinh 18
str = "An apple A day keeps doctor Away."
str = str.replace('a', '$')
str = str.replace('a'.upper(),'$')
print("Modified string : ")
print(str)

# count alphabets ,digits and special characters 19
 
def count_characters(input_string):
    alphabets = 0
    digits = 0
    special_chars = 0
    for char in input_string:
        if char.isalpha(): 
            alphabets += 1
        elif char.isdigit(): 
            digits += 1
        else: 
            special_chars += 1
    return alphabets, digits, special_chars
input_string = input("Enter a string: ")
alphabets, digits, special_chars = count_characters(input_string)
print(f"Alphabets: {alphabets}")
print(f"Digits: {digits}")
print(f"Special characters: {special_chars}")

# chicking character is digit or not using isdigit()method 20
s = "12345"
print(s.isdigit())  

s2 = "1234a5"
print(s2.isdigit())
print("......")
# to calculate sum of integers in string 21

def sum_of_integers_in_string(input_string):
    total_sum = 0
    temp = ""  
    for char in input_string:
        if char.isdigit(): 
            temp += char 
        else:
            if temp: 
                total_sum += int(temp)
                temp = "" 
    if temp: 
        total_sum += int(temp)
    return total_sum
input_string = input("Enter a string: ")
result = sum_of_integers_in_string(input_string)
print("Sum of integers in the string:", result)

# print all non repeating character in string 22

String = "prepinsta"
for i in String:
    count = 0
    for j in String:
        if i == j:
            count+=1
        if count > 1:
            break
    if count == 1:
        print(i,end = " ")

#copy one string to another string 23

def copy_string(source_string):
    destination_string = source_string
    return destination_string
source_string = input("Enter a string: ")
destination_string = copy_string(source_string)
print("Copied string:", destination_string)

# character is vowel or consonant. 24
l = ['a', 'e', 'i', 'o', 'c'] 
if chr in l: 
	print(chr, "is a vowel") 
else: 
	print(chr, "is a consonant") 

#check the character is digit or not 25
a = "abc123"
aa = a.isdigit()
print(aa)	
b = "123"
s = b.isdigit()
print(s)