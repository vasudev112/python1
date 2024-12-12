# sets
s = {1,"set",2.3,3,4,6,True}
print(type(s))
 
s = {}
print(type(s))

s = ()
print(type(s))
print(s)

s = {1,"set",2.3,3,4,6,True,False}
print(type(s))
print(s)

# accesing
s = {1,"set",2.3,3,4,6,True}
print(s)

# adding elements to set
a = {"vijay","venkat","pavan","vamsi"}
a.add("praveen")
print(a)
print(type(a))

# update the elements
s = {1,"set",2.3,3,4,6,True}
a = {"vijay","venkat","pavan","vamsi"}
a.update(s)
print(a)

# remove the elements in set
print(a)
a.remove("vijay")
print(a)

# discard 
a.discard("venkat")
print(a)

# pop
a.pop()
print(a)
a.pop()
print(a)

