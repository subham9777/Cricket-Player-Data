#This code requests the data from the howstat website asynchronously and is almost 3 to 4 times faster
#than the synchronous requests.

from bs4 import BeautifulSoup
import grequests
import csv
import xlwt
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('Data')
alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z']
base_link = 'http://www.howstat.com/cricket/Statistics/Players/PlayerList.asp?Country=ALL&Group='
links = []
for i in range(len(alphabets)):
    links.append(base_link+alphabets[i])
reqs = [grequests.get(link) for link in links]
resp = grequests.map(reqs)
player_name = []
player_code = []
for r in resp:
    soup = BeautifulSoup(r.text, "lxml")
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
player_links = []
for i in range(len(player_code)):
    player_links.append(base_link_player+player_code[i])
reqs_player = [grequests.get(player_link) for player_link in player_links]
resp_player = grequests.map(reqs_player)
print(resp_player)
for i in resp_player:
    a=a+1
    print(player_name[resp_player.index(i)])
    soup1 = BeautifulSoup(i.text,"lxml")
    table1 = soup1.find("table",class_="TableLined")
    rows1 = table1.find_all('tr',{"bgcolor":["#E3FBE9","#FFFFFF"]})
    sheet.write(a,0,player_name[resp_player.index(i)])
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
    # sheet.write(a,1,date_up[-1])
    # sheet.write(a,2,aggr_up[-1])
print(a)
workbook.save("test_xyz.xls")