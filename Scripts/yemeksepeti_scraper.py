import time
import winsound
import ctypes
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from data_manager import get_mailAddress, get_mail_authLink, random_firstName, random_lastName, random_date, random_password

PATH = "D:\App Folders\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

_UserAgentCode="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"

def YS_signup_mailStep():
    driver = webdriver.Chrome(executable_path=PATH, options=options)
    driver.implicitly_wait(20)
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    driver.execute_cdp_cmd("Network.setUserAgentOverride", {
        "userAgent": _UserAgentCode})
    driver.get("https://www.yemeksepeti.com/login/new?step=email")

    if (driver.title == "Access to this page has been denied"):
        winsound.Beep(1276, 700)
        ctypes.windll.user32.MessageBoxW(0, "You have got 50 seconds to pass captcha or just restart the app.", "Bot Detected", 1)

    WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.ID, "email")))
    driver.execute_script("""
    var element = document.querySelector('#usercentrics-root');
    if (element)
        element.parentNode.removeChild(element);
    """)
    driver.find_element(By.ID, "email").click()
    time.sleep(0.6)
    driver.find_element(By.ID, "email").send_keys(get_mailAddress())
    time.sleep(1.2)
    driver.find_element(By.ID, "email").send_keys(Keys.ENTER)
    time.sleep(5.7)
    driver.find_element(By.XPATH, "//button[@type=\'submit\']").click()
    time.sleep(2.5)
    driver.close()

def YS_signup_secondPhase():
    driver = webdriver.Chrome(executable_path=PATH, options=options)
    driver.implicitly_wait(20)
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    driver.execute_cdp_cmd("Network.setUserAgentOverride", {
        "userAgent": _UserAgentCode})
    driver.get(get_mail_authLink())

    if (driver.title == "Access to this page has been denied"):
        winsound.Beep(1276, 700)  
        ctypes.windll.user32.MessageBoxW(0, "You have got 50 seconds to pass captcha or just restart the app.", "Bot Detected", 1)  

    WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.ID, "first_name")))
    driver.execute_script("""
    var element = document.querySelector('#usercentrics-root');
    if (element)
        element.parentNode.removeChild(element);
    """)
    driver.find_element(By.ID, "first_name").click()
    time.sleep(0.9)
    driver.find_element(By.ID, "first_name").send_keys(random_firstName())
    time.sleep(0.6)
    driver.find_element(By.ID, "last_name").click()
    time.sleep(0.6)
    driver.find_element(By.ID, "last_name").send_keys(random_lastName())
    time.sleep(0.6)
    driver.find_element(By.ID, "birthdate").click()
    time.sleep(0.8)
    driver.find_element(By.ID, "birthdate").send_keys(random_date())
    time.sleep(0.6)
    driver.find_element(By.ID, "password").click()
    time.sleep(0.7)
    driver.find_element(By.ID, "password").send_keys(random_password())
    time.sleep(1)
    winsound.Beep(1276, 300)
    winsound.Beep(3276, 300)
    time.sleep(200)
    driver.close()