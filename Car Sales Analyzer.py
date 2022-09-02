'''
Project 3 - Car Sales Analyzer - Spring 2021 
Author: Matthias Cannon matthiasc@vt.edu

Car Sales Analysis.

I have neither given or received unauthorized assistance on this assignment.
Signed:  Matthias Cannon
'''

def get_data(filename, type): #Reads the file and returns a list of prices 
    lines = []
    with open(filename,'r') as file: #With statement to make sure file doesnt remain open when not in use 
        lines=file.readlines()
    prices=[]
    for line in lines:
        words=line.split() #splits a long string at the spaces 
        if words [0].lower()==type:
            prices.append(int(words[1])) #adds price to a list called prices
    return prices
    

    
    
    
def count_range(saleprices, minimum, maximum): #goes through list of prices and checks whether it is within the range and then incrememnts a counter if so 
    count = 0
    for price in saleprices:
        if price <= maximum and price >= minimum: 
            count = count + 1
    return count
    

def main(): #Represents the main program being run 
    print('Welcome to the Car Sales Analyzer!')
    print()
    filename=  input('Enter the name of the data file: ')
    usedprices=get_data(filename,'u') #gets and finds data specifically in the used section
    usedunder= count_range(usedprices ,0,9999)
    usedbetween= count_range(usedprices ,10000,20000)
    usedover= len(usedprices)-usedunder-usedbetween
    usedaverage= sum(usedprices) // len(usedprices)
    
    newprices=get_data(filename, 'n') #brings back data under the new category 
    newunder= count_range(newprices, 0,29999)
    newbetween= count_range(newprices, 30000, 45000)
    newover = len(newprices)-newunder-newbetween
    newaverage= sum(newprices) // len(newprices)
    
    print()#used for space 
    print('Used Cars')#formatting of program from line 51-65 
    print('    Under 10K: ' + str(usedunder))
    print('    10K - 20K: ' + str(usedbetween))
    print('    Over 20K: ' + str(usedover))
    print()
    print('Average: ' + str(usedaverage))
    print()
    print('New Cars')
    print('    Under 30K: ' + str(newunder))
    print('    30K - 45K: ' + str(newbetween))
    print('    Over 45K: ' + str(newover))
    print()
    print('Average: ' + str(newaverage))
    print()
    print('Thanks for using the Car Sales Analyzer!')
  
if __name__=="__main__":
    main() 