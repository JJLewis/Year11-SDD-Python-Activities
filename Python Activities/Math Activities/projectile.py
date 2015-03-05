'''
Copyright © Jordan Lewis 2015 All Rights Reserved
This code is distributed under the Creative Commons Attribution ShareAlike 3.0 Licence

When I wrote this, only God and I understood what I was doing
Now, God only knows

WARNING:	The code that follows may make you cry;
            A Safety Pig has been provided below for your benefit
                         _
 _._ _..._ .-',     _.._(`))
'-. `     '  /-._.-'    ',/
   )         \            '.
  / _    _    |             \
 |  a    a    /              |
 \   .-.                     ;  
  '-('' ).-'       ,'       ;
     '-;           |      .'
        \           \    /
        | 7  .__  _.-\   \
        | |  |  ``/  /`  /
       /,_|  |   /,_/   /
          /,_/      '`-'
'''

import math

def dtor(d): # Function for converting degrees to radians
    return (d*math.pi)/180 # If you don't know what this does, find another job

def main():
    # Get the values from the user
    args = raw_input("Enter the values for the Velocity(V), Angle(A), and Time until explosion(T), in the following format below: 'V=<>, A=<>, T=<>' where <> gets replaces with the value you would like to assign. NOTE: The angle must be in degrees.")
    args = args.upper()
    args = args.replace(" ", "") # Get rid of all whitespace
    args_arr = args.split(",") #Split the args into seperate equations
    
    # Declare the varible
    v = 0
    a = 0
    t = 0
    
    # Being flexible with the order in which the user enters the values
    for arg in args_arr:
        arg_split = arg.split("=")
        if (arg_split[0] == "V"):
            v = float(arg_split[1])
        if (arg_split[0] == "A"):
            a = float(arg_split[1])
        if (arg_split[0] == "T"):
            t = float(arg_split[1])
    
    d = (v*t)*math.cos(dtor(a)) # If you don't know what this does, find another job
    
    # Give the mercenary or ISIS the kill zone
    print "The death zone is %fu along the ground from the launch site" % d
    
if __name__ == '__main__':
    main()