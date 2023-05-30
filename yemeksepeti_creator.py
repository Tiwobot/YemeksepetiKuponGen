import time
import json
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


def yemeksepetiCreator():

    options = webdriver.ChromeOptions()

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(executable_path=PATH, options=options)
    driver.implicitly_wait(3)
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    useragentarray = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    ]

    for i in range(len(useragentarray)):
        driver.execute_cdp_cmd("Network.setUserAgentOverride", {
                               "userAgent": useragentarray[i]})
        print(driver.execute_script("return navigator.userAgent;"))

    driver.get(dependencies.AccountConfirmLink)
    wait = WebDriverWait(driver, 3)
    title = driver.title
    print(title)
    if (title == "Access to this page has been denied"):
        print("caught boting by yemeksepeti")
        time.sleep(10)
    element = driver.execute_script(
        """return document.querySelector('#usercentrics-root').shadowRoot.querySelector('div div div div div div div[class="sc-cCjUiG gHlwwJ"] div div div[class="sc-lllmON fjvxqY"] div button[data-testid="uc-accept-all-button"]')""")
    element.click()
    driver.close()