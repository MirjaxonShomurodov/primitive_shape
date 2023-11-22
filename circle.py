class Circle:
    def __init__(self, r) -> None:
        self.r = r

    def getArea(self):
        pi=3.1415
        """
        This method finds the area of the Circle.

        Args:
            No
        Returns:
            float or int: result.
        """
        return self.r**2*pi

    def getLength(self):
        pi=3.1415
        """
        This method finds the length of the cirle.

        Args:
            No
        Returns:
            float or int: result..
        """
        return self.r*2*pi



sum = Circle(3)
print(sum.getLength())