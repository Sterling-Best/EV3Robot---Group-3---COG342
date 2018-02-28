from src.Ev3Grid.Ev3Coordinates import Ev3Coordinates

class Ev3Region:
    """
    A section/region of the world grid. Storing specific
    """

    # TODO: Find Docstring Generator

    __xMax: int
    __xMin: int
    __yMax: int
    __yMin: int

    #TODO: Convert regionCoordinates to 'private' variable
    regionCoordinates: list

    def __init__(self, targetcoordinates : Ev3Coordinates, targetregionsize: int):
        # TODO: Create Unittests
        """
        Initiates a Region with a first coordinate.

        Args:
            targetcoordinates (Ev3Coordinates): First Ev3Coordinate for the region
            targetregionsize (int): Size of the region that determines what coordinates should be put inside it.

        >>> aC = Ev3Coordinates(0,0)
        >>> aR = Ev3Region(aC, 10)
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

    def get_xmin(self) -> int:
        #TODO: Create Unittests
        """
        Returns current value of self.__xMin

        Returns:
            int: Current value of self.__xMin

        Doctest:
        >>> aC = Ev3Coordinates(4,6)
        >>> aR = Ev3Region(aC, 8)
        >>> print(aR)
        {0,0,7,7 | [(4,6)]}
        >>> aR.get_xmin()
        0
        """
        return self.__xMin

    def set_xmin(self, a_targetxmin: int) -> None:
        #TODO: Create UnitTests
        """
        Sets self.__xMin to the interger value of a_targetxmin.

        Args:
            a_targetxmin (int): Interger value that will replace current value of self._xMin

        Returns:
            None: Replaces value of self.__xMin with the value of a_targetxmin

        Doctest:
        >>> aC = Ev3Coordinates(4,6)
        >>> aR = Ev3Region(aC, 8)
        >>> print(aR)
        {0,0,7,7 | [(4,6)]}
        >>> aR.get_xmin()
        0
        >>> aR.set_xmin(1)
        >>> aR.get_xmin()
        1
        """
        self.__xMin = a_targetxmin

    def get_xmax(self) -> int:
        # TODO: Create Unittests
        """
        Returns current value of self.__xMax

        Returns:
            int: Current value of self.__xMax

        Doctest:
        >>> aC = Ev3Coordinates(18,34)
        >>> aR = Ev3Region(aC, 7)
        >>> print(aR)
        {14,28,20,34 | [(18,34)]}
        >>> aR.get_xmax()
        20
        """
        return self.__xMax

    def set_xmax(self, a_targetxmax: int) -> None:
        #TODO: Create Unittests
        """
        Replaces current self.__xMax value with interger value of a_targetxmax

        Args:
            a_targetxmax (int): Desired interger to replace value of self.__xMax

        Returns:
            None: Replaces current self.__xMax value with interger value of a_targetxmax

        Doctest:
        >>> aC = Ev3Coordinates(18,34)
        >>> aR = Ev3Region(aC, 7)
        >>> print(aR)
        {14,28,20,34 | [(18,34)]}
        >>> aR.get_xmax()
        20
        >>> aR.set_xmax(24)
        >>> aR.get_xmax()
        24
        """
        self.__xMax = a_targetxmax

    def get_ymin(self) -> int:
        # TODO: Create Unittests
        """
        Returns current value of self.__yMin

        Returns:
            int: Current value of self.__yMin

        Doctest:
        >>> aC = Ev3Coordinates(103,84)
        >>> aR = Ev3Region(aC, 16)
        >>> print(aR)
        {96,80,111,95 | [(103,84)]}
        >>> aR.get_ymin()
        80
        """
        return self.__yMin

    def set_ymin(self, a_targetymin: int) -> None:
        #TODO: Create Unittests
        """
        Replaces current self.__yMin value with interger value of a_targetymin

        Args:
            a_targetymin (int): Desired interger to replace value of self.__yMin

        Returns:
            None: Replaces current self.__yMin value with interger value of a_targetyMin

        Doctest:
        >>> aC = Ev3Coordinates(103,84)
        >>> aR = Ev3Region(aC, 16)
        >>> print(aR)
        {96,80,111,95 | [(103,84)]}
        >>> aR.get_ymin()
        80
        >>> aR.set_ymin(42)
        >>> aR.get_ymin()
        42
        """
        self.__yMin = a_targetymin

    def get_ymax(self) -> int:
        #TODO: Create Unittests
        """
        Returns current value of self.__yMax

        Returns:
            int: Current value of self.__yMax

        Doctest:
        >>> aC = Ev3Coordinates(7,22)
        >>> aR = Ev3Region(aC, 8)
        >>> print(aR)
        {0,16,7,23 | [(7,22)]}
        >>> aR.get_ymax()
        23
        """
        return self.__yMax

    def set_ymax(self, a_targetymax: int) -> None:
        #TODO: Create Unittests
        """
        Replaces current self.__yMax value with interger value of a_targetymax

        Args:
            a_targetymax (int): Desired interger to replace value of self.__yMax

        Returns:
            None: Replaces current self.__yMax value with interger value of a_targetyMax

        Doctest:
        >>> aC = Ev3Coordinates(7,22)
        >>> aR = Ev3Region(aC, 8)
        >>> print(aR)
        {0,16,7,23 | [(7,22)]}
        >>> aR.get_ymax()
        23
        >>> aR.set_ymax(13)
        >>> aR.get_ymax()
        13
        """
        self.__yMax = a_targetymax

    def simplecoordcheck(self, target: Ev3Coordinates) -> bool:
        # TODO: Create Unittests
        """
        Check to see if the target coordinates in questionare in this region.

        Args:
            target (Ev3Coordinates): Coordinates to be checke

        Returns:
            bool: True if target is found in self.regionCoordinates

        >>> aC = Ev3Coordinates(4,5)
        >>> bC = Ev3Coordinates(21,34)
        >>> aR = Ev3Region(aC, 8)
        >>> print(aR)
        {0,0,7,7 | [(4,5)]}
        >>> aR.simplecoordcheck(aC)
        True
        >>> aR.simplecoordcheck(bC)
        False
        """
        if target in self.regionCoordinates:
            return True
        else:
            return False

    def listcoordcheck(self, a_targetcoordinateslist: list) -> bool:
        # TODO: Create Unittests
        """
        Check to see if all EV3Coordinates in a list are within the region. If even one Ev3Coordinates object is not
        found, the method will return false.

        Note: The reverse is not true, in that not all Ev3Coordinates in a region need to be in the list.

        Args:
            a_targetcoordinateslist (list): List of Ev3Coordinates that should in in regionCoordinates

        Returns:
            bool: True if all Ev3Coordinates in target list are found within self.regionCoordinates

        Doctest:
        >>> aC = Ev3Coordinates(4,5)
        >>> bC = Ev3Coordinates(6,7)
        >>> cC = Ev3Coordinates(7,7)
        >>> aR = Ev3Region(aC, 8)
        >>> aR.addcoord(bC)
        >>> aR.addcoord(cC)
        >>> print(aR)
        {0,0,7,7 | [(4,5), (6,7), (7,7)]}
        >>> dC = Ev3Coordinates(4,5)
        >>> eC = Ev3Coordinates(7,7)
        >>> aC == dC
        True
        >>> aL = [dC,eC]
        >>> fC = Ev3Coordinates(8,4)
        >>> bL = aL + [fC]
        >>> aR.listcoordcheck(aL)
        True
        >>> aR.listcoordcheck(bL)
        False
        """
        for targetcoord in a_targetcoordinateslist:
            if targetcoord not in self.regionCoordinates:
                return False
        return True

    def doescoordbelong(self, a_targetcoord: Ev3Coordinates) -> bool:
        """
        Check to see if coord belong in this region, based on axis border values.

        Args:
            a_targetcoord (EV3Coordinates): Ev3Coordinate to be check if it is valid for current region

        Returns:
            bool: True if Ev3Coordinate is value for current region based on axis border values.

        Doctest:
        >>> aC = Ev3Coordinates(4,5)
        >>> bC = Ev3Coordinates(7,7)
        >>> cC = Ev3Coordinates(17,32)
        >>> dC = Ev3Coordinates(14, 21)
        >>> eC = Ev3Coordinates(21, 14)
        >>> aR = Ev3Region(aC, 16)
        >>> aR.doescoordbelong(bC)
        True
        >>> aR.doescoordbelong(cC)
        False
        >>> aR.doescoordbelong(dC)
        False
        >>> aR.doescoordbelong(eC)
        False
        """
        if self.get_xmin() <= a_targetcoord.get_xcoordinate() <= self.get_xmax():
            if self.get_ymin() <= a_targetcoord.get_ycoordinate() <= self.get_ymax():
                return True
            else:
                return False
        else:
            return False

    def addcoord(self, a_targetcoords: Ev3Coordinates) -> None:
        # TODO: Create Unittests
        """
                Adds an Ev3Coordinates object to regionCoordinates list. Organizes the coordinate to fit in X, Y organizational structure.

        {0,0,15,15 | [(4,12), (5,8), (5,13), (14,2)]}
        Args:
            a_targetcoords (Ev3Coordinates): Coordinate to add to self.regionCoordinates

        Returns:
            None: Adds new coordinate to self.regionCoordinates into proper place.

        Doctest:
        >>> aC = Ev3Coordinates(4,12)
        >>> bC = Ev3Coordinates(5,13)
        >>> cC = Ev3Coordinates(14,2)
        >>> dC = Ev3Coordinates(5,8)
        >>> aR = Ev3Region(aC, 16)
        >>> print (aR)
        {0,0,15,15 | [(4,12)]}
        >>> aR.addcoord(bC)
        >>> print(aR)
        {0,0,15,15 | [(4,12), (5,13)]}
        >>> aR.addcoord(cC)
        >>> print(aR)
        {0,0,15,15 | [(4,12), (5,13), (14,2)]}
        >>> aR.addcoord(dC)
        >>> print(aR)
        {0,0,15,15 | [(4,12), (5,8), (5,13), (14,2)]}
        """
        #TODO: Add exception if the coordinate is already in the region, or not valid for this region
        self.regionCoordinates.append(a_targetcoords)
        self.sort()

    def removecoord(self, a_targetcoord: Ev3Coordinates = None) -> None:
        """
        Removes indicated Ev3Coordinates from self.__regionCoordinates
        Args:
            a_targetcoord (Ev3Coordinates): Target coordinate to be found and removed

        Returns:
            None: Removes target Ev3Coordinate from self.regionCoordinates

        Doctest:
        >>> aC = Ev3Coordinates(2,4)
        >>> bC = Ev3Coordinates(6,7)
        >>> cC = Ev3Coordinates(0,0)
        >>> aR = Ev3Region(aC, 8)
        >>> aR.addcoord(bC)
        >>> aR.addcoord(cC)
        >>> print(aR)
        {0,0,7,7 | [(0,0), (2,4), (6,7)]}
        >>> aR.removecoord(Ev3Coordinates(2,4))
        >>> print(aR)
        {0,0,7,7 | [(0,0), (6,7)]}
        """
        #TODO: Raise exception if the Ev3Coordinates are not found
        if a_targetcoord in self.regionCoordinates:
            self.regionCoordinates.remove(a_targetcoord)

    def sort(self) -> None:
        """
        Sorts the self.regionCoordinates list in order of least to greatest

        Returns:
            None: Sorts self.regionCoordinates in order of least to greatest.

        Doctests:
        >>> aC = Ev3Coordinates(0,0)
        >>> aR = Ev3Region(aC, 8)
        >>> aR.sort()
        >>> print (aR)
        {0,0,7,7 | [(0,0)]}
        >>> bC = Ev3Coordinates(5,4)
        >>> aR.addcoord(bC)
        >>> cC = Ev3Coordinates(3,4)
        >>> aR.regionCoordinates.append(cC)
        >>> print (aR)
        {0,0,7,7 | [(0,0), (5,4), (3,4)]}
        >>> aR.sort()
        >>> print (aR)
        {0,0,7,7 | [(0,0), (3,4), (5,4)]}
        """
        newlist = []
        if len(self.regionCoordinates) == 1:
            newlist.append(self.regionCoordinates[0])
        else:
            for coord in self.regionCoordinates:
                if len(newlist) == 0:
                    newlist.append(coord)
                else:
                    for item in newlist:
                        if item > coord:
                            newlist.insert(newlist.index(item), coord)
                            break
                        elif coord > item and newlist.index(item) == len(
                            newlist) - 1:
                            newlist.append(coord)
                            break
        self.regionCoordinates = newlist

    #TODO: __lt__

    #TODO: __le__

    #TODO: __eq__
    def __eq__(self, a_other: 'Ev3Region') -> bool:
        """
        Compare self and another Ev3Region, and determine if they are equal, iff border values of region are the same.

        Args:
            a_other (Ev3Region): Ev3Region being compared.

        Returns:
            bool: True if all border vales of self and other Ev3Region are the same.

        Doctests:
        >>> aR = Ev3Region(Ev3Coordinates(2,3), 16)
        >>> bR = Ev3Region(Ev3Coordinates(7,9), 16)
        >>> cR = Ev3Region(Ev3Coordinates(21,26), 16)
        >>> aR == bR
        True
        >>> aR == cR
        False
        """
        if self.get_xmin() == a_other.get_xmin() and self.get_ymin() == a_other.get_xmin():
            if self.get_xmax() == a_other.get_xmax() and self.get_ymax() == a_other.get_ymax():
                return True
            else:
                return False
        else:
            return False

    #TODO: __ne__

    #TODO: __ge__

    #TODO: __gt__

    def __str__(self) -> str:
        #TODO: Create Unittests
        """
        Returns string representation of Ev3Regon

        Returns:
            str: '{' represention region. Followed by region boundaries, then a list of coordinates within the region.

        Doctest:
        >>> aC = Ev3Coordinates(4,5)
        >>> print(aC)
        (4,5)
        >>> aR = Ev3Region(aC, 10)
        >>> print(aR)
        {0,0,9,9 | [(4,5)]}
        """
        #TODO: Find out why rcstring assignments are throwing up formating erors
        regionborders = str(self.get_xmin()) + ',' + str(self.get_ymin()) + ',' + str(self.get_xmax()) + ',' + str(self.get_ymax())
        rcstring = '['
        if len(self.regionCoordinates) > 1:
            for coord in self.regionCoordinates:
                rcstring = rcstring + str(coord)
                if coord != self.regionCoordinates[-1]:
                    rcstring = rcstring + ', '
                else:
                    rcstring = rcstring + ']'
        else:
            rcstring = rcstring + str(self.regionCoordinates[0]) + ']'
        return '{' + regionborders + " | " + rcstring + '}'


if __name__ == "__main__":
    import doctest
    doctest.testmod()
