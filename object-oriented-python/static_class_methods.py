class ToyClass:

    def instancemethod(self):
        return "instance method called", self

    @classmethod
    def classmethod(cls):
        return "class method called", cls

    @staticmethod
    def staticmethod():
        return "static method called"

obj = ToyClass()

print(obj.classmethod())
print(obj.instancemethod())
print(obj.staticmethod())
