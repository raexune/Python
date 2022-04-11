import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

fname = input("Gib deinen Vornamen ein: ")
lname = input("Gib deinen Nachnamen ein: ")

print(lname + " " + fname)



