from polygon import Polygon
from math import*
class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def get_proot(self)->int:
        if self.a+self.b>self.c or self.a+self.c>self.b or self.b+self.c>self.a:
            return True
        else:
            return False
    def get_arr(self):

        p = (self.a+self.b+self.c)/2

        S = sqrt(p*(self.a+p)*(self.b+p)*(self.c+p)) 

        return S
    def get_permetr(self):

        P = self.a+self.b+self.c

        return P
triangle = Triangle(2,3,4)
print(triangle.get_arr())