from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import date,timedelta
import time
import argparse
# User defined modules
from siteutils import *
from csvutils import *
from dateutils import *


# Parsing arguments
parser = argparse.ArgumentParser()
parser.add_argument('-w', action='store_true',help = "Enable wholesale data scraping")
parser.add_argument("-y","--year",type=int, help = "Year to start scraping",required = True)
args = parser.parse_args()


# Initializing selenium components
driver = webdriver.Firefox()
driver.get('https://fcainfoweb.nic.in/reports/Report_Menu_Web.aspx')

# Initializing other components
date_init(args.year)
csv_init()
date_in = rdate()
site_init(driver)

# Scraping loop
while(date_in != None):
    fillform(driver,args.w)
    filldate(driver,date_in)
    if(check_error(driver)):
        print("Error on day: "+fdate(rdate()))
        driver.get('https://fcainfoweb.nic.in/reports/Report_Menu_Web.aspx')
    else:
        data = [str(fdate(date_in))]
        data.extend(extract(driver))
        saverow(data)
        back(driver)
        print(fdate(rdate())+" Success")
    date_in = inc()

print("\n"+"*"*5+"Scrapping succesfull"+"*"*5)
