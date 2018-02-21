from src.Ev3Grid import Ev3Coordinates

class EV3Region:
    """
    A section/region of the world grid. Storing specific
    """

    xMax: int
    xMin: int
    yMax: int
    yMin: int

    regionCoordinates: list

    def __init__(self, targetcoordinates : Ev3Coordinates, targetregionsize: int):
        """
        Initiates a Region with a first coordinate.

        :param targetCoordinates:
        :type targetCoordinates:
        """
        self.xMin = (targetcoordinates.get_xcoordinate() // targetregionsize) * targetregionsize
        self.xMax = self.xMin + targetregionsize
        self.yMin = (targetcoordinates.get_ycoordinate() // targetregionsize) * targetregionsize
        self.yMax = self.xMin + targetregionsize
        self.regionCoordinates.append(targetcoordinates)

    def coordinatesInRegion(self, targets):
