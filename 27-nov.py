# Python code to check if string is numeric or not without using indigit()
string = '123ayu456'
print(string.isnumeric()) 
   
string = '123456'
print(string.isnumeric())
print("........")
#python program to find index values of a mid charector

a = input("enter the string:" )
x = len(a)
y = x//2
print("middle value:",a[y])
print(",,,,,,,")

#program to Replace last Occurrence Of Vowel With ‘-‘ in String.
 
a = input("enter the string:" )
x = len(a)
y = x//2
print("middle value:",a[y])

def replace_last_vowel_with_dash(s):
    vowels = "wellcome to my world"
    for i in range(len(s) - 1, -1, -1):
        if s[i] in vowels:
            s = s[:i] + '-' + s[i + 1:]
            break 
    return s
a = "wellcome to my world"
result = replace_last_vowel_with_dash(a)
print(f"Original String: {a}")
print(f"Modified String: {result}")

