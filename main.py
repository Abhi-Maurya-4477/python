list_1 = ["ram", 1 ,2.0 , True]
print(list_1)

tuple_1 = (1,2,3,4)
print(tuple_1)

dict_1 = {"name" : "ram" }

print(dict_1)

set_1 = {1 , 2 , 3 ,4  }
print(set_1)

class New:
    
    #class variables 
    college = "GGI"
    
    def __init__(self, name, roll_no):
        #instace variable 
        self._name = name 
        self.roll_no = roll_no
        
    def display(self):
        print(self.__name)
        print(self.roll_no)
    
    


obj = New("sita", 2)
obj.display()
print(obj.roll_no)  # public variable
print(obj._name)    # protected variable

class A:
    pass

class B(A):
    pass

class C(B):
    pass



class D ( A , B ):
    pass

class D ( B, A):
    pass



