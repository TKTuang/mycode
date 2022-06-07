#!/usr/bin/env python3

#first list
wordbank= ["four", "spaces"]

#student list
tlgstudents= ["Aaron", "Casey", "Donny", "Emmanuel", "Eric", "Jaelen", "James", "Jay", "John", "Ken", "Maurice", "Mike", "Ryan", "Shamain", "Tuang", "Tyler", "Zhenqian", "Travis"]

num = int(input("Type any number between 0 -17: "))

#print output
print("Student #",num, "is", tlgstudents[num])

#Save student name
student_name = tlgstudents[num]

print(student_name, "always uses", num, wordbank[1],  "to indent")


