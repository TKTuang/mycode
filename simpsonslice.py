#!/usr/bin/env python3
"""Morning Slicing Challenge!"""

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

def main():
    """write your code in this function to solve the challenge"""

    # write one print function for each list above
    # get the strings "eyes," "goggles," and "nothing from each
    # final output for each print should look like this:
    """My eyes! The goggles do nothing!"""

    print(challage)
    print(trial)
    print(nightmare)
    print("My", challenge[2][1] + "! The", challenge[2][0], "do", challenge[3] + "!")

    if __name__ == "__main__": # <-- what is this??? we will review later :)
        main()

print(f"My {challenge[2][1]}! The {challenge[2][0]} do {challenge[3]}!")
#print("My", challenge[2][1] + "! The", challenge[2][0], "do", challenge[3] + "!")
#print("My", trial[2]["goggles"] + "! The", trial[2]["eyes"], "do", challenge[3] + "!")
print(f"My {trial[2]["goggles"]}! The {trial[2]["eyes"]} do {trial[3]}!")
