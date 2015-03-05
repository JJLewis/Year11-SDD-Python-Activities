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
	# This is the initial story
	story = 'One morning Fred woke up and decided to go to the beach. At the beach there was a dog called Spot. They played with a ball for quite some time. When the day was over Fred and Spot went their separate ways.'

    print story
    
    # Get the user to enter some information
    name = raw_input("What is your name?")
    dog = raw_input("Type a dog's name below")
    #gender = raw_input("Enter your gender. eg: male, female, both")
    location = raw_input("Where did you go last weekend?")
    
    # Replace parts of the main story with the information provided by the user
    new_story = story.replace("Fred", name)
    new_story = new_story.replace('Spot', dog)
    new_story = new_story.replace('beach', location)
    
    print new_story
    
    # Get the user to enter / copy and paste part of the story they want to change
    part_to_change = raw_input("Now you can change any part of the story, '%s', copy the section you want to replace into the textfield below." % new_story)
    # Get the user to enter what they want to change the part of the story to
    change_to = raw_input("Enter below what you would like to change '%s' to." % part_to_change)
    
    # Now do the replacing
    even_newer_story = new_story.replace(part_to_change, change_to)
    print even_newer_story
    
    # Some meta-data on the story
    story_length = len(even_newer_story)
    words_array = even_newer_story.split() # Array of words for counting in the next line
    word_count = len(words_array)
    
    print "The story has "+str(story_length)+" characters in it"
    print "The story has "+str(word_count)+" words in it"
    
if __name__ == '__main__':
    main()