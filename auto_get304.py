from selenium import webdriver
import time
import codecs

chrome_path = "C:\selenium_driver_chrome\chromedriver.exe" #chromedriver.exe執行檔所存在的路徑
web = webdriver.Chrome(chrome_path)

web.get('http://www.51bxg.com/web/login_register/login.aspx')

username = web.find_element_by_xpath("//input[@id='login_name']")
username.send_keys("vinceliu")

password = web.find_element_by_xpath("//input[@id='login_password']")
password.send_keys("yusco07")

web.find_element_by_xpath("//button[@id='login_btn']").click()
time.sleep(5)

#web.find_element_by_link_text('板卷报价').click()
#web.find_element_by_link_text('板卷報价').click()

#web.get('http://www.51bxg.com//web/data_center/coil_price_list.aspx?type=%E5%8D%B7&mkt=%E6%97%A0%E9%94%A1%E5%B8%82%E5%9C%BA')
web.get('http://www.51bxg.com//web/data_center/coil_price_list.aspx')


time.sleep(5)
type = web.find_element_by_id('type_array')
type.send_keys("卷")

