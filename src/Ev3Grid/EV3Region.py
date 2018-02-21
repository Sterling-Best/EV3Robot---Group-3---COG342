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

    def ifcoordlistin(self, targetcoordinateslist: list) -> bool:
        """

        Check to see if all EV3Coordinates in a list are within the region.

        Note: The reverse is not true, in that not all Ev3Coordinates in a region need to be in the list.

        :param targetcoordinateslist:
        :type targetcoordinateslist:
        :return:
        :rtype:
        """

        for targetcoord in targetcoordinateslist:
            if targetcoord not in self.regionCoordinates:
                return False
        return True



