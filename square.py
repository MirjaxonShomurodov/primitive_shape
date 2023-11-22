from polygon import Polygon

class Square(Polygon):
    def __init__(self, height, width) -> None:
        super().__init__(height, width)
    
    def get_proof(self)->int:

        if (self.height<0 or self.width>0) and (self.height>0 or self.width<0) and (self.height==self.width):
            return True
        else:
            return False


    def get_arrey(self)->int:

        S=self.height*self.width

        return S
    
    def get_Perimeter(self,height:int)->int:
        super().__init__(height,height)

        return 4*self.height
sum = Square(5,3)
print(sum.get_proof())