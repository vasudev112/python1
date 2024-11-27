#count occurrence of given character 1
a = "wellcome to python"
aa = a.count("l")
print(aa)

# Python Code to check if two Strings are anagram of each other using sorting 2
def areAnagrams(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    return s1 == s2

if __name__ == "__main__":
    s1 = "geeks"
    s2 = "kseeg"
    print("true" if areAnagrams(s1, s2) else "false")

# Write a program to check whether a string is palindrome or not in python 3
def isPalindrome(s):
    return s == s[::-1]
s = "proogram"
a = isPalindrome(s)
if a:
    print("Yes")
else:
    print("No")    

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
string = "proogram"
p = " "
for char in string:
	if char not in p:
		p = p+char
print(p)

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
a = "GeeksforGeeks"
s = max(a, key=lambda x: a.count(x))
print(s)

# replace first occurrence of vowel with "-" in strinh 18
s = "An apple A day keeps doctor Away."
s = s.replace('a', '$')
print(s)

# count alphabets ,digits and special characters 19
string = "program123!@"
total_letters = sum([1 for char in string if char.isalpha()])
total_digits = sum([1 for char in string if char.isdigit()])
print("Total letters found :-", total_letters)
print("Total digits found :-", total_digits)

# chicking character is digit or not using isdigit()method 20
s = "12345"
print(s.isdigit())  

s2 = "1234a5"
print(s2.isdigit())
print("......")
# to calculate sum of integers in string 21
def getSum(n): 
    sum = 0
    for digit in str(n):  
      sum += int(digit)       
    return sum

# print all non repeating character in string 22

S = "prepinsta"
for i in S:
    count = 0
    for j in S:
        if i == j:
            count+=1
        if count > 1:
            break
    if count == 1:
        print(i,end = " ")

#copy one string to another string 23

s = input("Please Enter Your Own String : ")
a = s
r = s[:]
print("The Final String : a  = ", a)
print("The Final String : r  = = ", r)


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