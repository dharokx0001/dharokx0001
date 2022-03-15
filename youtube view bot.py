#install python
#windows cmd: py -m pip install selenium
#download the latest mozilla gecko driver from github
#extract the mozilla gecko driver and add the path of the geckodriver.exe to PATH in the windows system environment variables
#restart your computer

#disclaimer: do not use this software for illegal activity
#disclaimer: you, and only you, are responsible for what you do with this script
#disclaimer: download only as reading material for educational purpose

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webbrowser, time

import warnings
warnings.filterwarnings("ignore")

url = str(input("url: "))
counter = 0

for i in range(int((input("add view count: ")))):
    options = Options()
    options.headless = True #prevents the gecko driver browser from appearing
    profile = webdriver.FirefoxProfile()
    profile.set_preference("media.volume_scale", "0.0")
    driver = webdriver.Firefox(firefox_profile=profile, options=options, executable_path=r'C:\Users\0\Documents\geckodriver-v0.30.0-win64\geckodriver.exe') #copy and paste your PATH to the geckodriver.exe
    if (counter == 0):
        print("youtube view bot is running, please wait.")
    driver.get(url) #launches the url with the firefox gecko driver
    try: #handles google cookies consent overlay confirmation button
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"ytd-button-renderer.style-scope:nth-child(2) > a:nth-child(1) > tp-yt-paper-button:nth-child(1)"))).click()
        time.sleep(31) #watch time required for a youtube video to gain a view (in seconds)
        counter += 1
        print("count added:", counter)
        driver.quit()
    except: #if google cookies consent overlay confirmation button is not present, handles activation of the play-button of the video
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".ytp-play-button"))).click()
        time.sleep(31) #watch time required for a youtube video to gain a view (in seconds)
        counter += 1
        print("count added:", counter)
        driver.quit()
    finally: #if the play-button cannot be activated, continue until completion of the loop
        pass

#advertisements contribute as viewable time to a youtube video
#advertisements are handled in this script
#youtube servers might take 10 - 20 minutes to update view count for a video
