class Ev3Coordinates:
    """
    Beep
    """

    #TODO: Convert to Google Style Docstrings -- http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
    #TODO: Finish docstring tests
    #TODO: Find Docstring Generator

    #Declares Class Variables
    #Coordinates
    __xCoordinate: int
    __yCoordinate: int
    #Property List
    __propertyList: list

    #Initializer
    def __init__(self, targetx : int, targety : int, *targetproperties: str):
        # TODO: Convert to Google Style Docstrings
        # TODO: Optional: Add more docstring tests
        # TODO: Create Unittests

        """
        Inititialises a two interger graph point, x and y, for use of a 2D grid. X an Y must be integers.
        Target Properties (such as 'Point of Obstruction' or 'Point of Path') are optionally added as strings).

        >>> a = Ev3Coordinates(2,4)
        >>> print(a)
        (2,4)
        >>> b = Ev3Coordinates(6,2, "Test1")
        >>> print(b)
        (6,2)
        >>> b.get_propertylist()
        ['Test1']

        :param targetx: Vertical
        :type targetx:
        :param targety:
        :type targety:
        :param targetproperty:
        :type targetproperty:
        """
        self.__xCoordinate = targetx
        self.__yCoordinate = targety
        self.__propertyList = []
        for tp in targetproperties:
            self.__propertyList.append(tp)

    #Variable Specific Functions
    #xCoordinate Specific Functions
    def get_xcoordinate(self) -> int:
        # TODO: Convert to Google Style Docstrings
        # TODO: Optional: Add more docstring tests
        # TODO: Create Unittests
        """
        Returns xCoordinate Value.

        >>> a = Ev3Coordinates(5,6)
        >>> a.get_xcoordinate()
        5

        :return:
        :rtype:
        """
        return self.__xCoordinate

    def set_xcoordinate(self, targetx : int):
        # TODO: Convert to Google Style Docstrings
        # TODO: Optional: Add more docstring tests
        # TODO: Create Unittests
        """
        Sets xCoordinate to target value.

        >>> a = Ev3Coordinates(2,8)
        >>> a.set_xcoordinate(4)
        >>> a.get_xcoordinate()
        4

        :param targetx:
        :type targetx:
        :return:
        :rtype:
        """
        self.__xCoordinate = targetx

    #yCoordinate Specific Functions
    def get_ycoordinate(self) -> int:
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        # TODO: Create Unittests
        """
        Returns yCoordinate Value

        >>> a = Ev3Coordinates(7,3)
        >>> a.get_ycoordinate()
        3

        :return:
        :rtype:
        """
        return self.__yCoordinate

    def set_ycoordinate(self, targety: int):
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        # TODO: Create Unittests
        """
        Sets yCoordinate to target value.

        >>> a = Ev3Coordinates(9,1)
        >>> a.set_ycoordinate(9)
        >>> a.get_ycoordinate()
        9

        :param targety:
        :type targety:
        :return:
        :rtype:
        """
        self.__yCoordinate = targety

    #propertyList Specfic Functions
    def get_propertylist(self) -> list:
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        # TODO: Create Unittests
        """
        Returns propertyList

        >>> a = Ev3Coordinates(1,1,"Test1")
        >>> a.get_propertylist()
        ['Test1']
        >>> b = Ev3Coordinates(2,2,"Test2","Test3")
        >>> b.get_propertylist()
        ['Test2', 'Test3']


        :return:
        :rtype:
        """
        return self.__propertyList

    def set_properylist(self, targetlist):
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        # TODO: Create Unittests
        """
        Sets propertyList to new targetList

        >>> a = Ev3Coordinates(1,1,"Test1")
        >>> a.get_propertylist()
        ['Test1']
        >>> a.set_properylist(['Test2'])
        >>> a.get_propertylist()
        ['Test2']

        :param targetlist:
        :type targetlist:
        :return:
        :rtype:
        """
        self.__propertyList = targetlist

    def add_property_propertylist(self, *targetproperties: str):
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        # TODO: Create Unittests
        """
        Adds property strings to the target property list

        >>> a = Ev3Coordinates(1,1,"Test1")
        >>> a.get_propertylist()
        ['Test1']
        >>> a.add_property_propertylist("Test2")
        >>> a.get_propertylist()
        ['Test1', 'Test2']

        :param targetproperties:
        :type targetproperties:
        :return:
        :rtype:
        """
        for tp in targetproperties:
            self.__propertyList.append(tp)

    def remove_property_propertylist(self, targetproperty : str):
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        # TODO: Create Unittests
        """
        Finds and removes target property from property list.

        >>> a = Ev3Coordinates(1,1,"Test1","Test2")
        >>> a.get_propertylist()
        ['Test1', 'Test2']
        >>> a.remove_property_propertylist("Test2")
        >>> a.get_propertylist()
        ['Test1']

        :param targetproperty:
        :type targetproperty:
        :return:
        :rtype:
        """
        if targetproperty in self.__propertyList:
            self.__propertyList.remove(targetproperty)


    #Rich Comparisons < , <= , == , >=, >

    def __lt__ (self, other) -> bool:
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        # TODO: Create Unittests
        """
        <
        Returns whether other (x,y) are less than vales of self.

        >>> a = Ev3Coordinates(1,1)
        >>> b = Ev3Coordinates(1,2, "Test1")
        >>> a < b
        True
        >>> b < a
        False

        :param other:
        :type other:
        :return:
        :rtype:
        """

        if self.get_xcoordinate() < other.get_xcoordinate() and self.get_ycoordinate() < other.get_ycoordinate():
            return True
        elif self.get_xcoordinate() == other.get_xcoordinate() and self.get_ycoordinate() < other.get_ycoordinate():
            return True
        else:
            return False

    def __le__(self, a_other: 'Ev3Coordinates') -> bool:
        # TODO: Create Unittests
        """
        <=
        Returns whether other (x,y) are less or equal to vales of self.

        Args:
            a_other (Ev3Coordinates):

        Returns:
            bool: True if this coordinate is less than or equal other coordinate. False if greater than.

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

    def __eq__(self, other) -> bool :
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        # TODO: Create Unittests
        """
        ==
        What to compare when determining whether an Ev3Coordinate object is equal to target object.

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

        :param other:
        :type other:
        :return:
        :rtype:
        """
        if self.get_xcoordinate() == other.get_xcoordinate() and self.get_xcoordinate() == other.get_ycoordinate():
            return True
        else:
            return False

    def __ge__(self, other) -> bool :
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        # TODO: Create Unittests
        """
        >=
        Returns whether target coordinates is great or equal to (x,y) values than self.

        :param other:
        :type other:
        :return:
        :rtype:
        """
        if self.get_xcoordinate() >= other.get_xcoordinate() and self.get_ycoordinate() >= other.get_ycoordinate:
            return True
        else:
            return False

    def __gt__(self, other) -> bool:
        # TODO: Convert to Google Style Docstrings
        # TODO: Add docstring tests
        # TODO: Create Unittests
        """
        >
        Returns whether target coordinates is great (x,y) values than self.

        :param other:
        :type other:
        :return:
        :rtype:
        """
        if self.get_xcoordinate() > other.get_xcoordinate() and self.get_ycoordinate() > other.get_ycoordinate:
            return True
        else:
            return False

    #String Representations of Ev3Coordinates Class

    def __str__(self) -> str :
        # TODO: Convert to Google Style Docstrings
        # TODO: Create Unittests
        """
        String Representation of Ev3Coordinate object

        >>> a = Ev3Coordinates(5,6)
        >>> print(a)
        (5,6)
        >>> b = Ev3Coordinates(-6, -4)
        >>> print(b)
        (-6,-4)
        >>> c = Ev3Coordinates(7, -9)
        >>> print(c)
        (7,-9)

        :return:
        :rtype:
        """
        return '(' + str(self.get_xcoordinate()) + ',' + str(self.get_ycoordinate()) + ')'

#When running Ev3Coordinates.py directly from file, doctests will run.
if __name__ == "__main__":
    import doctest
    doctest.testmod()
