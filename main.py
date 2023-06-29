from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
from PIL import ImageGrab
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.page_load_strategy = "none"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://elgoog.im/dinosaur-game/")
driver.implicitly_wait(10)
driver.maximize_window()



checkbox = driver.find_element(By.ID, "botStatus") 
driver.implicitly_wait(2)
time.sleep(2)
checkbox.click()

time.sleep(3)
pyautogui.press('space')

