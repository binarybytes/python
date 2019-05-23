#lists can hold multiple items in it at once
#lists in python are zero-indexed = meaning the first item in them sits at position 0
my_list = ['a', 'b', 'c', 'd']

my_list[0]
#will print 'a'

my_list[2]
#will print 'c'

#tuples are a type of list that can't be changed once created
tuple_of_numbers = (1, 2, 3, 4, 5)

#dictionaries are a datatype that stores keys and values as '':''
phone_contact= { 'mom': '416-123-4567', 'dad': '647-765-4321'}
phone_contact['mom']
#will print '416-123'4567'

#control structures will let us execute code when the right conditions are met
#2 types of control structures we'll use = if statements and else statements
#if statements:
number = 20
if number > 10: #declare the if condition and END IT WITH A COLON
    print "thats a big number!" #whitespace matters in python - must be 4 spaces
#because it depends on the if statement, it's identented 4 times
#this should pring "thats a big number!"

#in if statements we'll use equality operators (greater than(>), less than (<), and greater than or equal to (>=),
#and equal to (==), this is a double equals sign because a single equals sign (=), is an assignment operator.)

#else statements we can use when our if statement turns out to not be true
number = 15
if number > 20:
    print "that's a big number"
  else: #colon 
    print "that's a small number" #indent 4 spaces because it depends on the if statement

#for loop = run thru an entire list, one at a time + do something with them
list_of_numbers = [1, 2, 3, 4, 5, 6, 7]
for numbers in list_of_numbers: #that colon tho
    print numbers #indent
#the for *variable_name* in list_of_numbers: refers to each item in the list
#can be called anything 
list_of_numbers = [a, b , c]
for bunnys in list_of_numbers:
    print bunnys

#functions are tools that can be used overxover again
#functions are like boxes
#they take input (arguments), perform operations on them, and give us output

#functions are always declared by the word 'def' (define), then the name of the function
#the name is then followed by a set of parentheses with the arguments
def multiple_by_two(x):
    return x * 2
multiply_by_two(3)
#will show 6
