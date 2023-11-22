from polygon import Polygon

class Rectangle(Polygon):
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width
    def get_Proof(self):
        if (self.height<0 or self.width>0) and (self.height>0 or self.width<0) :
            return True
        else:
            return False

    def get_Array(self)->int:
        S = self.height*self.width

        return S
    def get_Perimeter(self)->int:
        
        P = 2*(self.height+self.width)

        return P
    
sum = Rectangle(-4,4)
print(sum.get_Proof())