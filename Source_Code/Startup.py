#!/usr/bin/python
# -*- coding: utf-8 -*-

# Project name: Thomas Scott

# -- Importing built-in modules --

import datetime  # Importing the datetime module for use.
import os  # Importing the os module for use.
import sys  # Importing the System module for use.
import getpass  # Importing the getpass module for use.
import time  # Importing the time module for use.

# -- Importing third-party modules --
# None

# -- Importing custome modules --
# None

# -- Developer details and infomation --

__author__ = 'Thomas Scott'
__copyright__ = 'Copyright 2019, Thomas Scott'
__credits__ = ['Thomas Scott']

__license__ = 'MIT'
__version__ = '1.0.0'
__maintainer__ = 'Thomas Scott'
__email__ = '2e0eej@gmx.com'
__status__ = 'Production'


# -- Main function --

def main():
    # ↓ Displays the welcome message to the user.
    print 'System startup script had been intitaied.'
    timeNow = datetime.datetime.now()  # Getting the current date and time.
    # ↓ Formatting the date and time to become a string.
    timeNowString = timeNow.strftime('%m/%d/%Y, %H:%M:%S')
    user = getpass.getuser()  # Getting the current username.
    # ↓ Combining the date and time with the username.
    string = (user, ' Logged in at ', timeNowString)
    # ↓ Joinging together the Tuple 'string' into a str.
    strinWritabele = ''.join(string)
    print string  # Prints 'string'
    time.sleep(1)  # Pauses the application for 1 sec.
    print 'Data is being written to file.'
    try:  # Try the below unless excpetion occurs then jump to except.
        f = open('logOnLog.txt', 'a')  # Defines a new object for the file.
        f.write(strinWritabele)  # Writes a string to the opbect.
        f.close  # Closes the file object.
    except Exception, e:

                # If an exception occurs run the below code.
        # ↓ Informing the user of the error.
        print 'There was an issue writting to the file.'
        print e  # Print the error details.
        time.sleep(100)  # Pauses the application for 100 seconds.
        sys.exit()  # Exits the application cleanily.
    # ↓ Inform the user that the application has run sucessfully.
    print 'All worked well.'
    time.sleep(0.5)  # Pause the application for 1/2 a sec.
    sys.exit()  # Exits the application cleanily.


# -- Starting main function --

if __name__ == '__main__':  # If the 'main' function exists run the below code.
    main()  # Calls the 'main' function to be run.
