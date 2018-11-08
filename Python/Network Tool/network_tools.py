# By Jessica Angela Campisi
# 11/08/2018
# Description: Obtain the network status of a host.

import os, file_access, socket

class NetworkTools:

    data = file_access.UserData()
    hostname = data.get_pc_name()
    # Checks to see if it can reach the device. Currently provides status messages. Will change it to return a 0 or 1
    # later so that it can be used before install/config attempts.
    def check_ping(self):
        response = os.system("ping " + self.hostname + " /n 4")
        if response == 0:
            pingstatus = "Network Active"
        else:
            pingstatus = "Network error"
        return pingstatus


    # remote connection
    def remote_desktop(self):
        os.system("mstsc /v:{}".format(self.hostname))

    # Trace the route of the connection to determine where the connection drops.
    def trace_route(self):
        response = os.system("tracert " + self.hostname)

        if response == 0:
            tracestatus = "Trace Completed."
        else:
            tracestatus = "Trace could not resolve target."
        return tracestatus

    def instructions(self):
        print("Network Testing Tools")
        print("These tools will allow you to test the connection to end user devices.")
        print('{:*^40}'.format('*'))
        print("1. Ping")
        print("2. Trace Route")
        print("3. Remote Desktop Connection")
        print("4. Get IP Address")

        self.tool_choice()

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
        else:
            os.system("CLS")
            print("{} is not a choice! Try again!".format(choice))

    # getting hostname does not work here.
    def get_ip_address(self):
        try:
            print("IP Address: {}".format(socket.gethostbyname(self.hostname)))

        except socket.gaierror:
            print("Could not get IP Address")


# Getting hostname works here...
#hostname = "www.google.com"
#ip = socket.gethostbyname(hostname)
#print("\n{0} ip address: {1}".format(hostname, ip))

run_tools = NetworkTools()

again = "Yes"

# main program loop
while again == "Yes":
    run_tools.instructions()

    again = input("\nWould you like to run another tool? Yes/No: ").capitalize()

    if again == "Yes":
        newDevice = input("Different PC? Yes/No: ").capitalize()

        if newDevice == "Yes":
            run_tools.data.get_info_from_user()
            run_tools.data.save_user_file()
            print("\nRunning again with a new machine.")
        else:
            print("\nRunning again with the same machine.")



# print("\nPinging {}".format(hostname))
# print('{:*^40}'.format('*'))
# print("Status for {0}: {1}".format(hostname, check_ping(hostname)))
#
# print("\nTracing the route for {}".format(hostname))
# print('{:*^40}'.format('*'))
# print("Trace status for {0}: {1}".format(hostname, trace_route(hostname)))
