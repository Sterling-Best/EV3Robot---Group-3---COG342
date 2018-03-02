from src.Ev3Grid.Ev3Coordinates import Ev3Coordinates
from src.Ev3Grid.Ev3Region import Ev3Region

class Ev3Global:
    """
    Contains all regions and coordinates during a robot's run.
    """

    globalCoordinate: list

    __regionSize: int

    def __init__(self, a_targetsize: int) -> None:
        """

        """
        self.globalCoordinate = []
        self.__regionSize = a_targetsize

    #TODO: regionSize get and set
    def get_regionsize(self) -> int:
        """
        Returns self.__regionSize current interger value

        Returns:
            int: The current value of self.__regionSize

        Doctests:
        >>> aG = Ev3Global(8)
        >>> aG.get_regionsize()
        8
        """
        return self.__regionSize

    #TODO: Create add coordinate
    def addcoord(self, a_targetcoord: Ev3Coordinates) -> None:
        """
        Adds an Ev3Coordinate to Global grid system. First determining if there is already a region it belong, and if so puts it there, and if not create a region for it.

        Args:
            a_targetcoord (Ev3Coordinates): Target Ev3Coordinates to be added to global grid

        Returns:
            None: Ev3Coordinate is added to the Global grid.

        Doctest:
        >>> aG = Ev3Global(16)
        >>> print(aG)
        <16 | []>
        >>> aC = Ev3Coordinates(2,4)
        >>> aG.addcoord(aC)
        >>> print(aG)
        <16 | [{0,0,15,15 | [(2,4)]}]>
        >>> bC = Ev3Coordinates(12,8)
        >>> cC = Ev3Coordinates(-5,-7)
        >>> dC = Ev3Coordinates(0,0)
        >>> aG.addcoord(bC)
        >>> aG.addcoord(cC)
        >>> aG.addcoord(dC)
        >>> print (aG)
        <16 | [{-16,-16,-1,-1 | [(-5,-7)]}, {0,0,15,15 | [(0,0), (2,4), (12,8)]}]>
        """
        if len(self.globalCoordinate) == 0:
            newregion = Ev3Region(a_targetcoord, self.get_regionsize())
            self.globalCoordinate.append(newregion)
        else:
            for region in self.globalCoordinate:
                if region.doescoordbelong(a_targetcoord):
                    region.addcoord(a_targetcoord)
                    break
                elif self.globalCoordinate.index(region) == len(self.globalCoordinate) - 1:
                    self.globalCoordinate.append(Ev3Region(a_targetcoord, self.get_regionsize()))
                    break
        self.globalCoordinate.sort()

    def sort(self) -> None:
        """
        Sort the regions within globalCoordinates from those with the least values to greatest based on

        Returns:
            None: Sorts regions in globalCoordinates from least to greatest

        >>> aG = Ev3Global(8)
        >>> aC = Ev3Coordinates(5,7)
        >>>

        """
        newlist = []
        if len(self.globalCoordinate) == 1:
            newlist.append(self.globalCoordinate[0])
        else:
            for region in self.globalCoordinate:
                if len(newlist) == 0:
                    newlist.append(region)
                else:
                    for item in newlist:
                        if item > region:
                            newlist.insert(newlist.index(item), region)
                            break
                        elif region > item and newlist.index(item) == len(
                                newlist) - 1:
                            newlist.append(region)
                            break
        self.globalCoordinate = newlist

    #TODO: Create add region

    #TODO: Create region search/return

    #TODO: Create Export csv file

    #TODO: Create collect all coordinates

    #TODO: Optional: Modify region size
    #Goes through all regions modifying their borders, and reassigning coordinates
    #This will bye tough

    #TODO: Create __str__
    def __str__(self) -> str:
        """
        Generates string representation of Ev3Global

        Returns:
            str: String representation of Ev3Global

        Doctests
        >>> aG = Ev3Global(16)
        >>> print(aG)
        <16 | []>
        """
        gstring = "<" + str(self.get_regionsize()) +  " | ["
        if len(self.globalCoordinate) == 0:
            gstring = gstring + "]"
        elif len(self.globalCoordinate) >= 1:
            for region in self.globalCoordinate:
                gstring = gstring + str(region)
                if self.globalCoordinate.index(region) == len(self.globalCoordinate) - 1:
                    gstring = gstring + ']'
                else:
                    gstring = gstring + ', '
        return gstring + ">"

if __name__ == "__main__":
    import doctest
    doctest.testmod()
