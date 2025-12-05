"""
示例 doctest:
加法：：
>>>v1 = Vetor(2, 4)
>>>v2 = Vetor(2, 2)
>>>v1 + v2
Vetor(4, 6)
绝对值：：
>>>v = Vetor(3, 4)
>>>abs(v)
5.0
标量积：：
>>>v*3
Vetor(9, 12)
>>>abs(v)
15.0
"""
import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)