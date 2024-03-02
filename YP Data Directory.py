import datetime
# - This module allows the processing of date and time separate from integer or string representation with bulky if statements to limit length of months. e.g. month_length <= 31 elif month = February month_length <= 29/28 etc.
import pytest
# - This module called is called pytest and will "assert" data to verify that it is presented to the user as the program intends it to. e.g. "assert isinstance(datasets, list)" asserts that the data outputted/stored is actually a list. e.g. ('a', 'b', 'c', 'd')

# - This tests that there are indeed 10x datasets that the user can view and amend.
def Test_Hardcoded_YP_Data():
    datasets = Hardcoded_YP_Data()
    assert isinstance(datasets, list)
    assert len(datasets) == 10

# - This tests that the Forenames and Surnames of all 10x datasets are shown on start up of the program and shown again upon rerunning the program.
def Test_Stored_YP_Data(capsys):
    datasets = Hardcoded_YP_Data()
    Stored_YP_Data(datasets)
    captured = capsys.readouterr()
    assert "All stored YP data:" in captured.out

# - This tests the function of searching by forename and surname and ensures that when a forename and surname that match a record are entered that the program retrieves the full relevent dataset.
def Test_Query_YP_Data_By_Name():
    datasets = Hardcoded_YP_Data()
    result = Query_YP_Data_By_Name(datasets, "Robert", "Kent")
    assert result is not None
    assert result["Forename"] == "Robert"
    assert result["Surname"] == "Kent"

# - This tests the function of searching by forename and surname and ensures that when a forename and surname that match a record are entered that the user can then amend all other data within that dataset.
def Test_Amend_YP_Data_By_Name():
    datasets = Hardcoded_YP_Data()
    amended_data = {"YP's Wheelchair Model:": "NewModel", "Risk Assessment Status:": True}
    Amend_YP_Data_By_Name(datasets, "Robert", "Kent", amended_data)
    updated_data = Query_YP_Data_By_Name(datasets, "Robert", "Kent")
    assert updated_data["YP's Wheelchair Model:"] == "NewModel"
    assert updated_data["Risk Assessment Status:"] == True

# - This function validates that any data the user has entered into the program is an integer where required/relevant.
def validate_integer_input(prompt):
    while True:
        try:
            YP_Data = int(input(prompt))
            return YP_Data
        except ValueError:
            print("Invalid input. Please enter an integer.")

# - This function validates that any data the user has entered into the program is a boolean value (True or False) where required/relevant.
def validate_boolean_input(prompt):
    while True:
        YP_Data = input(prompt).lower()
        if YP_Data == "true" or YP_Data == "false":
            return YP_Data == "true"
        else:
            print("Invalid input. Please enter 'True' or 'False'.")

# - This function validates that any data the user has entered into the program is of the right date format (DD-MM-YYYY) where required/relevant.
def date_input_validation(prompt):
    while True:
        date_str = input(prompt)
        try:
            YP_Data = datetime.datetime.strptime(date_str, "%d-%m-%Y").date()
            return YP_Data
        except ValueError:
            print("Invalid date format. Please enter a date in the format 'DD-MM-YYYY'.")

# - These 10x lists are the 10 YP Datasets that the user can view/amend in the program.
def Hardcoded_YP_Data():
    return [
        {"Forename": "Robert", "Surname": "Kent", "Date of Next Clinical Assessment:": "01-01-2001", "Date of Last Clinical Assessment:": "02-02-2002", "YP's Wheelchair Model:": "Neo", "YP's Wheelchair Width (cm):": 55 , "YP's Access Method:": "Red Smoothie Switch", "YP's Risk Assessment Status:": False},
        {"Forename": "Rupert", "Surname": "Buster", "Date of Next Clinical Assessment:": "02-02-2002", "Date of Last Clinical Assessment:": "03-03-2003", "YP's Wheelchair Model:": "Chunc", "YP's Wheelchair Width (cm):": 67, "YP's Access Method:": "Yellow Softy Top", "YP's Risk Assessment Status:": True},
        {"Forename": "Billy", "Surname": "Dakidd", "Date of Next Clinical Assessment:": "03-03-2003", "Date of Last Clinical Assessment:": "04-04-2004", "YP's Wheelchair Model:": "Discovery", "YP's Wheelchair Width (cm):": 65, "YP's Access Method:": "Eyegaze", "YP's Risk Assessment Status:": False},
        {"Forename": "Lionel", "Surname": "Tamer", "Date of Next Clinical Assessment:": "04-04-2004", "Date of Last Clinical Assessment:": "05-05-2005", "YP's Wheelchair Model:": "Neo", "YP's Wheelchair Width (cm):": 54, "YP's Access Method:": "Joystick", "YP's Risk Assessment Status:": True},
        {"Forename": "Cecil", "Surname": "Awning", "Date of Next Clinical Assessment:": "05-05-2005", "Date of Last Clinical Assessment:": "06-06-2006", "YP's Wheelchair Model:": "Neo", "YP's Wheelchair Width (cm):": 49, "YP's Access Method:": "Red Smoothie Switch", "YP's Risk Assessment Status:": False},
        {"Forename": "Lily", "Surname": "Harvey", "Date of Next Clinical Assessment:": "06-06-2006", "Date of Last Clinical Assessment:": "07-07-2007", "YP's Wheelchair Model:": "Whizzy", "YP's Wheelchair Width (cm):": 45, "YP's Access Method:": "Red Softy Top", "YP's Risk Assessment Status:": True},
        {"Forename": "Molly", "Surname": "Enfield", "Date of Next Clinical Assessment:": "07-07-2007", "Date of Last Clinical Assessment:": "08-08-2008", "YP's Wheelchair Model:": "Salsa", "YP's Wheelchair Width (cm):": 70, "YP's Access Method:": "Red Buddy Button", "YP's Risk Assessment Status:": False},
        {"Forename": "Lizzie", "Surname": "Weiss", "Date of Next Clinical Assessment:": "08-08-2008", "Date of Last Clinical Assessment:": "09-09-2009", "YP's Wheelchair Model:": "Discovery", "YP's Wheelchair Width (cm):": 65, "YP's Access Method:": "Green Buddy Button", "YP's Risk Assessment Status:": True},
        {"Forename": "Brenton", "Surname": "Jameson", "Date of Next Clinical Assessment:": "09-09-2009", "Date of Last Clinical Assessment:": "10-10-2010", "YP's Wheelchair Model:": "Neo", "YP's Wheelchair Width (cm):": 60, "YP's Access Method:": "Joystick", "YP's Risk Assessment Status:": False},
        {"Forename": "Aimee", "Surname": "Anderson", "Date of Next Clinical Assessment:": "10-10-2010", "Date of Last Clinical Assessment:": "11-11-2011", "YP's Wheelchair Model:": "Salsa Mini", "YP's Wheelchair Width (cm):": 60, "YP's Access Method:": "Eyegaze", "YP's Risk Assessment Status:": True},
    ]

# - This function displays the Forenames and Surnames of the 10x YP Datasets that the user can view and amend in the terminal.
def Stored_YP_Data(datasets):
    print("\nAll stored YP data:")
    for dataset in datasets:
        print(f"{dataset['Forename']} {dataset['Surname']}")

# - This function allows the user to select a YP's Dataset to view by entering a corresponding forename and surname.
def Query_YP_Data_By_Name(datasets, Forename, Surname):
    for dataset in datasets:
        if dataset["Forename"].lower() == Forename.lower() and dataset["Surname"].lower() == Surname.lower():
            return dataset
    return None

# - This function allows the user to select a YP's Dataset to amend by entering a corresponding forename and surnameand then allowing the user to amend all other pieces of data within that dataset.
def Amend_YP_Data_By_Name(datasets, Forename, Surname, amended_yp_data):
    for dataset in datasets:
        if dataset["Forename"].lower() == Forename.lower() and dataset["Surname"].lower() == Surname.lower():
            dataset.update(amended_yp_data)
            print("YP data successfully amended.")
            return
    print("No matching YP's.")

# - This initialises the program so that it is able to run and triggers the 10x stored YP forename/surnames to print in the terminal and then displays the user interface.
def main():
    datasets = Hardcoded_YP_Data()

# - This displays the 10x stored YP forename/surnames that the user can view/edit the stored data of.
    Stored_YP_Data(datasets)

# - This is the interface presented to the user so and explains the functions that can be activated, users can view or amend a datsaset or exit the program.
    while True:
        print("\n1. View YP's Data:")
        print("2. Amend YP's Data:")
        print("3. Exit")

# - This function stores the users input of what function they wish to activate and runs a validation test on it in line 37 to 43 to ensure it is an integer value between =>1 and =<3
        user_selection = input("Select desired program function: input 1 - 3: ")

# - This function allows the user to enter a forename and surname and if they match a stored dataset it will display the full dataset. The program will then reboot and allow the user to choose the same or a diffeent function or even exit the program.
        if user_selection == "1":
            Forename = input("Enter the Forename to search: ")
            Surname = input("Enter the Surname to search: ")
            result = Query_YP_Data_By_Name(datasets, Forename, Surname)
            if result:
                print("Current Data for YP:", result)
            else:
                print("No matching YP Data, please ensure YP name is correct.")
        elif user_selection == "2":

# - This function allows the user to enter a forename and surname and if they match a stored dataset it will allow the user to edit the other data that is present such as wheelchair model and access method. The program will then reboot and alow the user to recall the amended dataset.
            Forename = input("Enter the Forename of the record to amend: ")
            Surname = input("Enter the Surname of the record to amend: ")
            amended_yp_data = {
                "What was the date of the YP's last clinical assessment: (Format: DD-MM-YYYY)": date_input_validation("What was the date of the YP's last clinical assessment: (Format: DD-MM-YYYY)"),
                "Date of Next Clinical Assessment: (Format: DD-MM-YYYY)": date_input_validation("What is the date of the YP's next clinical assessment: (Format: DD-MM-YYYY)"),
                "YP's Wheelchair Model:": input("What is the model of the YP's new wheelchair? "),
                "YP's Wheelchair Width:": validate_integer_input("What is the width of the YP's new wheelchair? (cm)"),
                "YP's Access Method:": input("What is the YP's current access method? "),
                "Risk Assessment Status:": validate_boolean_input("What is the YP's current status of risk assessment? Please input either: (True/False):"),
            }
            amend_dataset(datasets, Forename, Surname, amended_yp_data)
        elif user_selection == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Incorrect selection. Select an option numbered 1 to 3:")

# - This runs the program once the run button is pressed and begins outputting to the terminal.
if __name__ == "__main__":
    main()