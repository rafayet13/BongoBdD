from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class SlideShow():

    def test1(self):
        baseUrl = "https://www.bongobd.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        driver.switch_to.frame(0)

        driver.find_element(By.XPATH, "//*[@id='my-slider']/div[1]/div[2]/div[2]/i").click()
        time.sleep(2)
        

ff = SlideShow()
ff.test1()
