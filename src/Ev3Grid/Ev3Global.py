from src.Ev3Grid.Ev3Coordinates import Ev3Coordinates
from src.Ev3Grid.Ev3Region import Ev3Region

class Ev3Global:
    """
    Contains all regions and coordinates during a robot's run.
    """

    __globalCoordinate: list

    __regionSize: int

    def __init__(self) -> None:
        """

        """
        __globalCoordinate = []
        __regionSize = 16

    #TODO: Create add coordinate

    #TODO: Create add region

    #TODO: Create region search/return

    #TODO: Create Export csv file

    #TODO: Create collect all coordinates

    #TODO: Optional: Modify region size
    #Goes through all regions modifying their borders, and reassigning coordinates
    #This will bye tough


    #TODO: Create __str__


if __name__ == "__main__":
    import doctest
    doctest.testmod()
