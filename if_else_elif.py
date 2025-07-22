#if
"""age=18 
if age>=18:
  print("you are eligible to vote")"""
  
#if else
"""age=int(input("enter your age:"))
if age>=18:
    print("eligible")      #true
else:
    print("not eligible")"""    
    
#elif
"""x=int(input("enter a number:"))
if x>0:
    print("positive")
elif x<0:
    print("negative")
else:
    print("number is zero")
"""
#nested if
"""age=20
citizen=True
if age>=18:
    if citizen:
        print("you are eligible to vote")
    else:
        print("you must be a citizen to vote")
else:
    print("you are not old enough to vote")"""