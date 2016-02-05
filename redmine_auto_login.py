#!coding: utf8
from selenium import webdriver

# define
url = $REDMINE_URL
username = $YOUR_USERNAME
passwd = $YOUR_PASSWORD

# login transation
driver = webdriver.Firefox()
driver.get(url)
driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(passwd)
driver.find_element_by_name('password').submit()

# logout transaction
logout = driver.find_elements_by_class_name('logout')[0]
logout.click()

# kill process
driver.quit()

