#This is a webscraper bot that detects if an item is in stock in
#Canada Computers. While TRUE, it will keep scanning if the item is in stock
#Copyright to Jack Jabra all rights reserved.
#Any selling or illegal distribution of this code will be subject to prosecution.


print("Thank you for using my Stock Scanner for Canada Computer. The GPU market has been beyond insane, and hopefully this tool will ease your F5 finger pain.\n")
print("__Developer__: Jack Jabra\n")
print("__Copyright__: Copyright © 2021 Jack Jabra\n")
print("__License__: Public\n")
print("__Version: 1.0\n")
print("DISCLAIMER: I will not be held responsible for the illigitimate use of this tool or if your IP gets blocked by websites.\n")




import requests
from bs4 import BeautifulSoup   
import time
import winsound
import webbrowser

search = True

while True:
    
    url = input('Paste the URL of the item here: ')
    
    if "canadacomputers" not in url:
        
        print("Not a Canada Computers link Jackass...Try Again\n")
        
        continue
    #ADDED ERROR EXCEPTION FOR WHEN USER PASTES LINK WITHOUT HTTP OR HTTPS. NEEDS TO BE FULL URL.
    elif "http" and "https" not in url:

        print("Invalid Link Format. Please make sure to include the full link with https://www. or http://www.\n")
        continue
        
    else:
        
        break

while True:
    
    try: 
        delay = float(input("Enter delay time between scans in minutes: "))
        break
        
    except:
        
        print("This is not a valid option. Please choose a number...")
        
        
delay = delay * 60





def initiate():


    global page
    global soup

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    print(f'Scanning stock availability for: {soup.title.string}\n')

def checkstock():

    global search 

    outofstock = str(soup.find(content="OutOfStock"))
    instock = str(soup.find(content="InStock"))

    out_of_stock = "OutOfStock" in outofstock
    in_stock = "InStock" in instock

    if out_of_stock == True and in_stock == False:

        search = True

    else:

        search = False


while search:

    initiate()

    checkstock()

    #To avoid getting IP blocked, if search returns False, we found the product and we'll break the loop to notify the user
    #If search is still True, it means the product is still out of stock, we will pass to the time.sleep to delay searches, then since search
    #is still True, the while loop continues
    

    if search == False:

        break

    else:
        pass

    print(f"Waiting {delay/60} minutes...\n")

    time.sleep(delay)


print("ITEM IN STOCK!")
print("Press Ctrl+C To Open Item Webpage")

try:

    while True:

        winsound.Beep(800,1000)

except KeyboardInterrupt:

    print("Press any button to open webpage")

    pass

webbrowser.open(url)











