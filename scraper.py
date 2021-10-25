from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time 
import csv
starturl = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("C:/Users/Dell/OneDrive/Probouy/chromedriver")
browser.get(starturl)
time.sleep(10)
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
planetdata = []
newplanetdata = []
def scrape():
    for i in range (0,428):
        Soup = BeautifulSoup(browser.page_source,"html.parser")
        current_page_num = int(Soup.find_all("input", attrs={"class", "page_num"})[0].get("value"))
        if current_page_num<i:
            browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        elif current_page_num >i:
            browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a').click()
        else:
            break
        for ultag in Soup.find_all("ul",attrs = {'class','exoplanet'}):
            litags = ultag.find_all("li")
            templist = []
            for index,litag in enumerate(litags):
                if index == 0:
                    templist.append(litag.find_all("a")[0].contents[0])
                else:
                    try:
                        templist.append(litag.contents[0])
                    except:
                        templist.append("")        
            hyperlinklitag = litags[0] 
            templist.append("https://exoplanets.nasa.gov"+hyperlink_li_tag.find_all("a", href=True)[0]["href"])

            planetdata.append (templist)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        print("page ",i)

def scrapemoredata(hyperlink):
    try:
        page = requests.get(hyperlink)
        soup = BeautifulSoup(page.content,"html.parcer")
        templist = []
        for trtag in soup.find_all("tr",attrs = {'class':'fat_row'}):
            tdtag = trtag.find_all("td")
            for td in tdtag:
                try:
                    templist.append(td.find_all("div",attrs = {"class":"value"})[0].contents[0])
                except:
                    templist.append("")
        newplantetdata.append(templist)
    except:
        time.sleep(1)
        scrapemoredata(hyperlink)
scrape()
for index,data in enumerate(planetdata):
    scrapemoredata(data[5])
finalplanetdata = []
for index,data in enumerate(planetdata):
    newplanetdataelement = newplanetdata[index]
    newplanetdataelement = [elem.replace("\n", "") for elem in new_planet_data_element]
    newplanetdataelement = newplanetdataelement[:7]
    finalplanetdata.append(data+newplanetdataelement)
with open("final.csv","w")as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(finalplanetdata)



