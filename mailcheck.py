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


class MailChecker():
    def checkMail():

        PATH = dependencies.ChromeDriverLocation
        driver = webdriver.Chrome(PATH)

        LinkString="https://generator.email/"+dependencies.tempMail

        driver.get(LinkString)
        title = driver.title
        print(title)

        # driver.find_element(By.CSS_SELECTOR, "a:nth-child(1) > .e7m").click()

        print(dependencies.tempMail)

        element = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) > td")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        vars["window_handles"] = driver.window_handles
        driver.find_element(By.LINK_TEXT, "E-MAİL ADRESİNİ ONAYLA").click()
