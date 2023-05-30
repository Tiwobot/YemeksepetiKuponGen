import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from data_manager import get_mailAddress
import winsound

PATH = "D:\App Folders\chromedriver.exe"


def YS_signup_mailStep():
    driver = webdriver.Chrome(executable_path=PATH)
    driver.get("https://www.yemeksepeti.com/login/new?step=email")
    if (driver.title == "Access to this page has been denied"):
        winsound.Beep(1276, 1000)

    driver.execute_script("""
    var element = document.querySelector('#usercentrics-root');
    if (element)
        element.parentNode.removeChild(element);
    """)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "email")))
    driver.find_element(By.ID, "email").send_keys(get_mailAddress())
    driver.find_element(By.ID, "email").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@type=\'submit\']").click()
    time.sleep(1)
    driver.close()
