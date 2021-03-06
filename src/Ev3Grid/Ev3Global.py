from src.Ev3Grid.Ev3Coordinates import Ev3Coordinates
from src.Ev3Grid.Ev3Region import Ev3Region
from src.Ev3Grid.Ev3CsvExporter import Ev3CsvExporter


class Ev3Global:
    """
    Contains all regions and coordinates during a robot's run.
    """

    globalCoordinate: list

    __regionSize: int

    ev3Exporter: Ev3CsvExporter

    def __init__(self, a_targetsize: int) -> None:
        """

        """
        self.globalCoordinate = []
        self.__regionSize = a_targetsize
        self.ev3Exporter = Ev3CsvExporter()

    # TODO: regionSize get and set
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

    # TODO: Create add coordinate
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

    def collectcoord(self) -> list:
        """
        Collects all coordinates in global grid and returns them.

        Returns:
            list: List of Ev3Coordinates that are currently in global grid.

        >>> aG = Ev3Global(16)
        >>> aG.addcoord(Ev3Coordinates(2,4))
        >>> aG.addcoord(Ev3Coordinates(0,0))
        >>> aG.addcoord(Ev3Coordinates(8,6))
        >>> aG.addcoord(Ev3Coordinates(-15,-12))
        >>> aG.addcoord(Ev3Coordinates(-18, 22))
        >>> aG.addcoord(Ev3Coordinates(13, -14))
        >>> aG.addcoord(Ev3Coordinates(42, 69))
        >>> print(aG)
        <16 | [{-32,16,-17,31 | [(-18,22)]}, {-16,-16,-1,-1 | [(-15,-12)]}, {0,-16,15,-1 | [(13,-14)]}, {0,0,15,15 | [(0,0), (2,4), (8,6)]}, {32,64,47,79 | [(42,69)]}]>
        >>> aTest = aG.collectcoord()
        >>> print(str(aTest))
        [(-18,22), (-15,-12), (13,-14), (0,0), (2,4), (8,6), (42,69)]
        """
        newlist = []
        for region in self.globalCoordinate:
            for coord in region.regionCoordinates:
                newlist.append(coord)
        return newlist

    # TODO: Optional: Modify region size
    # Goes through all regions modifying their borders, and reassigning coordinates
    # This will bye tough

    def exportcsv(self) -> None:
        """
        Exports csv of Ev3Coordinates using Ev3CsvExporter.

        Returns:
            None: Exports Ev3Coordinates in globalCoordinate as csv
        """
        self.ev3Exporter.createcsv(self)

    # TODO: Create __str__
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
        gstring = "<" + str(self.get_regionsize()) + " | ["
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
