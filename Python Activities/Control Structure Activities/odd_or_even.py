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
    
    # Ask the user for a number and convert it into an integer
    number = int(raw_input("Enter a whole number to know if it is odd or even!"))
    
    # If when the number is divided by 2 the remainder is 0 it is even, other wise it is odd
    if (number % 2 == 0):
        print "%i is Even" % number
    else:
        print "%i is Odd" % number

# This is the boiler plate stuff that should be in the marking criteria
if __name__ == '__main__':
    main()