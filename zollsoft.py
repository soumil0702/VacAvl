'''
Created on 7 Jun 2021

@author: soumi
'''
from selenium import webdriver

if __name__ == '__main__':
    pass

# Importing libraries
import time
import webbrowser
import hashlib
from urllib.request import urlopen, Request

# setting the URL you want to monitor
url = Request('https://onlinetermine.zollsoft.de/patientenTermine.php?uniqueident=6087dd08bd763')
#url = Request('https://peaceful-sea-40539.herokuapp.com/blogs/5e02c178d2b0640017c122de')

# to perform a GET request and load the
# content of the website and store it in a var
response = urlopen(url).read()

# to create the initial hash
currentHash = hashlib.sha224(response).hexdigest()
print("running")
while True:

    try:
        # perform the get request and store it in a var
        response = urlopen(url).read()
        
        # create a hash
        currentHash = hashlib.sha224(response).hexdigest()
        
        x=2
        
        # wait for 30 seconds
        time.sleep(20)
        
        # perform the get request
        response = urlopen(url).read()
        # create a new hash
        newHash = hashlib.sha224(response).hexdigest()
        

        # check if new hash is same as the previous hash
        if newHash == currentHash:
            continue

        # if something changed in the hashes
        else:
            # notify
            
            print("something changed")

            # again read the website
            # response = urlopen(url).read()

            # create a hash
            # currentHash = hashlib.sha224(response).hexdigest()

            # wait for 30 seconds
#            webbrowser.open('https://onlinetermine.zollsoft.de/patientenTermine.php?uniqueident=6087dd08bd763')
            webbrowser.open('https://onlinetermine.zollsoft.de/patientenTermine.php?uniqueident=6087dd08bd763')
            time.sleep(5)
            continue
            
    # To handle exceptions
    except Exception as e:
        print("In exception \n")
        print(e)
        webbrowser.open('https://onlinetermine.zollsoft.de/patientenTermine.php?uniqueident=6087dd08bd763')

