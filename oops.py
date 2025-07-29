"""class laptops:
    def spec(self):
        self.ram="4GB"
        self.model="lenovo"
        
lap1=laptops()
lap1.spec()
print(lap1.model)
print(lap1.ram)"""

"""class laptops:
    def spec(self,r,m):
        self.ram=r
        self.model=m
        
lap1=laptops()
lap2=laptops()
lap1.spec(r="4GB",m="lenovo")
lap2.spec(r="16GB",m="lenovo")

print(lap1.model)
print(lap2.ram)"""

"""class laptops():
    owner="zaman"
    def __init__(self,r,m):
        self.ram=r
        self.model=m
        
lap1=laptops(r="4GB",m="lenovo")
lap2=laptops(r="16GB",m="hp")
print(lap1.model)
print(lap2.ram)
print(laptops.owner)""" 

#inheritance
"""class Vehicles:
    def detail(self,make,power):
        self.make=make
        self.power=power  
            
class Car(Vehicles):
    def __init__(self,color,brand):
        self.color=color
        self.brand=brand   
c1=Car(color="blue",brand="bmw")
c1.detail(make="2004",power="500 rpm")
print(c1.color)
print(c1.power)"""



