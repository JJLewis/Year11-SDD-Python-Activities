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
    
    # Print all the multiples of 3 between 1 and 1000
    print "Multiples of 3 from 1 to 1000"
    for i in range(1,1000): # Loop 1000 times
        if (i % 3 == 0): # If the number is divisible by 3, print the number
            print str(i) # Convert the number to a string, just because
            
    print "Multiples of 7 from 1 to 1000"
    i = 1
    while i <= 1000: # While i is less than or equal to 1000
        if (i % 7 == 0): # If the number is divisible by 7, print the number
            print str(i) # Convert the number to a string, just because
        i += 1 # Increment the value of i because a while won't do it for you
    
    # It's always nice to tell the user when the program has ended with one like this, because it seems frozen at the last number
    print "End of Program"
    
# This is the boiler plate stuff that should be in the marking criteria
if __name__ == '__main__':
    main()