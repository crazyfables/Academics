"""
By Jessica Angela Campisi
Date: 10/29/2019
Project: Present random chuck norris quotes to the user using the chucknorris.io api. 
Transform them from a json format to a dictionary. 
Allow the user to read as many as they want and quit when they want. 
"""
import json, requests, flask

# function gets a string of data using requests.get
def get_chuck():
    req = requests.get("https://api.chucknorris.io/jokes/random")
    # req.json() converts the json to a dictionary format.
    req_json = req.json()
    # send the chucky quote to the function call
    return req_json['value']


if __name__ == '__main__':
    # Let's introduce the program to the user
    print("Welcome to The Chuck!")
    print("You will be exposed to the awesomeness of the Chuck. You can choose at any time to get off the Chuck Bus.")

    # start the loop, because why not?!
    while True:
        choice = input("\n\nWould you like to see a Chuck Norris joke (y/n): ")

        # If statements converts answers to capital when checking
        # tells the user they've made poor life choices if they don't enter y or n
        if choice.upper() == 'Y':
            # get a chucky quote
            print(get_chuck())
        elif choice.upper() =='N':
            print("\nGoodbye!")
            break
        else:
            print("You somehow managed to not answer with a y or n. Try again!")