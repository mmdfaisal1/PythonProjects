from csv_reader import CSVReader

my_credentials_list = CSVReader("TestData/credentials.csv").read_data()

# Since my_credentials_list is a list of dictionaries
# We can iterate through each item in the list (a dictionary)
for row in my_credentials_list:
    print(row["UserName"], row["Password"])







