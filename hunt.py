#Hunt.py
#This program uses Wisconsin deer hunting data that is searchable by county name
#The imported csv file contains the data by county name, number of tags issued,
#and number of deer harvested based on data from the year 2019

import csv


def code_dictionary():
    f = open('hunting success.csv', 'r')
    #open csv for reading
    reader = csv.reader(f)
    hunt = {}
    #create dictionary
    for row in reader:
        hunt[row[0]]=myClass(row[0], float(row[1]), float(row[2]))
    #read csv file and  loop over the lines of the csv file,
    #and for each line, create an instance of myClass
    f.close()
    return hunt

class myClass():
    #creates class with instance variables as the three data colomns in the csv
    def __init__(self, county, issued, harvested):
        self.county = county
        self.issued = issued
        self.harvested = harvested
    #added method to calculate successrate percentage
    def success(self):
        return round(self.harvested/self.issued *100, 2)
    #returns a rounded float number two decimal places
def success_rate():
    #function for calling the successrate later in the program
    hunt = code_dictionary()
    county = input("Which county do you want to find the hunting success rate?(All Uppercase): ")
    #defines the three objects in the class if the county is inputed correctly
    if county in hunt:
        issued = hunt[county].issued
        harvested = hunt[county].harvested                                         
        rate = myClass(county, issued, harvested)
        print(rate.success(), 'percent success rate')
    else:
        print("county not found")
    #calls success method from myClass
    return main()

def query_hunt_code():
    #first input function, asks for user to input a county name
    hunt = code_dictionary()

    county = input("Please name a county in Wisconsin(All Uppercase): ")

    if county in hunt :
    #returns number of tags issued and deer harvested for the couny inputed 
        print('Tags issued',hunt[county].issued, 'Deer harvested',hunt[county].harvested)
    else:
        print("county not found")
    #County name must be all uppercase or it will return 'county not found'
query_hunt_code()

def main():
    print("What else would you like to do?")
    
    while True:
        
        decide = int(input('1 - Search another county \n2 - Find success rate\n3 - quit\nPlease select a number: '))

        if decide ==1:
            ans = query_hunt_code(), main()
        #makes sure the program loops over again instead of quitting
            break
        elif decide ==2:
            ans = success_rate()
        #calls the success rate function
            break
        elif decide ==3:
        #quits the program
            ans = quit
            break
        else:
            print('Please enter a number between 1 and 3\n')
    return ans
main()
        



    
