#range:it is a buitin function range() returns an immutable sequence of numbers 
#used for looping specific no. of times
#datatype is range
#creating ranges
#the range function can be called with 1,2,or 3 arguments
#syntax:range(start,stop,step)

#call range() with one argument:the argument represents stop value
#start is optional if not provided it defaults to 0
#start is inclusive
#stop is exclusive
#step difference btw two nums
#Create a range of numbers from 0 to 9:
x=range(10)
print(x)#range(0, 10)
print(list(x))#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#call range() with two arguments:one is start,second is stop
#Create a range of numbers from 3 to 9:
x=range(3,10)
print(list(x))#[3, 4, 5, 6, 7, 8, 9]

#call range() with three arguments:third is step value
#Create a range of numbers from 3 to 9:
x=range(3,10,2)
print(list(x))#[3, 5, 7, 9]

#ranges are used in for loops to iterate over sequence of nums
#ex
for i in range(10):
    print(i)

#using list to display ranges
print(list(range(6)))
print(list(range(1,8)))
print(list(range(4,9,2)))

#slicing ranges:ranges can use slicing to extract a subsequence
r=range(18)
print(r[:10])
print(r[4])

#membership testing:ranges support membership testing with in operator
#Test if the numbers 6 and 7 are present in a range:
r=range(0,10,2)
print(7 in r)
print(9 in r)
print(2 in r)

#length:ranges supports len() to get no. of elements in the range
r=range(2,9)
print(len(r))#7
