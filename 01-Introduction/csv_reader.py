import csv


class CSVReader:
    def __init__(self, file_path):
        self.file_path: str = file_path

    def read_data(self):
        with open(self.file_path) as csv_file:
            reader = csv.DictReader(csv_file)
            # return reader   This does not work. reader is just a file handle containing the headers of the csv
            #                 It does not contain the actual file. So returning reader here means trying to do I/O
            #                 on a file which has been closed
            credentials_list: list = []
            for row in reader:
                credentials_list.append(row)
            return credentials_list  # This is a list of dictionaries




