# By Jessica Angela Campisi
# 11/08/2018
# Description: Obtain the network status of a host.

import os, file_access


# Checks to see if it can reach the device. Currently provides status messages. Will change it to return a 0 or 1
# later so that it can be used before install/config attempts.
def check_ping(host):
    response = os.system("ping " + host + " /n 4")
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network error"
    return pingstatus


# Trace the route of the connection to determine where the connection drops.
def trace_route(host):
    response = os.system("tracert " + host)

    if response == 0:
        tracestatus = "Trace Completed."
    else:
        tracestatus = "Trace could not resolve target."
    return tracestatus


print("Network testing tools")
print("These tools will allow you to test the connection to end user devices.")

# create a customer object to hold username, pc name, and old pc name
customer = file_access.UserData()

# get and display this information
customer.new_or_old_data()

# pass the pc name as the hostname. Redundancy is for readability.
hostname = customer.get_pc_name()

print("\nPinging {}".format(hostname))
print('{:*^40}'.format('*'))
print("Status for {0}: {1}".format(hostname, check_ping(hostname)))

print("\nTracing the route for {}".format(hostname))
print('{:*^40}'.format('*'))
print("Trace status for {0}: {1}".format(hostname, trace_route(hostname)))
