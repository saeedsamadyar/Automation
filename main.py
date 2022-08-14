from selenium import webdriver
from time import sleep
#from webdriver.chrome import ChromeDriverManager

driver = webdriver.Chrome("/home/myubunto/Documents/chromedriver")
#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())


driver.get("http://google.com")
sleep(2)

driver.find_element('name', 'q').send_keys("Wikipedia")
sleep(3)
driver.quit()