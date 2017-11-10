# tuple

# it named tuple 
# it can't change and it don't have append() and insert()
# but you can get classmate[0] or classmate[1]
classmates = ('Michael', 'Bob', 'Tracy')

print classmates[0]
print classmates[1]
print classmates

# the empty t = ()

# some time we use (1) like 1, it like the same,so we use (1,) to make difference
t = (1,)

print t

# the list in a tuple
t = ('a', 'b', ['A', 'B'])
print t
t[2][0] = 'X'
t[2][1] = 'Y'
print t