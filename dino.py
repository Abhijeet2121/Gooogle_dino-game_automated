from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from PIL import ImageGrab
import pyautogui
import numpy as np
import cv2

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.page_load_strategy = "none"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

URL = "https://elgoog.im/dinosaur-game/"
driver.get(URL)
driver.maximize_window()

box = (316, 555, 565, 690)
                   
    
pyautogui.press('down')
time.sleep(1) 
pyautogui.press('space')
while True:
# take a sceenshot
    image = ImageGrab.grab(box) 
# convert image pixel to array for cv2 and covertit its color
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    # cv2.imshow('image', image)
    
# count_pixel
    black_pixel_count = np.sum(image < 100) #pixel value less than 100 
    white_pixel_count = np.sum(image > 100) #pixel value higher than 100
    print(f"Number of balck pixels {black_pixel_count}")
    print(f"Number of White pixels {white_pixel_count}")

# now check pixel value
    
# for light mode pixel count should be 4k to 30k
    if black_pixel_count > 4000 and black_pixel_count < 30000:
        time.sleep(0.0001)
        pyautogui.press('up')

# for dark mode 
    if white_pixel_count > 4000 and white_pixel_count < 30000:
        time.sleep(0.0001)
        pyautogui.press('up')


    if cv2.waitKey(10) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
 