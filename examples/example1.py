from constant_properties_protector import CPP

class A:
    def __init__(self):
        CPP.protect(self, 'initialized_protected')
        CPP.protect(self, 'uninitialized_protected')
        self._initialized_protected = 12
        
a = A()
print(a.initialized_protected)
# >>> 12
a.t = 2
print(a.t)
# >>> 2
a.initialized_protected += 1
# Exception: Can not modify constant property: initialized_protected
a.uninitialized_protected = 10
# Exception: Can not modify constant property: uninitialized_protected

class B(A):
    def __init__(self):
        super().__init__()
        CPP.protect(self, 'new_protected_value')
        self._new_protected_value = 26

b = B()
print(b.new_protected_value)
# >>> 26
b.new_protected_value += 2
# Exception: Can not modify constant property: new_protected_value