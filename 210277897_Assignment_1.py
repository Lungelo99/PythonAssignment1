str = 'fullstackslp'

#Using index to print characters
# 'f'

print(str[0])

# 'p'

print(str[-1])

# 'stack'

print(str[4:9])

# 'cks'

print(str[-5:10])

#Bonus: Use the indexing to reverse the string

x = 11
st = ''
while x >= 0:
    st = st + str[x]
    x = x - 1
print()
print(st)
print()

#Problem 2

l = [3,7,[5,[1,4,'hello']]]

print(l)
l[2][1][2] = 'goodbye'

print(l)

#Problem 3

#Problem 3.1
d1 = {'simple_key': 'hello'}

print()
print(d1['simple_key'])

#Problem 3.2
d2 = {'key1': {'key2': 'hello'}}

print()
print(d2['key1']['key2'])

#Problem 3.3

d3 = {'key1':[{'nest_key':['this is deep',['hello']]}]}

print()
print(d3['key1'][0]['nest_key'][1][0])



#Problem 4

my_list = [1,1,1,1,1,2,2,2,2,3,3,3,3]

unique_items = set(my_list)

print()
print(unique_items)

#Problem 5

name = "Kyle"
age = 45 
str = "Hello my dog's name is {} and he looks {} years old".format(name,age)

print()
print(str)

