from selenium import webdriver
from selenium.webdriver.common.by import By
from data_manager import set_mailAddress, get_mailLink
import dependencies

PATH = "D:\App Folders\chromedriver.exe"

def scrapeNewMail():
    driver = webdriver.Chrome(executable_path=PATH)
    driver.get("https://generator.email/")
    emailtxt = driver.find_element(By.ID, "email_ch_text").text
    set_mailAddress(emailtxt)
    driver.close()

def checkexistingMails():
    driver = webdriver.Chrome(executable_path=PATH)
    driver.get(get_mailLink())
    driver.close()
