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

def rtd(r): # Radians to Degrees function
    return (r*180)/math.pi # If you don't know what this does, find another job

def main():

	# Get the user to enter in the values for the perpendicular sides of the triangle in the format a,b or with white-space in-between which we will strip later
    sides = raw_input("Enter the lengths of two perpendicular sides of a triange seperated by a comma.")
    
    # Split the string with the format a,b into an array with [a,b]
    sides_arr = sides.split(',')
    
    # Incase the string was something like: ' a   ' and had whitespace everywhere, lets get rid of it
    vert_str = sides_arr[0].strip()
    hor_str = sides_arr[1].strip()
    
    # Convert the string value into floats
    vert = float(vert_str)
    hor = float(hor_str)
    
    # I should not have to comment from here down, the safety pig should help you otherwise
    area = (1/2.0)*vert*hor
    hypotenuse = math.sqrt(((vert**2)+(hor**2)))
    
    angle1 = rtd(math.asin(vert/hypotenuse))
    angle2 = rtd(math.asin(hor/hypotenuse))
            
    print "A triagle with a base %fu and height %fu has:" % (hor, vert)
    print "An area of %fu^2" % area
    print "A hypotenuse with length %fu" % hypotenuse
    print "Angles of 90 degrees, %f degrees, and %f degrees" % (angle1, angle2)
    
if __name__ == '__main__':
    main()