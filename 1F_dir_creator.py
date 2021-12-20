from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) #ignore deprecations

your_email = "Tyler.Smith11407@gmail.com"
your_password = "UJ3B8VuYDMfhkG7"

driver = webdriver.Firefox()

driver.get("https://1fichier.com/login.pl")

email = driver.find_element_by_name("mail")
password = driver.find_element_by_name("pass")
login = driver.find_element_by_name("valider")

#print(email)

email.send_keys(your_email)
password.send_keys(your_password)
login.click()

time.sleep(3) #wait for slower computers

make = driver.find_element_by_id("mkdir")
make.click()
time.sleep(2)
new_dir = driver.find_element_by_id("new_dir")
confirm = driver.find_element_by_id("valider")
for i in range(0, 100):
	new_dir.send_keys(i)
	confirm.click()


'''
a = driver.find_elements_by_class_name("ui-draggable")
#print(a)

x = 0
wait = .4
if len(a) > 20: #if theres more than 20 file, it may impact the loading speed
	wait = .4 #so wait longer

for item in a:
	print(item)



while len(a) > 1:
	time.sleep(wait) #wait for files to load
	#print(len(a))
	a = driver.find_elements_by_class_name("ui-draggable")
	print(len(a))
	a[0].click()
	time.sleep(.7)
	print(driver.current_url)
	delete = driver.find_element_by_id("rmdir")
	delete.click()
	driver.refresh()
	x += 1

print("Removed {} directories.".format(x))
'''

#for a in li:



#driver.close()
