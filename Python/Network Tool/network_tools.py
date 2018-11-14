# By Jessica Angela Campisi
# 11/08/2018
# Description: Obtain the network status of a host.

import os, file_access, socket, subprocess, sys


class NetworkTools:

    data = file_access.UserData()
    hostname = data.get_pc_name()

    # Checks to see if it can reach the device. Currently provides status messages. Will change it to return a 0 or 1
    # later so that it can be used before install/config attempts.
    def check_ping(self):
        response = os.system("ping " + self.hostname + " /n 4")
        if response == 0:
            return True
        else:
            return False

    # remote connection, function will ping the device to make sure it's online before it connects.
    def remote_desktop(self):
        if self.check_ping():
            print("\nLaunching a remote desktop connection to " + self.hostname)
            os.system("mstsc /v:{}".format(self.hostname))
        else:
            print("\nUnable to reach host: {}\nVerify the hostname and try again later.".format(self.hostname))

    # Trace the route of the connection to determine where the connection drops.
    def trace_route(self):
        response = os.system("tracert " + self.hostname)

        if response == 0:
            tracestatus = "Trace Completed."
        else:
            tracestatus = "Trace could not resolve target."
        return tracestatus

    # Provide the menu that will be used by the technician to choose what action they would like to perform.
    def instructions(self):
        print("Network Testing Tools")
        print("These tools will allow you to test the connection to end user devices.")
        print('{:*^40}'.format('*'))
        print("1. Ping")
        print("2. Trace Route")
        print("3. Remote Desktop Connection")
        print("4. Get IP Address")
        print("99. Quit")

        self.tool_choice()

    # Split the menu choice from the instructions function so tha it can be ran again separately if a wrong choice is
    # entered.
    def tool_choice(self):
        choice = int(input("Enter your choice: "))
        if choice == 1:
            self.check_ping()
        elif choice == 2:
            self.trace_route()
        elif choice == 3:
            self.remote_desktop()
        elif choice == 4:
            self.get_ip_address()
        elif choice == 99:
            print("Goodbye!")
            quit()
        else:
            print("{} is not a choice! Try again!".format(choice))

            # This function is calling itself again because it is narcissistic. And because it will ask for a new choice
            # following a bad entry.
            self.tool_choice()

    # use the hostname to get the IP address.
    def get_ip_address(self):
        try:
            print("Hostname: " + self.hostname)
            print("IP Address: {}".format(socket.gethostbyname(self.hostname)))

        except socket.gaierror:
            print("Could not get IP Address")


"""
commenting out this code as network_tools.py is going to be part of my library.

run_tools = NetworkTools()

again = "Yes"

# main program loop
while again == "Yes":
    run_tools.instructions()
    again = input("\nWould you like to run another tool? Yes/No [Yes]: ").capitalize()
    if again == "Yes" or again == "":
        newDevice = input("Different PC? Yes/No [No]: ").capitalize()
        if newDevice == "Yes":
            run_tools.data.get_info_from_user()
            run_tools.hostname = run_tools.data.get_pc_name()
            print("\nRunning again with a new machine.")
        else:
            print("\nRunning again with the same machine.")
        # run again
        run_tools.instructions()
    else:
        print("Have a good day!")
        quit()
# old testing code.
# print("\nPinging {}".format(hostname))
# print('{:*^40}'.format('*'))
# print("Status for {0}: {1}".format(hostname, check_ping(hostname)))
#
# print("\nTracing the route for {}".format(hostname))
# print('{:*^40}'.format('*'))
# print("Trace status for {0}: {1}".format(hostname, trace_route(hostname)))
"""