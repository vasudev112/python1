# set joins
# union()
a = {1,2,4,5,7,9,5,6}
s = {0,3,5,4,8,}
print(a.union(s))

# intersection
a = {1,2,4,5,7,9,5,6}
s = {0,3,5,4,8,}
print(a.intersection(s))

# difference
a = {1,2,4,5,7,9,5,6}
s = {0,3,5,4,8,}
print(a.difference(s))

# system difference
a = {1,2,4,5,7,9,5,6}
s = {0,3,5,4,8,}
print(a.symmetric_difference(s))

# dictonary
c = {"name":"pavan","age":34,"active":True,"percentage":85.666}
print(c)

# decleration
print(type(c))
print(c)
c ["name"]="vamsi"
c ["agee"] = 30
c ["salary"] = 23000
print(c)

no_products = 5
products = {}
for i in range(no_products):
    key = input("enter your key :")
    value = input("enter your value :")
    products[key] = value
print(products)