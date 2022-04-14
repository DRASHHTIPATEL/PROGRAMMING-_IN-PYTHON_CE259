# Creating a class Student.

class student:

Name = 'DRASHTI'

rollNumber = 49

# function to set the id & name

def details(self, rollNumber, Name):

self.Name = Name

self.rollNumber = rollNumber

# Creating a class exam from class student.

class exam(student):

marks_list = []

# function marks to set the marks of that student.

def marks(self, marks_list):

self.marks_list = marks_list

return marks_list

# Creating a class result from class exam.

class result(exam):

marks_gain = 0

# Function to obtain the total of the marks of a student.

def result_of_student(self, marks_gain):

total_marks = 0

for item in marks_gain:

total_marks += item

return total_marks

# Creating an object of result class.

sobj = result()

student_name = input("Enter the name of the student : ")

student_id = input("Enter the Roll Number of the student : ")

# Setting the details.

sobj.details(student_id, student_name)

print(f"Enter the marks of {student_name} in 6 subject : \n")

marks = []

for i in range(0, 6):

marks.append(int(input()))

# Setting the marks.

marks_obtain = sobj.marks(marks)

total = sobj.result_of_student(marks_obtain)

print(f"Total of {student_name} mark's is : {total}")
