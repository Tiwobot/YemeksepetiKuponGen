

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
from data_manager import get_mailLink
from data_manager import set_mailAddress


PATH = "D:\App Folders\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)
driver.get(get_mailLink())
driver.close()
