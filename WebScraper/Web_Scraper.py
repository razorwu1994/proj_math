from bs4 import BeautifulSoup
from urllib.request import urlopen


# specify link
kith = "https://kithnyc.com/sitemap_products_1.xml"
site = urlopen(kith)
soup = BeautifulSoup(site)
dic = []
all_dates = soup.find_all("lastmod")
all_links = soup.find_all("loc")
all_links.pop(0)
all_title = soup.find_all("image:title")
for i in range(0,all_links.__len__()):

    temp = i
    if i >= all_title.__len__():
        temp = all_title.__len__()-1
    dic.append(str(all_dates[i]).lower()+ str(all_title[temp]).lower() + str(all_links[i]).lower())
flag = 0
while flag == 0:
    op = int(input("0 for key search, 1 for date search,2 for both "))
    if op == 0:
        key = str(input("Enter Keyword you want to search"))
        for i in range(0,dic.__len__()):
            if str(dic[i]).__contains__(key):
                print(str(dic[i]))

    elif op == 1:
        date = str(input("Enter the date you want to search， YYYY-MM-DD, MM-DD,HH:MM:SS,etc"))
        for i in range(0,dic.__len__()):
            if str(dic[i]).__contains__(date):
                print(str(dic[i]))

    elif op == 2:
        key = str(input("Enter Keyword you want to search"))
        date = str(input("Enter the date you want to search， YYYY-MM-DD, MM-DD,HH:MM:SS,etc"))
        for i in range(0,dic.__len__()):
            if str(dic[i]).__contains__(date):
                if str(dic[i]).__contains__(key):
                        print(str(dic[i]))
    flag = input("0 for continue , else exits")