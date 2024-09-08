from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time

from dateutils import fdate

rw_id = "ctl00_MainContent_Ddl_Rpt_type"
pr_id="ctl00_MainContent_Rbl_Rpt_type_0"
dp_id="ctl00_MainContent_Ddl_Rpt_Option0"
da_id = "ctl00_MainContent_Txt_FrmDate"
bt_id = "btn_back"

rw_val = "Wholesale"
dpval="Daily Prices"
avgpath = "/html/body/form/div[3]/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[1]"

def site_init(driver):
    global wait
    wait = WebDriverWait(driver, 10)

def check_error(driver):
    global wait
    try:
        h3_tag = WebDriverWait(driver,1).until(
            EC.presence_of_element_located((By.TAG_NAME, "h3"))
        )
        if("inaccessible" in h3_tag.text):
            return True
    except TimeoutException:
        pass
    return False


def fillform(driver,wholesale = False):
    global pr_id,dp_id,dpval,wait
    if(wholesale):
        whole_button = wait.until(
        EC.presence_of_element_located((By.ID, rw_id))
        )
    select = Select(whole_button)
    select.select_by_visible_text(rw_val)
    radio_button = wait.until(
        EC.element_to_be_clickable((By.ID, pr_id))
    )
    radio_button.click()
    dropdown = wait.until(
        EC.presence_of_element_located((By.ID, dp_id))
    )
    select = Select(dropdown)
    select.select_by_visible_text(dpval)

def filldate(driver,date_in):
    global da_id,wait
    text_box = wait.until(
        EC.presence_of_element_located((By.ID, da_id))
    )
    text_box.send_keys(fdate(date_in))
    text_box.send_keys(Keys.ENTER)

def back(driver):
    submit_button = driver.find_element(By.ID,bt_id)
    submit_button.click()

def extract(driver):
    table = wait.until(EC.presence_of_element_located((By.XPATH, avgpath)))
    raw = (table.text).split(" ")
    data = [float(i) for i in raw[2:]]
    return data
