import csv

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
