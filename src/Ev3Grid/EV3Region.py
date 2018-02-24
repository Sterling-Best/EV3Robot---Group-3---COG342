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
        self.__yMax = self.__yMin + targetregionsize - 1
        self.regionCoordinates = list()
        self.regionCoordinates.append(targetcoordinates)

    #TODO: Add get_ and set_ methods for __xMax, __xMin, __yMax, __yMin

    def get_xmin(self) -> int:
        #TODO: Create Unittests
        """
        Returns current value of self.__xMin

        Returns:
            int: Current value of self.__xMin

        Doctest:
        >>> aC = Ev3Coordinates.Ev3Coordinates(4,6)
        >>> aR = EV3Region(aC, 8)
        >>> print(aR)
        {0,0,7,7 | [(4,6)]}
        >>> aR.get_xmin()
        0
        """
        return self.__xMin

    def get_xmax(self) -> int:
        # TODO: Create Unittests
        """
        Returns current value of self.__xMax

        Returns:
            int: Current value of self.__xMax

        Doctest:
        >>> aC = Ev3Coordinates.Ev3Coordinates(18,34)
        >>> aR = EV3Region(aC, 7)
        >>> print(aR)
        {14,28,20,34 | [(18,34)]}
        >>> aR.get_xmin()
        14
        """
        return self.__xMax

    def get_ymin(self) -> int:
        # TODO: Create Unittests
        """
        Returns current value of self.__yMin

        Returns:
            int: Current value of self.__yMin

        Doctest:
        >>> aC = Ev3Coordinates.Ev3Coordinates(103,84)
        >>> aR = EV3Region(aC, 16)
        >>> print(aR)
        {96,80,111,95 | [(103,84)]}
        >>> aR.get_ymin()
        80
        """
        return self.__yMin

    def get_ymax(self) -> int:
        # TODO: Create Unittests
        """
        Returns current value of self.__yMax

        Returns:
            int: Current value of self.__yMax

        Doctest:
        >>> aC = Ev3Coordinates.Ev3Coordinates(7,22)
        >>> aR = EV3Region(aC, 8)
        >>> print(aR)
        {0,16,7,23 | [(7,22)]}
        >>> aR.get_ymax()
        23
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

    def __str__(self) -> str:
        #TODO: Code Refacotr
        #Code works but its using str() references to compare objects ratherthan the objects themselfs. Should be fixed.
        #TODO: Create Unittests
        """
        Returns string representation of Ev3Regon

        Returns:
            str: '{' represention region. Followed by region boundaries, then a list of coordinates within the region.

        Doctest:
        >>> aC = Ev3Coordinates.Ev3Coordinates(4,5)
        >>> print(aC)
        (4,5)
        >>> aR = EV3Region(aC, 10)
        >>> print(aR)
        {0,0,9,9 | [(4,5)]}
        """
        regionborders = str(self.get_xmin()) + ',' + str(self.get_ymin()) + ',' + str(self.get_xmax()) + ',' + str(self.get_ymax())
        rcstring = '['
        for coord in self.regionCoordinates:
            if str(self.regionCoordinates[-1]) == str(coord):
                rcstring = rcstring + str(coord) + ']'
            else:
                rcstring = rcstring + str(coord) + ", "
        return '{' + regionborders + " | " + rcstring + '}'


if __name__ == "__main__":
    import doctest
    doctest.testmod()







