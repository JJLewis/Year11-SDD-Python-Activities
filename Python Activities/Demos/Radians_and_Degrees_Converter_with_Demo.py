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

# I should not have to comment from here down, the safety pig should help you otherwise

import math

def dtor(d): # Function for converting degrees to radians
    return (d*math.pi)/180.0 # If you don't know what this does, find another job

def rtod(r): # Radians to Degrees function
    return (r*180.0)/math.pi # If you don't know what this does, find another job

def main():
	# In Radians π/3 is the equivalent of 60˚ NOTE: 2π = 360˚ so π = 180˚
	radians = math.pi/3
	
	# Convert Radians to Degrees
	degrees = rtod(radians)
	
	print "Radians to Degrees Conversion %f" % degrees
	print "Degrees to Radians Conversion %f" % dtor(degrees) # Convert the Degrees back to Radians

if __name__ == '__main__':
	main()