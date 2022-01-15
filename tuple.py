'''STUDENT NAME:DRASHTI PATEL
   STUDENT ID:20cs049
  #1.Python program to create a tuple with different data types.'''
  
# create tuple with name features
features = ('goodlooking',19,45.6,False)
#print the tuple
print(features)

#2. Python program to create a tuple with numbers and print one item.
# create tuple with name age consisting 4 ages
age = (7,9,34,10)
#printing one item from the tuple named age
print(age[2])

#3.Python program to add an item in a tuple.
new_age =(17,)
# storing newly added age in old tuple and naming it age2
age2 = age+new_age
#printing new tuple named age2
print(age2)

#4.Python program to convert a tuple to a string.
#creating tuple named word
word = ('h','e','l','l','o')
# Using str.join() to convert tuple to string.
str = ''.join(word)
#print statement
print (str)

#5.Python program to find the length of a tuple.
names = ('riya','siya','diya','kiya')
print(names)
#print length of tuple
print(len(names))
