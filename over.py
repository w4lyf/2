class Base:
    def method(self, x=None):
        if x is None:
            print("Base method without arguments")
        else:
            print("Base method with argument:", x)

class Derived(Base):
    def method(self, x=None):
        if x is None:
            print("Derived method without arguments")
        else:
            print("Derived method with argument:", x)

if __name__ == "__main__":
    obj_base = Base()
    obj_base.method()      
    obj_base.method(10)    

    obj_derived = Derived()
    obj_derived.method()      
    obj_derived.method(20)   
