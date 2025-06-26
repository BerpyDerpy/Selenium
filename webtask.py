from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


USER = "seanskylar.0"
PWD = "rainbow47"

driver = webdriver.Edge()
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(4)

user_field = driver.find_element(By.NAME, "username")
pass_field = driver.find_element(By.NAME, "password")

user_field.clear()
user_field.send_keys(USER)
pass_field.clear()
pass_field.send_keys(PWD)

pass_field.send_keys(Keys.ENTER)
time.sleep(5)

try:
    notnow = driver.find_element(By.XPATH, "//div[@role='button' and text()='Not now']")
    notnow.click()
    time.sleep(3)
except Exception:
    pass

wait = WebDriverWait(driver, 15)
searchbox = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
searchbox.click()

searchbox.send_keys("cbitosc")
time.sleep(3)

firstresult = driver.find_element(By.XPATH, "//a[contains(@href, '/cbitosc/')]")
firstresult.click()
time.sleep(5)

wait = WebDriverWait(driver, 15)

wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[contains(@class,'x78zum5')]/li")))
stats = driver.find_elements(By.XPATH, "//ul[contains(@class,'x78zum5')]/li")
print(f"Found {len(stats)} stat items")

if len(stats) >= 3:
    # Posts
    numposts = stats[0].find_element(By.TAG_NAME, "span").text

    # Followers
    numfollowers = stats[1].find_element(By.TAG_NAME, "span").text

    numfollowing = stats[2].find_element(By.TAG_NAME, "span").text

else:
    raise RuntimeError("Stats block not found")

try:
    bio = driver.find_element(By.XPATH,"//section[contains(@class,'xc3tme8')]//span[contains(text(),'Learn')]").text
except:
    bio = "No bio found"


print("Posts:     ", numposts)
print("Followers: ", numfollowers)
print("Following: ", numfollowing)
print("Bio:       ", bio)

displayname = driver.find_element(By.TAG_NAME, 'h2').text
print(displayname)

try:
    followbtn = driver.find_element(By.XPATH, "//button[.//div[text()='Follow']]")
    followbtn.click()
    print("Follow button clicked")
    time.sleep(3)

except Exception:
    print("Follow button not clicked")

with open('cosc_profile.txt', 'w', encoding='utf-8') as f:
     f.write(f"Display name: {displayname}\n")
     f.write(f"Bio: {bio}\n")
     f.write(f"Followers: {numfollowers}\n")
     f.write(f"following: {numfollowing}\n")

print("Saved")

driver.quit()


