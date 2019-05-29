# Cricket-Player-Data
This repository contains aggregate runs for each year for every cricketer who has ever played a ODI match. The data was scraped from www.howstat.com website and the beautiful soup python library is used for the same.

# Required Libraries

1. Beautiful Soup 4 (Parsing HTML content)
2. grequests (For asynchronous Requests)
3. requests (For synchronous Requests)
4. xlwt (writing data to a excel sheet)
5. lmxl (structuring the raw html code to element tree)

The code is written in python and is tested in Python 3

# Steps to run the program

1. Download or clone the code
2. Run the code in command line : pip3 install beautifulsoup4 xlwt grequests requests lxml
3. Execute the code 
4. Code generates the excel sheet with the name of cricketers,the years they played, the aggregate runs in each year.
