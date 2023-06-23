# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (AlexisSmith, 20June, modified code)
# <Alexis Smith>,<20.June.2030>,Finished Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    objFile = open(file_name, "wb")
    pickle.dump(list_of_data, objFile)
    objFile.close()

def read_data_from_file(file_name):
    objFile = open(file_name, "rb")
    list_of_data = pickle.load(objFile)
    objFile.close()
    return list_of_data


# Presentation ------------------------------------ #

# TODO: Get ID and NAME From user, then store it in a list object
str_choice = str(input("What is your ID and name?"))
row = {str_choice.split(",")[0] : str_choice.split(",")[1]}
lstCustomer.append(row)


# TODO: store the list object into a binary file
save_data_to_file(strFileName, lstCustomer)

# TODO: Read the data from the file into a new list object and display the contents
print(read_data_from_file(strFileName))
