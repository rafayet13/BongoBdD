from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
 
driver =webdriver.Chrome()
driver.maximize_window()

baseUrl = "https://www.bongobd.com/"
driver.get(baseUrl)

driver.find_element_by_xpath("//*[@id='content']/div[1]/nav/div/div/div[2]/div[4]/ul/li[1]/a").click()

window_before = driver.window_handles[0]
window_before_title = driver.title
driver.find_element_by_xpath("//*[@id='regNext']/span[2]").click()

window_after = driver.window_handles[1]
driver.switch_to_window(window_after)


driver.find_element_by_xpath("//*[@id='u_0_6q']").send_keys("1710493613")

driver.find_element_by_id("u_0_6r").click()
driver.implicitly_wait(10)


myElement = driver.find_element_by_name("confirmation_code")
myElement.send_keys("556723")
myElement.send_keys(Keys.ENTER)

driver.implicitly_wait(10)
browser.quit()


