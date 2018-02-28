class Ev3Coordinates:
    """
    Ev3Coordinates represent a point of x,y coordinates and the properties of that point.

    __xCoordinate: Represents an interger on the x axis
    __yCoordinates: Represents an interger on the y axis

    __propertyList: A list of strings that represent properties of the coordinates.
    """

    #TODO: Find Docstring Generator

    #Declares Class Variables
    #Coordinates
    __xCoordinate: int
    __yCoordinate: int
    #Property List
    __propertyList: list

    #Initializer
    def __init__(self, a_targetx : int, a_targety : int, *a_targetproperties: str):
        # TODO: Create Unittests
        """
        Inititialises a two interger graph point, x and y, for use of a 2D grid. X an Y must be integers.

        Target Properties (such as 'Point of Obstruction' or 'Point of Path') are optionally added as strings).

        Args:
            a_targetx (int): Desired value of self.__xCoordinate
            a_targety (int): Diesired value of self.__yCoordinate
            *a_targetproperties (str): String objects which represent prropeties/Attributes of the Coordinates.
                To beplaced in list

        Doctest:
        >>> a = Ev3Coordinates(2,4)
        >>> print(a)
        (2,4)
        >>> b = Ev3Coordinates(6,2, "Test1")
        >>> print(b)
        (6,2)
        >>> b.get_propertylist()
        ['Test1']
        """
        self.__xCoordinate = a_targetx
        self.__yCoordinate = a_targety
        self.__propertyList = []
        for tp in a_targetproperties:
            self.__propertyList.append(tp)

    #Variable Specific Functions
    #xCoordinate Specific Functions
    def get_xcoordinate(self) -> int:
        # TODO: Create Unittests
        """
        Returns __xCoordinate Value.

        Returns:
            int: Current value of self.__xCoordinate

        Doctest:
        >>> a = Ev3Coordinates(5,6)
        >>> a.get_xcoordinate()
        5
        """
        return self.__xCoordinate

    def set_xcoordinate(self, a_targetx : int) -> None:
        # TODO: Create Unittests
        """
        Sets xCoordinate to target value.

        Args:
            a_targetx (int): Desired value for self.__xCoordinate

        Returns:
            None: Replaces current value of self.__xCoordinate with a_targetx

        Doctest:
        >>> a = Ev3Coordinates(2,8)
        >>> a.set_xcoordinate(4)
        >>> a.get_xcoordinate()
        4
        """
        self.__xCoordinate = a_targetx

    #yCoordinate Specific Functions
    def get_ycoordinate(self) -> int:
        # TODO: Create Unittests
        """
        Returns yCoordinate Value

        Returns:
            int: Current value of self.__ycoordinate

        Doctest:
        >>> a = Ev3Coordinates(7,3)
        >>> a.get_ycoordinate()
        3
        """
        return self.__yCoordinate

    def set_ycoordinate(self, a_targety: int) -> None:
        # TODO: Create Unittests
        """
        Sets yCoordinate to target value.

        Args:
            a_targety (int): Desired value for self.__yCoordinate

        Returns:
            None: Replaces current value of self.__xCoordinate with a_targetx

        Doctest:
        >>> a = Ev3Coordinates(9,1)
        >>> a.set_ycoordinate(9)
        >>> a.get_ycoordinate()
        9
        """
        self.__yCoordinate = a_targety

    #propertyList Specfic Functions
    def get_propertylist(self) -> list:
        # TODO: Create Unittests
        """
        Returns propertyList

        Returns:
            list: List containing property strings

        Doctest:
        >>> a = Ev3Coordinates(1,1,"Test1")
        >>> a.get_propertylist()
        ['Test1']
        >>> b = Ev3Coordinates(2,2,"Test2","Test3")
        >>> b.get_propertylist()
        ['Test2', 'Test3']
        """
        return self.__propertyList

    def set_properylist(self, a_targetlist: list) -> None:
        # TODO: Create Unittests
        """
        Sets propertyList to new targetList

        Args:
            a_targetlist (list): Disired list of propety strings to replace self.__propertyList

        Returns:
            None: Replaces value of self.__propertyList with a_targetlist

        Doctest:
        >>> a = Ev3Coordinates(1,1,"Test1")
        >>> a.get_propertylist()
        ['Test1']
        >>> a.set_properylist(['Test2'])
        >>> a.get_propertylist()
        ['Test2']
        """
        self.__propertyList = a_targetlist

    def add_property_propertylist(self, *a_targetproperties: str) -> None:
        # TODO: Create Unittests
        """
        Adds property strings to the target property list

        Args:
            *a_targetproperties (str): Strings that are to be added to self.__propertyList

        Returns:
            None: Appends property strings to self.__propertyList

        Doctest:
        >>> a = Ev3Coordinates(1,1,"Test1")
        >>> a.get_propertylist()
        ['Test1']
        >>> a.add_property_propertylist("Test2")
        >>> a.get_propertylist()
        ['Test1', 'Test2']
        """
        for tp in a_targetproperties:
            self.__propertyList.append(tp)

    def remove_property_propertylist(self, a_targetproperty : str) -> None:
        # TODO: Create Unittests
        """
        Finds and removes target property from property list.

        Args:
            a_targetproperty (str): String to find and remove with self.__propteryList

        Returns:
            None: Modifies self._propteryList be removing indicated (a_targetporptery) from self.__propertyList)

        Doctest:
        >>> a = Ev3Coordinates(1,1,"Test1","Test2")
        >>> a.get_propertylist()
        ['Test1', 'Test2']
        >>> a.remove_property_propertylist("Test2")
        >>> a.get_propertylist()
        ['Test1']
        """
        if a_targetproperty in self.__propertyList:
            self.__propertyList.remove(a_targetproperty)


    #Rich Comparisons < , <= , == , >=, >

    def __lt__ (self, a_other: 'Ev3Coordinates') -> bool:
        # TODO: Create Unittests
        """
        <
        Returns whether other (x,y) are less than vales of self.

        Args:
            a_other (Ev3Coordinates): Ev3Coordinate being compared to self.

        Returns:
            bool: True if self is less than a_other.

        Doctest:
        >>> a = Ev3Coordinates(1,1)
        >>> b = Ev3Coordinates(1,2, "Test1")
        >>> a < b
        True
        >>> b < a
        False
        """
        if self.get_xcoordinate() < a_other.get_xcoordinate() and self.get_ycoordinate() < a_other.get_ycoordinate():
            return True
        elif self.get_xcoordinate() == a_other.get_xcoordinate() and self.get_ycoordinate() < a_other.get_ycoordinate():
            return True
        else:
            return False

    def __le__(self, a_other: 'Ev3Coordinates') -> bool:
        # TODO: Create Unittests
        """
        <=
        Returns whether other (x,y) are less or equal to vales of self.

        Args:
            a_other (Ev3Coordinates): Ev3Coordinate being compared to self.

        Returns:
            bool: True if this coordinate is less than or equal other coordinate. False if greater than.

        Doctest:
        >>> a = Ev3Coordinates(5,5)
        >>> b = Ev3Coordinates(5,5, "Test1")
        >>> c = Ev3Coordinates(4,2)
        >>> d = Ev3Coordinates(5,3, "Test2", "Test3")
        >>> a <= b
        True
        >>> b <= a
        True
        >>> a <= c
        False
        >>> c <= a
        True
        >>> a <= d
        False
        >>> d <= a
        True
        """
        if self.get_xcoordinate() <= a_other.get_xcoordinate() and self.get_ycoordinate() <= a_other.get_ycoordinate():
            return True
        else:
            return False

    def __eq__(self, a_other: 'Ev3Coordinates') -> bool :
        # TODO: Create Unittests
        """
        ==
        What to compare when determining whether an Ev3Coordinate object is equal to target object.
        Args:
            a_other (Ev3Coordinates): Ev3Coordinate being compared to self.

        Returns:
            bool: True if value of a_other are the same as self.

        Doctest:
        >>> a = Ev3Coordinates(1,1)
        >>> b = Ev3Coordinates(1,1, "Test1")
        >>> c = Ev3Coordinates(1,2)
        >>> d = Ev3Coordinates(2,2, "Test2")
        >>> a == b
        True
        >>> a == c
        False
        >>> a == d
        False
        >>> aC = Ev3Coordinates(4,5)
        >>> bC = Ev3Coordinates(4,5)
        >>> aC == bC
        True
        """
        if not isinstance(a_other, Ev3Coordinates):
            return False
        elif self.get_xcoordinate() == a_other.get_xcoordinate() and self.get_ycoordinate() == a_other.get_ycoordinate():
            return True
        else:
            return False

    def __ne__(self, a_other: 'Ev3Coordinates') -> bool:
        #TODO: Create Unittests
        """
        !=
        Determine whether two Ev3Coordinates objects were equal.
        Args:
            a_other (Ev3Coordinates): Ev3Coordinate being compared to self.

        Returns:
            bool: True if value of a_other is not the same as self.

        Doctest:
        >>> a = Ev3Coordinates(1,1)
        >>> b = Ev3Coordinates(1,1, "Test1")
        >>> c = Ev3Coordinates(1,2)
        >>> d = Ev3Coordinates(2,2, "Test2")
        >>> a != b
        False
        >>> a != c
        True
        >>> a != d
        True
        """
        if not isinstance(a_other, Ev3Coordinates):
            return True
        elif self.get_xcoordinate() == a_other.get_xcoordinate() and self.get_ycoordinate() == a_other.get_ycoordinate():
            return False
        else:
            return True

    def __ge__(self, a_other: 'Ev3Coordinates') -> bool :
        # TODO: Create Unittests
        """
        >=
        Returns whether target coordinates is great or equal to (x,y) values than self.

        Args:
            a_other (int): Ev3Coordinate being compared to self.

        Returns:
            bool: True if self is greater than or equal to target Ev3Coordinate

        Doctest:
        >>> a = Ev3Coordinates(5,5)
        >>> b = Ev3Coordinates(5,5, "Test1")
        >>> c = Ev3Coordinates(4,2)
        >>> d = Ev3Coordinates(5,3, "Test2", "Test3")
        >>> a >= b
        True
        >>> b >= a
        True
        >>> a >= c
        True
        >>> c >= a
        False
        >>> a >= d
        True
        >>> d >= a
        False
        """
        if self.get_xcoordinate() >= a_other.get_xcoordinate() and self.get_ycoordinate() >= a_other.get_ycoordinate():
            return True
        else:
            return False

    def __gt__(self, a_other: 'Ev3Coordinates') -> bool:
        # TODO: Create Unittests
        """
        >
        Returns whether target coordinates is great (x,y) values than self.

        Args:
            a_other (Ev3Coordinates): Ev3Coordinate being compared to self.

        Returns:
            bool: True if self is greater than target Ev3Coordinates

        Doctest:
        >>> a = Ev3Coordinates(1,1)
        >>> b = Ev3Coordinates(1,2, "Test1")
        >>> a > b
        False
        >>> b > a
        True
        >>> c = Ev3Coordinates(5,13)
        >>> d = Ev3Coordinates(14,2)
        >>> d > c
        True
        >>> c > d
        False
        """
        if self.get_xcoordinate() > a_other.get_xcoordinate():
            return True
        elif self.get_xcoordinate() == a_other.get_xcoordinate() and self.get_ycoordinate() > a_other.get_ycoordinate():
            return True
        else:
            return False

    #String Representations of Ev3Coordinates Class

    def __str__(self) -> str :
        # TODO: Create Unittests
        """
        String Representation of Ev3Coordinate object

        Returns:
            str: String representation of EV3Coordinate object

        Doctest:
        >>> a = Ev3Coordinates(5,6)
        >>> print(a)
        (5,6)
        >>> b = Ev3Coordinates(-6, -4)
        >>> print(b)
        (-6,-4)
        >>> c = Ev3Coordinates(7, -9)
        >>> print(c)
        (7,-9)
        """
        return '(' + str(self.get_xcoordinate()) + ',' + str(self.get_ycoordinate()) + ')'

#When running Ev3Coordinates.py directly from file, doctests will run.
if __name__ == "__main__":
    import doctest
    doctest.testmod()
