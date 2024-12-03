#slicing 
s = ("want you what do")
print(s)
print(s[::-1])
 
#pop remove returns the last  element
l = [1,2,3,4,5,6,7,8,9]
pop = l.pop()
print(pop)
print(l)
#remove specified elements from the list
l = [20,30,40,50,90,100]
rl = l.remove(90)
print(rl)
print(l)
# reverse the elements
s = [1,2,3,4,5,6,7,8,9]
print(s)
s.reverse()
print(s)
# slicing
print(s)
# sort()
a = [0,1,2,3,4,6,-1,7,-3,-2]
a.sort()
print(a)

# clear it will remove all elements
s = [1,2,3,4,5,-1,8,-3]
s.clear()
print(s)