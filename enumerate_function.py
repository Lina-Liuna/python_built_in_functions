#Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
#the enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.

#enumerate(iterable, start=0)
#iterable: any object that supports iteration
#Start: the index value from which the counter is to be started, by default it is 0

l1 = ["morning", "noon", "night"]
s1 = "everyday"

obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("return type:", type(obj1))
print(list(obj1))

print("return type:", type(obj2))
print(list(obj2))