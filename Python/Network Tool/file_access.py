# By Jessica Angela Campisi
# 11/08/2018
# file_access.py
# Description: Create, read, modify a file to store the username, old pc name, and new pc name.


# define the userdata class
class UserData:
    # test data
    pcName = ""
    oldPC = ""
    userName = ""


    # def __init__(self):
    #     # check to see if they want to load the old information or use new user information.
    #
    #     self.display_user_info()
    #     new_user = input("\nDo you wish to enter new user information Yes/No [No]: ")
    #
    #     if new_user.capitalize() == "Yes":
    #         self.get_info_from_user()
    #
    #     elif new_user.capitalize() == "No" or new_user == "":
    #         print("\nUsing original information.")
    #     else:
    #         print("\nDid not enter a Yes or a No. Try Again.")
    #         self.initialize()

    # Write the user data to a file
    def save_user_file(self):
        # create or open existing text file named userdata.txt
        f = open("userdata.txt", "w+")

        f.write(self.pcName + "\n")
        f.write(self.oldPC + "\n")
        f.write(self.userName + "\n")

        f.close()

    # Read the user data from a file
    def get_user_data(self):
        try:
            f = open("userdata.txt", "r")
            # check if the file is open
            if f.mode == 'r':
                contents = f.readlines()

                self.set_pc_name(contents[0])
                self.set_old_name(contents[1])
                self.set_user_name(contents[2])
            f.close()

        except FileNotFoundError:
            print("A file does not exist yet!")

            # If the file does not exist, get it from the user
            self.get_info_from_user()

    # Set Variables
    def set_pc_name(self, name):
        self.pcName = name

    def set_old_name(self, name):
        self.oldPC = name

    def set_user_name(self, name):
        self.userName = name

    # Get Variables
    def get_pc_name(self):
        return self.pcName

    def get_old_name(self):
        return self.oldPC

    def get_user_name(self):
        return self.userName

    # Request information from the user
    def get_info_from_user(self):
        self.set_pc_name(input("What is the PC name: "))
        self.set_old_name(input("What is the old pc name, if any: "))
        self.set_user_name(input("What is the username: "))

        # Save the data
        self.save_user_file()

    # Display information for use
    def display_user_info(self):
        self.get_user_data()
        print("Computer Name: {}".format(self.get_pc_name().rstrip()))

        if self.get_old_name() is not " ":
            print("Old Computer Name: {}".format(self.get_old_name().rstrip()))

        print("Username: {}".format(self.get_user_name().rstrip()))

    def initialize(self):
        # check to see if they want to load the old information or use new user information.

        self.display_user_info()
        new_user = input("\n\nDo you wish to enter new user information Yes/No [No]: ")

        if new_user.capitalize() == "Yes":
            self.get_info_from_user()

        elif new_user.capitalize() == "No" or new_user == "":
            print("\nUsing original information.")
        else:
            print("\nDid not enter a Yes or a No. Try Again.")
            self.initialize()