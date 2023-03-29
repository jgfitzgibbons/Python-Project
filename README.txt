The purpose of hunt.py program is for providing the user deer hunting numbers in Wisconsin in 2019 based on county name. 
The program pulls data from a csv file 'hunting success.csv'. First, it prompts the user to input a county name that must be
in all uppercase letters, and then provides the number of tags issued, and the number of deer harvested. It then asks the user 
if they want to look up hunting numbers for another county, or if they want to look up the hunting success rate for a county, or if 
they want to quit the program (by inputing 1, 2, or 3). Any other number will return 'please enter a number between 1 and 3', 
and ask the user again what they want to do out of the three options. The program continuously loops through the options, and provides
the accurate responses until the user enters the number 3 to quit. 

code_dictionary() opens the csv 'hunting success.csv' for reading and creates the dictionary hunt with county name
as the key and tags issued and deer harvested as the values.

myClass creates a class with instance variables as the three data colomns in the csv (county, issued, harvested).
It also has a method success() that calculates the successrate percentage (Harvested/Issued * 100) rounded to 2 decimal
places.

success_rate() is for calculating the success rate by calling the method success() from myClass. Having it as its own
function makes it easier to call it into main() later in the program

query_hunt_code() asks the user to input a county in Wisconsin. If the county name provided is in the csv file
'hunting success.csv' it will return the values associated with the county (issued, harvested). If it is not
in the csv file, or if it is not all uppercase letters, it will return 'county not found'.

main() gives the user options for what they would like to search next. The user can input the number 1 to loop back
to query_hunt_code() in order to search a county to find issued/harvested numbers. The user can input 2 to call the 
success_rate() function, and calculate the success rate for a county of their choice which again, must be all uppercase
and in the imported csv file. The user can input the number 3 to quit the program.

To run the program th csv file 'hunting success.csv' must be saved in the current working directory for your idle shell.
Hunt.py must also be saved in the save directory as the csv. Once they are both saved, you can type 'input hunt' in
the idle shell, or open hunt.py and run the program from the run tab.