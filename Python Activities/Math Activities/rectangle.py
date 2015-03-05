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

def main():
	
	# Get the length and width of the rectangle from the user and strip any leading or trailing whitespace just in case there is any
    length = float(raw_input("Enter the length of a rectangle").strip())
    width = float(raw_input ("Enter the width of a rectangle").strip())
    
    # I should not have to comment from here down, the safety pig should help you otherwise
    area = length*width
    perimeter = 2*length + 2*width
    
    print "The area of a rectangle with length %f and width %f has an area of %fu^2 and a perimeter of %fu" % (length, width, area, perimeter)

if __name__ == '__main__':
    main()