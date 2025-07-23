"""#function defnition
def hello():
    print("welcome developers")
    
#function call
hello()"""

"""def display_name(name):
    print("my name is",name)
    
display_name("zaman")"""

"""def show_name(aname,bname):
    print(aname+" "+bname)
    
show_name("rohit","athul")"""

"""def show_list(list1):
    for item in list1:
        print(item)
show_list([4,6,"hello",7.5])"""

#positional arguments
"""def greet(name):
    print(f"hello,{name}!")
    
greet("rohit")"""

#default parameters
"""def greet(name="guest"):
    print(F"hello,{name}!")
    
greet()
"""
#keyword arguments
"""def show(c,d):
    print("value of c is",c,"\n" "value of d is",d)

show(c=10,d=7) """

#return funtion
"""def num(c,d):
    return c+d

result=num(5,3)
print(result)"""

#multiple return function
def num(c,d):
    return(c*d,c+d,c-d)

a,b,c=num(5,3)
print(a,b,c)