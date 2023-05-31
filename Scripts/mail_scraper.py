from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data_manager import set_mailAddress, get_mailLink, set_mail_authLink

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
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id=\"email-table\"]/div[2]/div[4]/div[3]/center/div[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/th/a")))
    set_mail_authLink(driver.find_element(
        By.XPATH, "//*[@id=\"email-table\"]/div[2]/div[4]/div[3]/center/div[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/th/a").get_attribute("href"))
    driver.close()
