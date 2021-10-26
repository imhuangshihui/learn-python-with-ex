# Exercises for GNBF5010 Lecture 5: Dictionaries

1. Dictionary Union. Create a function union_dictionaries() that takes two dictionaries as 
parameters returns their “union” as a dictionary—when a key is found in both, the larger value 
should be used in the output. If dictionary dict_a maps "A", "B", "C" to 3, 2, 6, and dict_b maps 
"B", "C", "D" to 7, 4, 1, for example, the output should map "A", "B", "C", "D" to 3, 7, 6, 1. 
 
2. Date Decoder. A date of the form 9-OCT-21 includes the name of the month, which must be 
translated to a number. Create a dict suitable for decoding month names to numbers. Create a 
function which uses string operations to split the date into 3 items using the "-" character, 
translates the month, and corrects the year to include all the digits. The function will accept a 
date in "dd-MMM-yy" format and return a tuple of (y, m, d), e.g. (2021, 10, 09). 
 
3. Dice Odds. There are 36 possible combinations of two dice. A simple pair of nested loops will 
enumerate all combinations. The sum of the two dice is more interesting than the actual 
combination. Create a dict of all combinations, using the sum of the two dice as the key. Each 
value in the dict should be a list of tuples; each tuple has the value of two dice. The 
general outline is something like the following: 

    dice_dict = {} 
    
    Loop with d1 from 1 to 6 
    
        Loop with d2 from 1 to 6 
        
            newTuple ← (d1, d2) # create the tuple 
            
            oldList ← dictionary entry for sum d1+d2  
            
            replace entry in dictionary with oldList + newTuple 
            
     
     Loop over all values in the dictionary 
    
        print the key and the length of the list 
