from src.Ev3Grid import Ev3Coordinates as Ev3Coordinates

class EV3Region:
    """
    A section/region of the world grid. Storing specific
    """

    # TODO: Convert to Google Style Docstrings -- http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
    # TODO: Add docstring tests
    # TODO: Find Docstring Generator

    __xMax: int
    __xMin: int
    __yMax: int
    __yMin: int

    regionCoordinates: list

    def __init__(self, targetcoordinates : Ev3Coordinates, targetregionsize: int):
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        # TODO: Create Unittests
        """
        Initiates a Region with a first coordinate.

        Args:
            targetcoordinates (Ev3Coordinates): First Ev3Coordinate for the region
            targetregionsize (int): Size of the region that determines what coordinates should be put inside it.

        >>> aC = Ev3Coordinates.Ev3Coordinates(0,0)
        >>> aR = EV3Region(aC, 10)
        >>> aR.get_xmin()
        0
        >>> aR.get_xmax()
        9
        >>> aR.get_ymin()
        0
        >>> aR.get_xmax()
        9
        """
        self.__xMin = ((targetcoordinates.get_xcoordinate() // targetregionsize) * targetregionsize)
        self.__xMax = self.__xMin + targetregionsize  - 1
        self.__yMin = ((targetcoordinates.get_ycoordinate() // targetregionsize) * targetregionsize)
        self.__yMax = self.__xMin + targetregionsize - 1
        self.regionCoordinates = list()
        self.regionCoordinates.append(targetcoordinates)

    #TODO: Add get_ and set_ methods for __xMax, __xMin, __yMax, __yMin

    def get_xmin(self) -> int:
        #TODO: Create Doctests
        #TODO: Create Unittests
        """
        Returns current value of self.__xMin

        Returns:
            int: Current value of self.__xMin

        """
        return self.__xMin

    def get_xmax(self) -> int:
        # TODO: Create Doctests
        # TODO: Create Unittests
        """
        Returns current value of self.__xMax

        Returns:
            int: Current value of self.__xMax

        """
        return self.__xMax

    def get_ymin(self) -> int:
        # TODO: Create Doctests
        # TODO: Create Unittests
        """
        Returns current value of self.__yMin

        Returns:
            int: Current value of self.__yMin

        """
        return self.__yMin

    def get_ymax(self) -> int:
        # TODO: Create Doctests
        # TODO: Create Unittests
        """
        Returns current value of self.__yMax

        Returns:
            int: Current value of self.__yMax

        """
        return self.__yMax


    def ifcoordin(self, target: Ev3Coordinates) -> bool:
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        # TODO: Create Unittests
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
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        # TODO: Create Unittests
        """

        Check to see if all EV3Coordinates in a list are within the region. If even one Ev3Coordinates object is not
        found, the method will return false.

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

    def addcoord(self, targetcoord: Ev3Coordinates):
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        # TODO: Create Unittests
        """
        Adds an Ev3Coordinates object to regionCoordinates list. Organizes the coordinate to fit in X, Y organizational structure.

        :param targetcoord:
        :type targetcoord:
        :return:
        :rtype:
        """
        if self.regionCoordinates is not None or not self.regionCoordinates:
            for rc in self.regionCoordinates:
                if rc == targetcoord:
                    break
                elif rc < targetcoord:
                    self.regionCoordinates.insert(self.regionCoordinates.index(rc), targetcoord)

if __name__ == "__main__":
    import doctest
    doctest.testmod()







