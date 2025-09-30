#! usr/bin/env python3
# Author: ABabalola
# Description: This script will simulate a high street bank ATM machine

"""
DOCSTRING
"""

master_pin = "0123"
pin = None
count = 0

while pin != master_pin and count < 3:
    count += 1
    pin = input("Enter PIN: ")
    if pin == master_pin:
        print("Valid PIN")
        break
    else:
        print("Invalid PIN")
else:
    # ONLY EXECUTE ONCE if while loop becomes false
    print('Too many attempts')
    print('Your card has been retained. The police are on their way!!!')

print("Done")