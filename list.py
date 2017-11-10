# list.py

classmates = ['Michael', 'Bob', 'Tracy']

print classmates # print list

# print all kinds of element
print "classmates[0] = "+classmates[0]
print "classmates[1] = "+classmates[1]
print "classmates[2] = "+classmates[2]
print "classmates[-1] = "+classmates[-1]

# get count of list
print len(classmates)

# add a element at the last of list
classmates.append('Adam')
print classmates

# insert one element to a position classmate[1]
classmates.insert(1, 'Jack')
print classmates

# delete the last element of list
classmates.pop()
print classmates

# change one element to anoher
classmates[1] = 'Sarah'
print classmates

# different element in the list
# the boolean must be like True or False
L = ['apple', 123, True, False]

print L

# list in a list
s = ['python', 'java', ['asp', 'php'], 'golang']

print len(s)
print s[2][1]

# empty list
L = []
print len(L)