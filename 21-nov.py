print ("hello world")

name = 'vasu'
name1 = "deva"
name2 = """pavan"""
print(type(name))
print(type(name1))
print(type(name2))

name = "vasudeva"

print(name[1])
print(name[5])
print(name[-1])

s = "hello well to my python program"
ss = "python"
print(ss in s)
if ss in s:
 print("ss is available in s")
if ss not in s:
 print("ss is not available in s")
username = " vasudeva "
print(len(username))
ss = username.strip()
print(ss)
print(len(ss))
s = "well come to my program" 
ns = s.replace(" ","")
print(ns)
numbers = "1234567890"
print(numbers[0:10:2])
print(numbers[1:10:3])
name = "well come to my program"
ns = name.replace(" ","$")
print(ns)
ps = name.replace("program","python")
print(ps)
