#create list named lst
lst = []
#taking n inputs
n = int(input(" "))
for i in range(0, n):
    item = int(input())
    #adding items to list
    lst.append(item)
print(lst)
#sorting the list lst in ascending order
lst.sort()
#converting list to set
converted_set = set(lst)
#printing the set 
print(converted_set)
new=list(converted_set)
#printing the new converted list 
print(new)
#printing second last number
print(new[len(new)-2])
