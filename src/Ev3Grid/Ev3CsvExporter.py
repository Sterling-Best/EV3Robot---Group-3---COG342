import csv
import time
import datetime

class Ev3CsvExporter:
    """
    Using data from given Ev3Global object, create an csv file of Ev3Coordinate Objects.
    """

    def __init__(self):
        """"
        Initialization of Ev3CsvExporter object.
        """

    def createcsv(self, a_targetglobal) -> None:
        """
        Create csv from

        Args:
            a_targetglobal (Ev3Global):

        Returns:
            None: CSV file of Ev3Coordinates
        """
        coordlist = a_targetglobal.collectcoord()
        with open('../../out/csv/globalgrid.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile, dialect='excel', delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(["X", "Y"])
            for coord in coordlist:
                filewriter.writerow([str(coord.get_xcoordinate()), str(coord.get_ycoordinate())])
        csvfile.close()

    def datetimefilename(self) -> str:
        """
        Generates a string based on computers current date and time to generate a unique filename.

        Returns:
            str: String containing date and time, to be used as file name.

        Doctests:
        >>> aEx = Ev3CsvExporter()
        >>> ts = time.time()
        >>> ds = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d-%H%M%S')
        >>> ds == aEx.datetimefilename()
        True
        """
        timestamp = time.time()
        return datetime.datetime.fromtimestamp(timestamp).strftime('%Y%m%d-%H%M%S')

if __name__ == "__main__":
    import doctest
    doctest.testmod()
