#1/usr/bin/env python3


#list
my_list = ["Black Suit", "Alien Costume"]
my_list2 = ["Eddie Brock (Costume)", "Peter Parker (cloth)"]

#dictionary
Symbiote_Costume = {"first appereance": "Amazing Spider-Man #252",
        "Alternate names": my_list[0],
        "Current Owner": my_list2[1],
        "film": "Spider-Man 3",
        "Other realities": 7}

num = input("Pick number between 1-5: ")

if num == 1:
    print("When was Symbiote Costume first appareance?", (Symbiote_Costume["first appereance"]))
elif num == 2:
    print("What is Symbiote Costume alternate names?", (Symbiote_Costume["Alternate names"]))
elif num == 3:
    print("Who is the current owner?", (Symbiote_Costume["Current Owner"]))
elif num == 4:
    print("What film was it first debut in?", (Symbiote_Costume["film"]))
else:
    print("How many other realities Symbiote Costume do we know of?", (Symbiote_Costume["Other realities"]))


