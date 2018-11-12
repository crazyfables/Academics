# By Jessica Angela Campisi
# Prime Finder
# 10/04/2018
# Description: Print out every prime number between 2 and x. Made a class for this. Overkill.


# Creating a class to handle this investigation into prime numbers
class Prime:

    # Instantiate numbers before use
    min = 2
    max = 0

    def is_prime(self, num):
        for x in range(2, num-1):
            if num % x is 0:
                return False
        return True

    def run(self):
        print("Enter a number. This program will return every prime number between 1 and that number.")
        self.number_request()
        self.print_prime()

    def print_prime(self):

        for x in range(self.min, self.max+1):
            if self.is_prime(x):
                print(x)

    def number_request(self):
        self.max = int(input("Please enter a large number: "))


# create and run my object
find_prime = Prime()
find_prime.run()
