# del some elements using del()
a = {"name":"pavan","age":34,"active":True,"percentage":85.666,"agee":45}
del a["agee"]
print(a)

# remove element is using pop()
print(a.pop("age"))
print(a)

# remove elements is using keys()
print(a.keys())

# remove elements is using values()
print(a.values())

# remove elements is using items()
print(a.items())
s = a.items()
print(type(s))