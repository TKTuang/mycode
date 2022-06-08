"""flowchart TD
    A[Check Our String] --> B{"Is it 'MTG'?"};
    B -- Yes --> C[print it out!]
    B -- No --> D[do nothing]
    C --> E[Logic Done]
    D --> E[Logic Done]"""

#!/usr/bin/env python3

# create the string hostname
hostname = "MTG"
# test logic with the `if` statement
# what to do if this statement is found to be true
if hostname == "MTG":
    print("The hostname was found to be MTG")


