from math import*
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def distance_from_Xcoordinate(self):
        """
        This method finds the distance between a point and its X coordinates.

        Args:
            No
        Returns:
            float or int: distance.
        """
        return self.y
        
    def distance_from_Ycoordinate(self):
        """
        This method finds the distance between a point and its Y coordinates.

        Args:
            No
        Returns:
            float or int: distance.
        """
        return self.x

    def getQuadrant(self):
        """
        This method finds which quadrant the point is in.

        Args:
            No
        Returns:
            int: quadrant.
        """
        if self.x>0 and self.y>0:
            return "I"
        elif self.x<0 and self.y>0:
            return "II"
        elif self.x<0 and self.y<0:
            return "III"
        elif self.x>0 and self.y<0:
            return "IV"

    def on_Xcoordinate(self):
        """
        This method checks for a point on the X coordinate.

        Args:
            No
        Returns:
            bool: result.
        """
        return "X o'qda joylashgan..." if self.y else "Y o'qda joylashgan..."

    def on_Ycoordinate(self):
        """
        This method checks for a point on the Y coordinate.

        Args:
            No
        Returns:
            bool: result.
        """
        return "Y o'qda joylashgan..." if self.x else "X o'qda joylashgan..."
a= Point(30,273)
print(a.getQuadrant())