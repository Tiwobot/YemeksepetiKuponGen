import sys
import time
import json
from typing import Self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from dependencies import dependencies
from mailgen import MailGenerator

PATH = dependencies.ChromeDriverLocation

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(executable_path=PATH, options=options)
driver.execute_script(
    "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

useragentarray = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
]


def yemeksepetiCreateAccount():
    for i in range(len(useragentarray)):
        driver.execute_cdp_cmd("Network.setUserAgentOverride", {
                               "userAgent": useragentarray[i]})
        print(driver.execute_script("return navigator.userAgent;"))
        driver.get("https://www.yemeksepeti.com/login/new?step=email")

    time.sleep(1.2)
    wait = WebDriverWait(driver, 3) 
    title = driver.title
    if (title=="Access to this page has been denied"):
        print("caught boting by yemeksepeti")
        sys.exit()
    try:
        driver.execute_script("""
        var l = document.getElementsByClassName("uc-default-banner")[0];
        l.parentNode.removeChild(l);
    """)
        print("cookie closer did it.")
    except:
        print("cookie closer failed.")
    time.sleep(1.8)
    driver.find_element(By.ID, "email").click()
    driver.find_element(By.ID, "email").send_keys(dependencies.tempMail)
    driver.find_element(By.XPATH, "//button[contains(.,\'Devam Et\')]").click()
    driver.find_element(
        By.XPATH, "//button[contains(.,\'Doğrulama E-postası Gönder\')]").click()
