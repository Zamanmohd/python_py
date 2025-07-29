class Parent1:
    def __init__(self):
        print("Parent1",self)
        print("Parent1 initialized")
        super().__init__()

class Parent2:
    def __init__(self):
        print("Parent2",self)
        print("Parent2 initialized")
        

class Child(Parent1, Parent2):
    def __init__(self):
        print("Child initialized")
        super().__init__()

obj = Child()
