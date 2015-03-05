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
    
    # The variable to become a 2D array
    chessboard = []
    
    for vert in range(0,8): # Repeat 8 times
        chessboard.append([]) # Add a row to the array
        for hor in range(0,8): # Repeat 8 times
            if (vert % 2 == 0): # If it is an even row
                if (hor % 2 == 0): # If even column
                    chessboard[vert].append("B") # Add B to the latest column in the latest row
                else: # If odd column
                    chessboard[vert].append("W") # Add W to the latest column in the latest row
            else: # If it is an odd row
                if (hor % 2 == 0): # If even column
                    chessboard[vert].append("W") # Add W to the latest column in the latest row
                else: # If odd column
                    chessboard[vert].append("B") # Add B to the latest column in the latest row
                    
        ''' Old Less Efficient Version
        if (vert % 2 == 0):
            chessboard[vert].append("W")
            for hor in range(1,8):
                if (hor % 2 == 0):
                    chessboard[vert].append("W")
                else:
                    chessboard[vert].append("B")
        else:
            chessboard[vert].append("B")
            for hor in range(1,8):
                if (hor % 2 == 0):
                    chessboard[vert].append("B")
                else:
                    chessboard[vert].append("W")
        '''
        
    # Print out the chessboard array
    for row in chessboard:
        print str(row) # Convert the array 
                
# This is the boiler plate stuff that should be in the marking criteria
if __name__ == '__main__':
    main()