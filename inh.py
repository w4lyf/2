
class A:
    def method_A(self):
        print("Method of class A")

class B(A):
    def method_B(self):
        print("Method of class B")

class C(B):
    def method_C(self):
        print("Method of class C")

class D(A):
    def method_D(self):
        print("Method of class D")

class E(C, D):
    def method_E(self):
        print("Method of class E")

if __name__ == "__main__":
    obj_e = E()
    obj_e.method_A()  
    obj_e.method_B()  
    obj_e.method_C()  
    obj_e.method_D() 
    obj_e.method_E()
