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

        :param targetcoordinates:
        :type targetcoordinates:
        """
        self.xMin = (targetcoordinates.get_xcoordinate() // targetregionsize) * targetregionsize
        self.xMax = self.xMin + targetregionsize
        self.yMin = (targetcoordinates.get_ycoordinate() // targetregionsize) * targetregionsize
        self.yMax = self.xMin + targetregionsize
        self.regionCoordinates.append(targetcoordinates)

    def ifcoordin(self, target: Ev3Coordinates) -> bool:
        """

        Check to see if the target coordinates in questionare in this region.

        :param target:
        :type target:
        :return:
        :rtype:
        """
        if target in self.regionCoordinates:
            return True
        else:
            return False



