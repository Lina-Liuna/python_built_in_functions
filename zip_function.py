#python zip() function joins two tuples together
#the zip() function returns a zip object, which is an iterator of tuples where the first item in each
#passed iterator is paired together, and then the second item in each passed iterator are paired together etc.

#the iterator with the least items decides the length of the new iterator.

a = ("a", "b", "c", "d")
b = ("1", "2", "3", "4", "5", "6")

x = zip(a, b)
print(tuple(x))

#to loop over two or more sequences at the same time, the entries can be paired with the zip() function.

questions = ['name', 'quest', "favorite color"]
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('what is your {0}? it is {1}. ' .format(q, a))
