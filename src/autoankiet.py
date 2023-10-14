from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

browser = webdriver.Chrome()
url = "https://docs.google.com/forms/d/e/1FAIpQLSdJwty0gzjPiVwFMBZplwXF41OV5Y_OAt0UcrpNTgaGucIS3A/viewform"
browser.get(url)
time.sleep(2)

# form inputs 
# radio buttons:
major_attendance = browser.find_element(By.XPATH, '//*[@id="i5"]/div[3]/div')
at_university = browser.find_element(By.XPATH, '//*[@id="i18"]/div[3]/div')
# yes
yes_according_to_rules = browser.find_element(By.XPATH, '//*[@id="i31"]/div[3]/div')
yes_according_to_course_card = browser.find_element(By.XPATH, '//*[@id="i53"]/div[3]/div')
yes_results_on_time = browser.find_element(By.XPATH, '//*[@id="i75"]/div[3]/div')
yes_classes_understandable = browser.find_element(By.XPATH, '//*[@id="i97"]/div[3]/div')
yes_classes_intresting = browser.find_element(By.XPATH, '//*[@id="i119"]/div[3]/div')
yes_contact_availability = browser.find_element(By.XPATH, '//*[@id="i141"]/div[3]/div')
yes_social_behavior = browser.find_element(By.XPATH, '//*[@id="i163"]/div[3]/div')
# w/e
# whatever_according_to_rules = browser.find_element(By.XPATH, '')
# whatever_according_to_course_card = browser.find_element(By.XPATH, '')
# whatever_results_on_time = browser.find_element(By.XPATH, '')
# whatever_classes_understandable = browser.find_element(By.XPATH, '')
# whatever_classes_intresting = browser.find_element(By.XPATH, '')
# whatever_contact_availability = browser.find_element(By.XPATH, '')
# whatever_social_behavior = browser.find_element(By.XPATH, '')
# text areas:
# unusual_behavior = browser.find_element(By.XPATH, '')
# other_suggestions = browser.find_element(By.XPATH, '')
submit = browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')


major_attendance.click();
at_university.click();
yes_according_to_rules.click() 
yes_according_to_course_card.click() 
yes_results_on_time.click() 
yes_classes_understandable.click() 
yes_classes_intresting.click() 
yes_contact_availability.click() 
yes_social_behavior.click() 
# submit.click()

input()