from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

your_email = ""
your_password = ""

driver = webdriver.Firefox()

driver.get("https://1fichier.com/login.pl")

email = driver.find_element_by_name("mail")
password = driver.find_element_by_name("pass")
login = driver.find_element_by_name("valider")

print(email)

email.send_keys(your_email)
password.send_keys(your_password)
login.click()

time.sleep(3) #wait for slower browsers

a = driver.find_elements_by_class_name("ui-draggable")
print(a)

x = 0
while len(a) > 1:
	a = driver.find_elements_by_class_name("ui-draggable")
	#time.sleep(.1)
	a[0].click()
	time.sleep(.7)
	print(driver.current_url)
	delete = driver.find_element_by_id("rmdir")
	delete.click()
	driver.refresh()
	x += 1

print("Removed {} directories.".format(x))

#for a in li:



#driver.close()
