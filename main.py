from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

URL = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102157348&keywords=python%20developer&location=Jakarta%2C%20Jakarta%2C%20Indonesia"

ser = Service("C:/Users/marce/Desktop/100 days of code/chrome-driver/chromedriver.exe")
op = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=ser, options=op)
driver.get(URL)
driver.maximize_window()

signin_button = driver.find_element(By.CSS_SELECTOR, "a.nav__button-secondary.btn-md.btn-secondary-emphasis")
signin_button.click()

email = driver.find_element(By.ID, "username")
email.send_keys("marcellusgerson@gmail.com")

password = driver.find_element(By.ID, "password")
password.send_keys("Simanjuntak10")

time.sleep(1)

signin_button2 = driver.find_element(By.CSS_SELECTOR, "button.btn__primary--large.from__button--floating")
signin_button2.click()

job_openings = driver.find_elements(By.LINK_TEXT, "Python Developer")

try:

    for job_opening in job_openings:

        job_opening.click()

        save_button = driver.find_element(By.CSS_SELECTOR, "button.jobs-save-button.artdeco-button.artdeco-button--3.artdeco-button--secondary")
        save_button.click()

        html = driver.find_element(By.TAG_NAME, 'html')
        html.click()
        html.send_keys(Keys.END)

        time.sleep(2)

        follow_button = driver.find_element(By.CSS_SELECTOR, "button.follow.artdeco-button.artdeco-button--secondary.ml5")
        follow_button.click()
except NoSuchElementException:
    html = driver.find_element(By.TAG_NAME, 'html')
    html.click()
    html.send_keys(Keys.S)
