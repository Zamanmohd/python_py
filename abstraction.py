from abc import ABC,abstractmethod
class parent(ABC):
    @abstractmethod
    def fun(self):
       pass
       
class child(parent):
    def display(self):
        print("hi")
    def fun (self):
        print("abrstract method implementation")
        
ob=child()
ob.display()
ob.fun()