#This code requests the data from the howstat website synchronously and is almost 3 to 4 times slower than
#the asynchronous requests.


from bs4 import BeautifulSoup
import requests
import csv
import xlwt
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('My Worksheet')
alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z']
base_link = 'http://www.howstat.com/cricket/Statistics/Players/PlayerList.asp?Country=ALL&Group='
player_name = []
player_code = []
for i in alphabets:
    link_web = base_link+i
    url = requests.get(link_web).text
    soup = BeautifulSoup(url, "lxml")
    table = soup.find("table",class_="TableLined")
    rows = table.find_all('tr',{"bgcolor":["#E3FBE9","#FFFFFF"]})
    for row in rows:
        cols = row.find('a',class_="LinkNormal")
        colu = row.find_all('td')[4]
        if(colu.text.strip() !=""):
            player_name.append(cols.text)
            link = cols.get('href')
            code = str(link).rsplit('=',1)[1]
            player_code.append(code)
print(player_name)
print(player_code)
base_link_player = 'http://www.howstat.com/cricket/Statistics/Players/PlayerProgressBat_ODI.asp?PlayerID='
a =0
for i in player_code:
    a=a+1
    print(player_name[player_code.index(i)])
    link_player = base_link_player+i
    url1 = requests.get(link_player).text
    soup1 = BeautifulSoup(url1,"lxml")
    table1 = soup1.find("table",class_="TableLined")
    rows1 = table1.find_all('tr',{"bgcolor":["#E3FBE9","#FFFFFF"]})
    sheet.write(a,0,player_name[player_code.index(i)])
    date = []
    aggr = []
    date_up = []
    aggr_up = []
    for row in rows1:
        cols = row.find('a',class_="LinkNormal")
        colu = row.find_all('td')[9]
        code = str(cols.text).rsplit('/',1)[1]
        date.append(code)
        aggr.append(colu.text.strip())
    for y in range(len(date)-1):
        if (date[y] == date[y+1]):
            continue
        else:
            date_up.append(date[y])
            aggr_up.append(aggr[y])
    date_up.append(date[-1])
    aggr_up.append(aggr[-1])
    for q in range(len(date_up)):
        sheet.write(a,1,date_up[q])
        sheet.write(a,2,aggr_up[q])
        a =a + 1
    sheet.write(a,1,date_up[-1])
    sheet.write(a,2,aggr_up[-1])
print(a)
workbook.save("test.xls")