# Word Ratio calcuator


I made this because i was bored lol

This program uses a list that i found online of every word in the english dictionary and takes the length of the word and divides it by the ammount of unique characters. If you can't tell, this will result in being able to find the longest word you can spell with the shortest ammount of unique characters (i got asked what i think it would be in a discord call and decided to make it LOL)

For example,  
For the word **Alaska** we get the total characters, and divide it by the unique characters.

*6/4 = 1.5*

Feel free to edit this code however you want and edit the words.txt file to make your own list. 





The "bigboy.txt" is for when a set ratio is above the ratio set (in line 17)

this is how the code works in full 

- Wait is defined for the end of the program so you know the program has been completed
- Every file needed gets opened
- Variables defined for how to get the required info to make the ratio 
- If ratio is above a set ammount (2.7 by default) the result gets sent to bigboy.txt
- else it  gets sent to result .txt  
 (The format is) stripped_word + " Has a word ratio of " + str(Ratio)
- X increments by 1 until it excedes the limit of the  file (194444 in this case)
- Program says it has been completed and promts the user to press space to end the program.