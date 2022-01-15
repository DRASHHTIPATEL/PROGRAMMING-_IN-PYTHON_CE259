""" Student ID: 20CS049
    Student Name : Drashti Patel 
"""
#1.Python script to check whether a given key already exists in a dictionary.

#create dictionary named Student with keys as below
Student = {
    'ID' : '20cs049',
    'first_Name' : 'Drashti',
    'last_Name' : 'Patel',
    'Age' : 19,
    'Gender' : 'Female',
    'skills' : ['Python', 'CSS', 'Django','ruby']
}
#print the dictionary created above
print(Student)

#check whether the key is present or not in the dictionary called Student
def is_key_present(x):
    if x in Student:
        print('Key is present')
    else:
        print('Key is not present')
is_key_present('skills') 
is_key_present('Gender') 

#2.  Python script to merge two Python dictionaries.

#defining merge function to join two dictionaries
def Merge(rollno1, rollno2):
    return(rollno2.update(rollno1))
    #create dictionary named rollno1
rollno1 = { 
    'Disha': 98,
    'Harsh' : 99,
    'Drashti' : 98,
    'Mohit': 99,
    'Anuj' : 98
} 
#Dictionary named rollno2
rollno2 = { 
    'Harshiv': 98,
    'Dev' : 99,
    'Darsh' : 98,
    'Khushi': 99,
    'Shubhangi' : 98
} 

# print statemnt to merge 2 dictionaries
print(Merge(rollno1, rollno2))
 
# changes made in dictionary 2
print(rollno2)

# 3.Python program to sum all the items in a dictionary.
Data = {
    'd1' : 100,
    'd2' : 200,
    'd3' : 200,
    'd4' : 100,
    'd5' : 100
}
print(Data)
#printing the sumof all data values.
print(sum(Data.values()))

#4. Python script to add a key to a dictionary.
Student['skills'].append('cpp')
#print the new updated dictionary whichhas cpp included in it
print(Student)

#5.Python script to concatenate following dictionaries to create a new one.
items = {
    'cup' : 10,
    'spoons': 20,
    'plates' : 30
}
vegetables = {
    'carrot': 200,
    'potato': 250,
    'onion': 160
}
fruits = {
    'apple' : 270,
    'banana': 180,
    'litchi': 300
}
#It will concatenate the above dictionaries and display it in Dict4.
total = {}
for d in (items, vegetables,fruits) : total.update(d)
print(total)
