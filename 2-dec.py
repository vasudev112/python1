#write a program without using eval() to get a input value
l = input("enter the list : ")

s = int(l)

print(l[0])
print(type(s))
print(type(l[1]))

#print a integers list to divisible with 7 but not with 5 from 100 to 200

result = []

for number in range(100, 201):
    if number % 7 == 0 and number % 5 != 0:
        result.append(number)

print(result)
