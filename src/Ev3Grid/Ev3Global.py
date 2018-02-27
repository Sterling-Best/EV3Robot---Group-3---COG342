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
