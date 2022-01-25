#taking string input
str = input('')
newstring ='' 
  
for a in str: 
      
    # Checking for lowercase letter and 
    # converting to uppercase. 
    if (a.isupper()) == True: 
        newstring+=(a.lower()) 
          
    # Checking for uppercase letter and
    # converting to lowercase. 
    elif (a.islower()) == True: 
        newstring+=(a.upper()) 
    # adding it to the new string as it is. 
    else:
        newstring+= a 
         
print(newstring)
