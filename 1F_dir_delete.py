from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) #ignore deprecations

your_email = ".com"
your_password = ""

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

a = driver.find_elements_by_class_name("ui-draggable")
wait = WebDriverWait(driver, 10)

x = 0
while len(a) > 1:
	#cd = driver.find_element_by_class_name("ui-draggable") 
	#cd.click()
	try:
		wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ui-draggable"))).click()
	except:
		break
	wait.until(EC.element_to_be_clickable((By.ID, "rmdir"))).click()
	driver.refresh()
	x += 1
	print("Removed #{}".format(x))
print("Deleted {} directories.".format(x))

driver.close()
