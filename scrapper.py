from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import date,timedelta
import time
# User defined modules
from siteutils import *
from csvutils import *
from dateutils import *

driver = webdriver.Firefox()
driver.get('https://fcainfoweb.nic.in/reports/Report_Menu_Web.aspx')

date_init(2014)
csv_init()
date_in = rdate()
site_init(driver)


while(date_in != None):
    fillform(driver)  # pass True to scrape wholesale data
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
