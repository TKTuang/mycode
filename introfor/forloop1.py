#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   nesting an if-statement inside of a for loop

# create a list of strings
vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
# create a second list of strings
approved_vendors = ["cisco", "juniper", "big_ip"]
# loop across the list called vendors
for x in vendors:
    print("\nThe vendor is " + x, end="")   # newline, print current vendor, and end without newline
    if x not in approved_vendors:   # if x does not appear within the list approved_vendors
        print(" - NOT AN APPROVED VENDOR!", end="")
print("\nOur loop has ended.") # print when loop has finished"""


farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

user = input("Pick a zone (NE/W/SE): ")
yuck= ["carrots", "celery"]
def main():
    NE_animals= farms[0]["agriculture"]
    for animals in NE_animals:
        if user == "NE":                                                            
            print(animals, end="\n")

    W_animals= farms[1]["agriculture"]
    for animals in W_animals: 
        if user == "W":                                                             
            print(animals, end="\n")

    SE_animals= farms[2]["agriculture"]                                                 
    for animals in SE_animals:  
        if user == "SE" and animals not in yuck:
            print(animals, end="\n")
main()    

