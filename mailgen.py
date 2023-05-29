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

PATH = dependencies.ChromeDriverLocation
driver = webdriver.Chrome(PATH)

driver.get("https://generator.email/")
title = driver.title
print(title)

#driver.find_element(By.CSS_SELECTOR, "a:nth-child(1) > .e7m").click()

dependencies.tempMail=driver.find_element(By.ID, "email_ch_text").text

