from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

chrome_path = "C:\selenium_driver_chrome\chromedriver.exe" #chromedriver.exe執行檔所存在的路徑
driver = webdriver.Chrome(chrome_path)

# driver = webdriver.Firefox()
driver.get("http://mops.twse.com.tw/mops/web/t163sb04")

elem = driver.find_element_by_name("year")
elem.send_keys("103")
elem = driver.find_element_by_name("season")
elem.find_element_by_xpath("//select[@name='season']/option[text()='2']").click()
driver.find_element_by_xpath("//input[@type='button'][@value=' 查詢 ']").click()

cnt = 0
delay = 10 # seconds

while True:
	try:
	    element_present = EC.presence_of_element_located((By.NAME, 'fm2'))
	    WebDriverWait(driver, delay).until(element_present)
	    print ("Page is ready!")
	    break
	except TimeoutException:
	    cnt += 1
	    print ("Load cnt=" + str(cnt))
	    if cnt >= 3:
	    	break

table = elem.find_element_by_xpath("//table[@class='hasBorder']")
for row in table.find_elements_by_xpath(".//tr[@class='even']"): 
	print([td.text for td in row.find_elements_by_xpath(".//td[@width='100px'][text()]")])

print ("end of prog...")


driver.close()
