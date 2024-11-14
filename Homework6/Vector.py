from __future__ import annotations
from math import sqrt
class Vector:
    def __init__(self,*args):
        self.args=list(args)

    def __str__(self):
        return f"Vector({', '.join(map(str, self.args))})"
    
    def __bool__(self):
        return any(self.args)
    
    def __add__(self,other):
        return Vector(*(a+b for a,b in zip(self.args, other.args)))
    
    def __sub__(self,other):
        return Vector(*(a-b for a,b in zip(self.args, other.args)))

    def __mul__(self,other):
        return Vector(*(a*b for a,b in zip(self.args, other.args)))

    def __eq__(self,other):
        return self.args==other.args
    
    def __len__(self):
        return len(self.args)
    
    def __getitem__(self, index):
        return self.args[index]
    
    def __abs__(self):
        return sqrt(sum(a**2 for a in self.args))
    
    def __neg__(self):
        return Vector(*(-a for a in self.args))
    
    def __setitem__(self,index,value):
        self.args[index] = value

v1 = Vector(1, 4, 6)

print(v1)

print(bool(v1))
print(bool(Vector(0, 0)))

print(len(v1))

v1[1]
v1[1] = 10
print(v1)

print('\n')

v2 = Vector(3, 7, 2)
print(v1 + v2)
print(v1 - v2)
print(v1 * v2)

print(abs(v1))

print(v1 == Vector(1, 10, 6))

print(-v1)