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

def main():
	
	# Get the diameter of the circle from the user and strip any leading or trailing whitespace just in case there is any
    d = float(raw_input("Enter the diameter of a circle").strip())
    
    # I should not have to comment from here down, the safety pig should help you otherwise
    r = d/2
    p = math.pi*d
    a = 2*math.pi*(r**2)
    sa = 4*math.pi*(r**2)
    v = (4.0/3.0)*math.pi*(r**3)
    
    print "A circle with a diameter %fu has:" % d
    print "A radius of %fu" % r
    print "A perimeter of %fu" % p
    print "An area of %fu^2" % a
    print "\n"
    print "A sphere with a diameter %fu has:" %d
    print "A surface area of %fu^2" % sa
    print "A volume of %fu^3" % v
    
if __name__ == '__main__':
    main()