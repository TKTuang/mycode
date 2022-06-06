#!/usr/bin/env python3

#my list
my_list = [ "192.168.0.5", 5060, "UP" ]
    
#First item
print("The first items in the list is an IP address: " +  my_list[0])
    
#second item
print("The second item in the list is port: " + str(my_list[1]))

#Last item on the list
print("The last item in the list is: " + my_list[2])

#challenge
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

#display only IP addresses
print(" The IP addresses in the list are:", iplist[3], "and", iplist[4])


