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
    
    # Ask the user for their age and convert it into an integer
    age = int(raw_input("How old are you?"))
    
    # If the age is greater than or equal to 18 than the user can vote, if not tell him/her he can't and how long until he can
    if (age >= 18):
        print "Did you know that you CAN vote?"
    else:
        print "Sorry you can't vote yet, the legal age is 18 so you have about %i years before you can vote." % (18-age)

# This is the boiler plate stuff that should be in the marking criteria
if __name__ == '__main__':
    main()