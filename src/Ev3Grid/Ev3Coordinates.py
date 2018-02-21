class Ev3Coordinates:
    """
    Beep
    """

    #Declares Class Variables
    #Coordinates
    xCoordinate: int
    yCoordinate: int
    #Property List
    propertyList: list

    #Initializer
    def __init__(self, targetx : int, targety : int, *targetproperties: str):
        """
        Inititialises a two interger graph point, x and y, for use of a 2D grid. X an Y must be integers.
        Target Properties (such as 'Point of Obstruction' or 'Point of Path') are optionally added as strings).

        :param targetx: Vertical
        :type targetx:
        :param targety:
        :type targety:
        :param targetproperty:
        :type targetproperty:
        """
        self.xCoordinate = targetx
        self.yCoordinate = targety
        self.propertyList = []
        for tp in targetproperties:
            self.propertyList.append(tp)

    #Variable Specific Functions
    #xCoordinate Specific Functions
    def get_xcoordinate(self) -> int:
        """
        Returns xCoordinate Value.
        :return:
        :rtype:
        """
        return self.xCoordinate

    def set_xcoordinate(self, targetx : int):
        """
        Sets xCoordinate to target value.

        :param targetx:
        :type targetx:
        :return:
        :rtype:
        """
        self.xCoordinate = targetx

    #yCoordinate Specific Functions
    def get_ycoordinate(self) -> int:
        """
        Returns yCoordinate Value
        :return:
        :rtype:
        """
        return self.yCoordinate

    def set_ycoordinate(self, targety: int):
        """
        Sets yCoordinate to target value.
        :param targety:
        :type targety:
        :return:
        :rtype:
        """
        self.yCoordinate = targety

    #propertyList Specfic Functions
    def get_propertylist(self) -> list:
        """
        Returns propertyList
        :return:
        :rtype:
        """
        return self.propertyList

    def set_properylist(self, targetlist):
        """
        Sets propertyList to new targetList
        :param targetlist:
        :type targetlist:
        :return:
        :rtype:
        """
        self.propertyList = targetlist

    def add_property_propertylist(self, *targetproperties: str):
        """
        Adds property strings to the target property list

        :param targetproperties:
        :type targetproperties:
        :return:
        :rtype:
        """
        for tp in targetproperties:
            self.propertyList.append(tp)

    def remove_property_propertylist(self, targetproperty : str):
        """
        Finds and removes target property from property list.

        :param targetproperty:
        :type targetproperty:
        :return:
        :rtype:
        """
        if targetproperty in self.propertyList:
            self.propertyList.remove(targetproperty)

    def __str__(self) -> str:
        """
        String Representation of Ev3Coordinate object

        :return:
        :rtype:
        """
        return '(' + str(self.xCoordinate) + ',' + str(self.yCoordinate) + ')'

    def __eq__(self, other) -> bool :
        """
        What to compare when determining whether an Ev3Coordinate object is equal to target object.

        :param other:
        :type other:
        :return:
        :rtype:
        """
        if self.xCoordinate == other.xCoordinate and self.yCoordinate == other.yCoordinate:
            return True
        else:
            return False
