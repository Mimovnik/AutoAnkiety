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
submit_form_xpath='//*[@id="i1:form_pollAnswer"]'
submit_input_class_name='simpleButton'
submit_value = 'Wyślij odpowiedź'
confirm_span_xpath='//*[@id="i1:modal_confirmSendContent"]'
confirm_input_class_name='simpleButton'
confirm_value= 'Wyślij odpowiedź'

wait_timeout=3600

def click(driver, xpath):
    WebDriverWait(driver, wait_timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    clickable = driver.find_element(By.XPATH, xpath)
    clickable.click();

def fill_forms(driver):
    WebDriverWait(driver, wait_timeout).until(EC.visibility_of_element_located((By.XPATH, forms_table_xpath)))
    forms_table = driver.find_element(By.XPATH, forms_table_xpath)
    forms = forms_table.find_elements(By.TAG_NAME, 'tr')
    for i in range(len(forms)):
        WebDriverWait(driver, wait_timeout).until(EC.visibility_of_element_located((By.XPATH, forms_table_xpath)))
        forms_table = driver.find_element(By.XPATH, forms_table_xpath)
        form = forms_table.find_element(By.TAG_NAME, 'tr')
        form.click()
        fill_form(driver)

def fill_form(driver):
    click_radio_button(driver, attendance_major_td_xpath)
    click_radio_button(driver, location_at_university_td_xpath)
    click_radio_button(driver, according_to_rules_whatever_td_xpath)
    click_radio_button(driver, according_to_course_card_whatever_td_xpath)
    click_radio_button(driver, results_on_time_whatever_td_xpath)
    click_radio_button(driver, classes_understandable_whatever_td_xpath)
    click_radio_button(driver, classes_intresting_whatever_td_xpath)
    click_radio_button(driver, contact_availability_whatever_td_xpath)
    click_radio_button(driver, social_behavior_whatever_td_xpath)
    click_submit(driver, submit_form_xpath, submit_input_class_name, submit_value)
    click_submit(driver, confirm_span_xpath, confirm_input_class_name, confirm_value)


def click_radio_button(driver, xpath):
    WebDriverWait(driver, wait_timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    # without this line radio_button element is stale
    time.sleep(0.1)
    radio_button = driver.find_element(By.XPATH, xpath).find_element(By.TAG_NAME, 'img')
    radio_button.click();

def click_submit(driver, parent_xpath, input_class_name, value):
    WebDriverWait(driver, wait_timeout).until(EC.visibility_of_element_located((By.XPATH, parent_xpath)))
    # without this line element is stale
    time.sleep(0.1)
    parent = driver.find_element(By.XPATH, parent_xpath)
    classes = parent.find_elements(By.CLASS_NAME, input_class_name)

    for _class in classes:
        if(_class.get_attribute("value") == value):
            WebDriverWait(driver, wait_timeout).until(EC.visibility_of(_class))
            _class.click()
            return
        
##############################

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://moja.pg.edu.pl/auth/app/student/"
driver.get(url)

try:
    WebDriverWait(driver, wait_timeout).until(EC.url_to_be(url))

    click(driver, fill_forms_link_xpath)

    fill_forms(driver)
except TimeoutError:
    print("Desired url was not rendered with in allocated time")
