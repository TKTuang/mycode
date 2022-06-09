#!/usr/bin/python3

with open("dracula.txt", "r") as Dracula:
    DraculaNovel = Dracula.readlines()

    count = 0

    for read in DraculaNovel:
        if "vampire" in read.lower():
            print(read, end="")
            print(count)
            count += 1

            f = open("vampytimes.txt", "a")
            f.write(read)
            f.close()



