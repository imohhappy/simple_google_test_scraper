from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
theQues = "questions"
driver.get("https://www.google.com/search?q="+theQues)
sleep(3)
full_cont = driver.find_element_by_tag_name('body')
print(full_cont.text)

