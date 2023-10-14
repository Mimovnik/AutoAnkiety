from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

fill_forms_link_xpath = '//*[@id="i1:j_id321:j_id351"]'
forms_table_xpath = '//*[@id="i1:edt_polls_tbl:tb"]'

attendance_major_td_xpath = '//*[@id="i1:form_pollAnswer:questions_panel:0:pnl_anwsersLong"]/table/tbody/tr[1]/td'
location_at_university_td_xpath = '//*[@id="i1:form_pollAnswer:questions_panel:1:pnl_anwsersLong"]/table/tbody/tr[1]/td'
according_to_rules_whatever_td_xpath = '//*[@id="i1:form_pollAnswer:questions_panel:2:pnl_anwsersLong"]/table/tbody/tr[6]/td'
according_to_course_card_whatever_td_xpath = '//*[@id="i1:form_pollAnswer:questions_panel:3:pnl_anwsersLong"]/table/tbody/tr[6]/td'
results_on_time_whatever_td_xpath = '//*[@id="i1:form_pollAnswer:questions_panel:4:pnl_anwsersLong"]/table/tbody/tr[6]/td'
classes_understandable_whatever_td_xpath = '//*[@id="i1:form_pollAnswer:questions_panel:5:pnl_anwsersLong"]/table/tbody/tr[6]/td'
classes_intresting_whatever_td_xpath = '//*[@id="i1:form_pollAnswer:questions_panel:6:pnl_anwsersLong"]/table/tbody/tr[6]/td'
contact_availability_whatever_td_xpath = '//*[@id="i1:form_pollAnswer:questions_panel:7:pnl_anwsersLong"]/table/tbody/tr[6]/td'
social_behavior_whatever_td_xpath = '//*[@id="i1:form_pollAnswer:questions_panel:8:pnl_anwsersLong"]/table/tbody/tr[6]/td'

wait_to_load_time = 2

def enter_forms(driver):
    fill_forms_link = driver.find_element(By.XPATH, fill_forms_link_xpath)
    fill_forms_link.click()

def fill_forms(driver):
    forms_table = driver.find_element(By.XPATH, forms_table_xpath)
    forms = forms_table.find_elements(By.TAG_NAME, 'tr')
    for form in forms:
        form.click()
        time.sleep(wait_to_load_time)
        fill_form(driver)
        input()

def fill_form(driver):
    wait_to_fill_time = 0.1

    attendance_major = driver.find_element(By.XPATH, attendance_major_td_xpath).find_element(By.TAG_NAME, 'img')
    attendance_major.click();
    time.sleep(wait_to_fill_time)

    location_at_university = driver.find_element(By.XPATH, location_at_university_td_xpath).find_element(By.TAG_NAME, 'img')
    location_at_university.click();
    time.sleep(wait_to_fill_time)

    according_to_rules_whatever = driver.find_element(By.XPATH, according_to_rules_whatever_td_xpath).find_element(By.TAG_NAME, 'img')
    according_to_rules_whatever.click() 
    time.sleep(wait_to_fill_time)

    according_to_course_card_whatever = driver.find_element(By.XPATH, according_to_course_card_whatever_td_xpath).find_element(By.TAG_NAME, 'img')
    according_to_course_card_whatever.click() 
    time.sleep(wait_to_fill_time)

    results_on_time_whatever = driver.find_element(By.XPATH, results_on_time_whatever_td_xpath).find_element(By.TAG_NAME, 'img')
    results_on_time_whatever.click() 
    time.sleep(wait_to_fill_time)

    classes_understandable_whatever = driver.find_element(By.XPATH, classes_understandable_whatever_td_xpath).find_element(By.TAG_NAME, 'img')
    classes_understandable_whatever.click() 
    time.sleep(wait_to_fill_time)

    classes_intresting_whatever = driver.find_element(By.XPATH, classes_intresting_whatever_td_xpath).find_element(By.TAG_NAME, 'img')
    classes_intresting_whatever.click() 
    time.sleep(wait_to_fill_time)

    contact_availability_whatever = driver.find_element(By.XPATH, contact_availability_whatever_td_xpath).find_element(By.TAG_NAME, 'img')
    contact_availability_whatever.click() 
    time.sleep(wait_to_fill_time)

    social_behavior_whatever = driver.find_element(By.XPATH, social_behavior_whatever_td_xpath).find_element(By.TAG_NAME, 'img')
    social_behavior_whatever.click() 
    time.sleep(wait_to_fill_time)

    # submit = driver.find_element(By.XPATH,'')

    # submit.click()
    print("waiting")
    input()
    print("not")
    time.sleep(2)

driver = webdriver.Chrome()
url = "https://moja.pg.edu.pl/auth/app/student/"
driver.get(url)

try:
    WebDriverWait(driver, 3600).until(EC.url_to_be(url))
    time.sleep(wait_to_load_time)
    enter_forms(driver)
    time.sleep(wait_to_load_time)
    fill_forms(driver)
except TimeoutError:
    print("Desired url was not rendered with in allocated time")

input()