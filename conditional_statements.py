name=(input("enter your name"))
age=(input("enter your age"))

if age>=18:
    print("{} can apply for pan card".format(name))
else:
    print("{} is eligible to apply for pan card".format(name))
    print("{} you can only apply when you become 18 years old")